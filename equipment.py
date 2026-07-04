# SolarMate AI Equipment Selector

def recommend_panel(panel_size):

    if panel_size <= 200:
        return "1 × 200 W Solar Panel"

    elif panel_size <= 400:
        return "2 × 200 W Solar Panels"

    elif panel_size <= 600:
        return "2 × 300 W Mono Solar Panels"

    else:
        panels = round(panel_size / 300)
        return f"{panels} × 300 W Mono Solar Panels"


def recommend_battery(battery_size):

    if battery_size <= 100:
        return "1 × 12V 100Ah Battery"

    elif battery_size <= 200:
        return "1 × 12V 200Ah Battery"

    elif battery_size <= 400:
        return "2 × 12V 200Ah Batteries"

    else:
        batteries = round(battery_size / 200)
        return f"{batteries} × 12V 200Ah Batteries"


def recommend_inverter(inverter_size):

    if inverter_size <= 1000:
        return "1 × 1kVA Pure Sine Wave"

    elif inverter_size <= 1500:
        return "1 × 1.5kVA Pure Sine Wave"

    elif inverter_size <= 3000:
        return "1 × 3kVA Pure Sine Wave"

    else:
        return "Contact Installer for Custom Inverter"