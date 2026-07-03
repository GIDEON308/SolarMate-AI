# SolarMate AI Load Builder

load_list = []


def add_appliance(name, power, quantity, hours):
    """Add an appliance to the load schedule."""

    energy = power * quantity * hours

    load_list.append({
        "name": name,
        "power": power,
        "quantity": quantity,
        "hours": hours,
        "energy": energy
    })


def get_load_schedule():
    """Return the complete load schedule."""
    return load_list


def total_daily_energy():
    """Calculate total daily energy."""
    return sum(item["energy"] for item in load_list)


def clear_load_schedule():
    """Clear the load schedule."""
    load_list.clear()