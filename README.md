[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

## Installation instructions (external Grocy install):

1. Install HACS for Home Assistant
2. Go to Community > Store > Grocy
3. Install the Grocy integration
4. Restart Home Assistant
5. Go to Grocy > Wrench icon > Manage API keys > Add
6. Copy resulting API key
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Grocy"
8. You will now have a new integration for Grocy. Some or all of the entities might be disabled from the start.

(This component will not currently work if you have an install where you don't use a port, due to [this](https://github.com/SebRut/pygrocy/issues/121).)


## Additional installation instructions for Hass.io users

The configuration is slightly different for users that use Hass.io and the [official Grocy addon](https://github.com/hassio-addons/addon-grocy) from the Hass.io Add-on store.

1. If you haven't already done so, install Grocy from the add-on store
2. In the 'Network' section of the add-on config, input 9192 in the host field [screenshot](https://github.com/custom-components/grocy/raw/master/grocy-addon-config.png). Save your changes and restart the add-on.
3. Install HACS for Home Assistant
4. Go to Community > Store > Grocy
5. Install the Grocy integration
6. Restart Home Assistant
7. Go to Grocy > Wrench icon > Manage API keys > Add
8. Copy resulting API key
9. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Grocy"
10. You will now have a new integration for Grocy. Some or all of the entities might be disabled from the start.