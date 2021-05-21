# PushPlus
 [PushPlus](http://www.pushplus.plus) For HomeAssistant notification.

## Installation
### HACS (recommended)
1. In `Integrations` section add custom repositories URL `https://github.com/wubin2/pushplus`.
2. Category choose `Integrations`.
3. Install added repository.
### Manual
1. Install this component by copying [these files](https://github.com/wubin2/pushplus/tree/master/custom_components/pushplus) to `custom_components/pushplus/`.
2. Add the code to your `configuration.yaml` using the config options below.
3. Restart HomeAssistant.

## Configuration
### Example for configuration.yaml:
```yaml
notify:
  - platform: pushplus
    name: pushplus
    token: !secret pushplus_token
    topic: 888888
    template: html
```
### Options
| Key | Default |Required | Description |
|---|---|---|---|
| token | - | true | Your pushplus token  |
| topic | - | false | Group code, leave blank to send it to yourself |
| template | html | true | Choose a template:  `html`,`txt`,`json`,`markdown` |
| name | - | false | Name of notify |

## License
This project is licensed under MIT license. See [LICENSE](LICENSE) file for details.
