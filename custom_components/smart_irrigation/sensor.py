from homeassistant.helpers.entity import Entity
from homeassistant.const import STATE_ON, STATE_OFF
import logging

_LOGGER = logging.getLogger(__name__)

class SmartIrrigationSensor(Entity):
    """Representation of a Smart Irrigation Sensor."""

    def __init__(self, name, sensor_type, state):
        self._name = name
        self._sensor_type = sensor_type
        self._state = state

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unique_id(self):
        """Return a unique ID for this sensor."""
        return f"{self._sensor_type}_{self._name}"

    @property
    def device_class(self):
        """Return the class of this sensor."""
        return self._sensor_type

    def update(self):
        """Fetch new state data for the sensor."""
        # Logic to update the sensor state goes here
        _LOGGER.debug("Updating sensor state for %s", self._name)
        # Example: self._state = fetch_sensor_data()

class SoilMoistureSensor(SmartIrrigationSensor):
    """Representation of a Soil Moisture Sensor."""

    def __init__(self, name):
        super().__init__(name, "soil_moisture", STATE_OFF)

class RainSensor(SmartIrrigationSensor):
    """Representation of a Rain Sensor."""

    def __init__(self, name):
        super().__init__(name, "rain", STATE_OFF)

class TemperatureSensor(SmartIrrigationSensor):
    """Representation of a Temperature Sensor."""

    def __init__(self, name):
        super().__init__(name, "temperature", STATE_OFF)