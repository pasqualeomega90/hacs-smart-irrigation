from homeassistant.helpers import discovery
from homeassistant import config_entries
from .const import DOMAIN

async def async_setup(hass, config):
    """Set up the Smart Irrigation integration."""
    hass.data[DOMAIN] = {}
    # Load services
    await discovery.async_load_platform(hass, 'sensor', DOMAIN, {}, config)
    await discovery.async_load_platform(hass, 'switch', DOMAIN, {}, config)
    return True

async def async_setup_entry(hass, entry: config_entries.ConfigEntry):
    """Set up Smart Irrigation from a config entry."""
    hass.data[DOMAIN][entry.entry_id] = entry.data
    # Load services and entities
    await discovery.async_load_platform(hass, 'sensor', DOMAIN, {}, entry)
    await discovery.async_load_platform(hass, 'switch', DOMAIN, {}, entry)
    return True

async def async_unload_entry(hass, entry: config_entries.ConfigEntry):
    """Unload a config entry."""
    unload_ok = all(
        await discovery.async_unload_platform(hass, platform)
        for platform in ('sensor', 'switch')
    )
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok