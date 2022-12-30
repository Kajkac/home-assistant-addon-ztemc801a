import datetime
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (
    ATTR_FRIENDLY_NAME,
    CONF_NAME
)
from homeassistant.helpers.entity import Entity

CONF_SHOW_SECONDS = 'show_seconds'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default="Current Time"): cv.string,
    vol.Optional(CONF_SHOW_SECONDS, default=False): cv.boolean
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    name = config.get(CONF_NAME)
    show_seconds = config.get(CONF_SHOW_SECONDS)

    add_entities([CurrentTimeSensor(name, show_seconds)])

class CurrentTimeSensor(Entity):
    def __init__(self, name, show_seconds):
        self._name = name
        self._show_seconds = show_seconds
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    def update(self):
        now = datetime.datetime.now()
        if self._show_seconds:
            self._state = now.strftime("%H:%M:%S")
        else:
            self._state = now.strftime("%H:%M")

