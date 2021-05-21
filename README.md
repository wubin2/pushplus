# pushplus
 [PushPlus](http://www.pushplus.plus) For HomeAssistant

## Installation
1. Install this component by copying [these files](https://github.com/wubin2/pushplus/tree/master/custom_components/pushplus) to `custom_components/pushplus/`.
2. Add the code to your `configuration.yaml` using the config options below.
3. Restart HomeAssistant.

### Options
| Key | Default |Required | Description |
|---|---|---|---|
| token |  | yes | your token  |
| topic |  | no | group code, leave blank to send to yourself |
| template | html | yes | html\txt\json\markdown |
| name | pushplus | no |  |

## Exemples
### Example for configuration.yaml:
```yaml
notify:
  - platform: pushplus
    name: pushplus
    token: !secret pushplus_token
    topic: 888888
    template: html
```

## License
This project is licensed under MIT license. See [LICENSE](LICENSE) file for details.
