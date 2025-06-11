DOMAIN = "juntek"

async def async_setup_entry(hass, entry):
    """Set up Juntek from a config entry."""
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True

async def async_unload_entry(hass, entry):
    """Unload Juntek config entry."""
    return await hass.config_entries.async_forward_entry_unload(entry, "sensor")