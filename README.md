# Juntek Battery Monitor Integration

This is a custom Home Assistant integration that connects to a Junctek battery monitor over BLE (Bluetooth Low Energy).

## Features

- Reads voltage, current, capacity, and battery percentage.
- Exposes them as native Home Assistant sensors.
- No need for MQTT or external add-ons.

## Installation via HACS

1. Go to HACS → Integrations → Custom repositories.
2. Add this repository's URL and select category "Integration".
3. Search for "Juntek Battery Monitor" and install it.
4. Restart Home Assistant.

## Manual Installation

Copy the `juntek` folder inside `custom_components` into your Home Assistant's `config/custom_components/`.

## Configuration

```yaml
sensor:
  - platform: juntek
```

## Notes

This integration is based on the logic from the original Junctek add-on by Tsjippy, refactored into a native integration.
