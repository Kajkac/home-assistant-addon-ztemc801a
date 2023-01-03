import requests
import homeassistant.helpers.config_validation as cv
import voluptuous as vol

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (CONF_NAME)
from homeassistant.helpers.entity import Entity

CONF_EXTERNAL_URL = 'external_url'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_NAME): cv.string,
    vol.Optional(CONF_EXTERNAL_URL, default='https://api.ipify.org'): cv.string,
})

@ha.callback
def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    async_add_entities([MySensor(hass, config)])

class MySensor(Entity):
    def __init__(self, hass, config):
        self._name = config.get(CONF_NAME)
        self._external_url = config.get(CONF_EXTERNAL_URL)
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    async def async_update(self):
        self._state = requests.get(self._external_url).text
