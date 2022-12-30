import homeassistant.helpers.config_validation as cv
import voluptuous as vol
import requests
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (
    ATTR_FRIENDLY_NAME,
    CONF_NAME
)
from homeassistant.helpers.entity import Entity

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default="Public IP Address"): cv.string,
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    name = config.get(CONF_NAME)

    add_entities([PublicIPSensor(name)])

class PublicIPSensor(Entity):
    def __init__(self, name):
        self._name = name
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    def update(self):
        response = requests.get("https://api.ipify.org")
        self._state = response.text
