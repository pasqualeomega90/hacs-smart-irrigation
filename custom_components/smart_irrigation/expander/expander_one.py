from homeassistant.helpers.entity import Entity
from homeassistant.const import CONF_NAME

class ExpanderOne(Entity):
    def __init__(self, name: str):
        self._name = name
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    def update(self):
        # Logica per aggiornare lo stato dell'espandibile
        pass

    def turn_on(self):
        # Logica per attivare l'espandibile
        self._state = "on"

    def turn_off(self):
        # Logica per disattivare l'espandibile
        self._state = "off"