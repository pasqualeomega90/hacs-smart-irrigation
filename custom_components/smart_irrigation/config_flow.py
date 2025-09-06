from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN

class SmartIrrigationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    def __init__(self):
        super().__init__()
        self._user_input = {}

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            self._user_input = user_input
            return self.async_create_entry(title="Smart Irrigation", data=self._user_input)

        return self.async_show_form(step_id="user")

    @callback
    def _async_get_options_flow(self, config_entry):
        return SmartIrrigationOptionsFlow(config_entry)

class SmartIrrigationOptionsFlow(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(step_id="init")