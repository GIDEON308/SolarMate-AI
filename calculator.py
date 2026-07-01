def calculate_system(daily_energy_wh, sun_hours, battery_voltage, backup_days):
    adjusted_energy = daily_energy_wh * 1.2

    panel_size = adjusted_energy / sun_hours

    battery_ah = (adjusted_energy * backup_days) / battery_voltage

    inverter = max(1000, int(daily_energy_wh / 2))

    return {
        "panel": round(panel_size),
        "battery": round(battery_ah),
        "inverter": inverter
    }
    