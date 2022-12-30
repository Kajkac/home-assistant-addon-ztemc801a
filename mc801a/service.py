import requests

import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.const import CONF_NAME
from homeassistant.helpers.aiohttp_client import async_get_clientsession

CONF_API_TOKEN = '89244a3de7ecdd'

PLATFORM_SCHEMA = vol.Schema({
    vol.Required(CONF_NAME): cv.string,
    vol.Required(CONF_API_TOKEN): cv.string,
})

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    name = config[CONF_NAME]
    api_token = config[CONF_API_TOKEN]

    session = async_get_clientsession(hass)

    async_add_entities([PublicIPSensor(name, session, api_token)])

class PublicIPSensor(Entity):
    def __init__(self, name, session, api_token):
        self._name = name
        self._session = session
        self._api_token = api_token
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    async def async_update(self):
        api_url = "https://ipinfo.io/ip"
        headers = {"Authorization": f"Bearer {self._api_token}"}

        async with self._session.get(api_url, headers=headers) as response:
            self._state = await response.text()
