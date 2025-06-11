from homeassistant import config_entries
import voluptuous as vol

DOMAIN = "juntek"

class JuntekConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLLING

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(
                title=f"Juntek {user_input['mac']}",
                data=user_input,
            )

        schema = vol.Schema({
            vol.Required("mac"): str,
            vol.Required("battery_voltage"): vol.In(["12V", "24V"]),
        })

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
        )
