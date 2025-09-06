import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN

DATA_SCHEMA = vol.Schema({
    vol.Required("name", default="Irrigazione Smart MultiZona"): str,
    vol.Required("zone_count", default=2): int,
    vol.Required("durata_zona_1", default=10): int,
    vol.Required("durata_zona_2", default=10): int,
    vol.Required("modalita_zona_1", default="automatica"): vol.In(["manuale", "automatica"]),
    vol.Required("modalita_zona_2", default="automatica"): vol.In(["manuale", "automatica"]),
    vol.Required("orario_zona_1", default="alba"): vol.In(["alba", "tramonto"]),
    vol.Required("offset_zona_1", default=0): int,
    vol.Required("orario_zona_2", default="alba"): vol.In(["alba", "tramonto"]),
    vol.Required("offset_zona_2", default=0): int,
})

class SmartIrrigationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Gestione del flusso di configurazione tramite UI."""

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title=user_input["name"], data=user_input)
        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA, errors=errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return SmartIrrigationOptionsFlowHandler(config_entry)

class SmartIrrigationOptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)
        return self.async_show_form(
            step_id="init",
            data_schema=DATA_SCHEMA,
            errors=errors,
        )