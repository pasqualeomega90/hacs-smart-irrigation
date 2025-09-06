from homeassistant.helpers import discovery

def setup_expanders(hass):
    discovery.load_platform(hass, 'sensor', 'smart_irrigation.expander', {}, {})
    discovery.load_platform(hass, 'switch', 'smart_irrigation.expander', {}, {})