# SolarMate AI Pricing Database

PANEL_PRICES = {
    "1 × 200 W Solar Panel": 120000,
    "2 × 200 W Solar Panels": 240000,
    "2 × 300 W Mono Solar Panels": 360000
}

BATTERY_PRICES = {
    "1 × 12V 100Ah Battery": 260000,
    "1 × 12V 200Ah Battery": 500000,
    "2 × 12V 200Ah Batteries": 1000000
}

INVERTER_PRICES = {
    "1 × 1kVA Pure Sine Wave": 180000,
    "1 × 1.5kVA Pure Sine Wave": 280000,
    "1 × 3kVA Pure Sine Wave": 500000
}

INSTALLATION_COST = 80000


def estimate_cost(panel, battery, inverter):
    panel_cost = PANEL_PRICES.get(panel, 0)
    battery_cost = BATTERY_PRICES.get(battery, 0)
    inverter_cost = INVERTER_PRICES.get(inverter, 0)

    total = (
        panel_cost +
        battery_cost +
        inverter_cost +
        INSTALLATION_COST
    )

    return {
        "panel_cost": panel_cost,
        "battery_cost": battery_cost,
        "inverter_cost": inverter_cost,
        "installation": INSTALLATION_COST,
        "total": total
    }