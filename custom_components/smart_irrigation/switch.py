from homeassistant.components.switch import SwitchEntity
from .const import DOMAIN, SWITCH_NAME, SWITCH_ICON

class SmartIrrigationSwitch(SwitchEntity):
    def __init__(self, controller):
        self._controller = controller
        self._is_on = False

    @property
    def name(self):
        return SWITCH_NAME

    @property
    def icon(self):
        return SWITCH_ICON

    @property
    def is_on(self):
        return self._is_on

    async def async_turn_on(self, **kwargs):
        await self._controller.start_irrigation()
        self._is_on = True
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        await self._controller.stop_irrigation()
        self._is_on = False
        self.async_write_ha_state()