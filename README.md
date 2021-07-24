
# PushPlus
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/wubin2/pushplus)
[![buymeacoffee_badge](https://img.shields.io/badge/Donate-Buy%20Me%20a%20Coffee-ff813f?style=flat)](https://www.buymeacoffee.com/holala)

[PushPlus](http://www.pushplus.plus) notification for homeassistant.

## Installation
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

[![alt text](http://img1.coolsong.com/imgs/2021/05/49b7e0a6af0a43b6.png "Buy Me A Coffee")](https://www.buymeacoffee.com/holala)
