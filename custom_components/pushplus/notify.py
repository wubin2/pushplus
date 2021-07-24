"""PushPlus V1.2 For HomeAssistant by wubin2"""
import logging
import datetime
import requests
import voluptuous as vol

from homeassistant.components.notify import (
    ATTR_MESSAGE, ATTR_TITLE, ATTR_DATA, ATTR_TARGET, PLATFORM_SCHEMA, BaseNotificationService)
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)
_RESOURCE = 'http://www.pushplus.plus/send'

CONF_TOKEN = 'token'
CONF_TOPIC= 'topic'
CONF_TEMPLATE= 'template'
def get_service(hass, config, discovery_info=None):
    token = config.get(CONF_TOKEN )
    topic = config.get(CONF_TOPIC )
    template = config.get(CONF_TEMPLATE )
    return PushPlusNotificationService(hass, token, topic, template)

class PushPlusNotificationService(BaseNotificationService):
    def __init__(self, hass, token, topic, template):
        _LOGGER.debug("INIT message")
        self._token = token
        self._topic = topic
        self._template = template
    def send_message(self, message='', **kwargs):
        url = '{}?token={}&topic={}&template={}&'.format(_RESOURCE, self._token, self._topic, self._template)
        title = kwargs.get(ATTR_TITLE)
        if title:
           timestp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           sendmessage = '{} {}'.format(timestp, message)
           payload = {'title': title, 'content': sendmessage}
           response = requests.get(url,params = payload)
           _LOGGER.debug("sneding out message")
           if response.status_code != 200:
              obj = response.json()
              error_message = obj['error']['message']
              error_code = obj['error']['code']
              _LOGGER.error(
                   "Error %s : %s (Code %s)", resp.status_code, error_message,
                   error_code)
        else:
           _LOGGER.error("Title can NOT be null")
