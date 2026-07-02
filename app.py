import gradio as gr

from appliances import APPLIANCES
from calculator import calculate_system


def solar_calculator(appliance, quantity, hours):

    power = APPLIANCES[appliance]

    daily_energy = power * quantity * hours

    result = calculate_system(
        daily_energy,
        5,      # Peak Sun Hours
        24,     # Battery Voltage
        1       # Backup Days
    )

    return f"""
# ☀️ SolarMate AI Version 4

## Appliance Selected

**{appliance}**

Power Rating: **{power} W**

Quantity: **{quantity}**

Hours per Day: **{hours}**

---

## Daily Energy Consumption

**{daily_energy:.0f} Wh/day**

---

## Recommended Solar System

☀️ Solar Panel: **{result['panel']} W**

🔋 Battery: **{result['battery']} Ah**

⚡ Inverter: **{result['inverter']} W**
"""


with gr.Blocks(title="SolarMate AI Version 4") as demo:

    gr.Markdown("# ☀️ SolarMate AI")
    gr.Markdown("## Dynamic Appliance Selector")

    appliance = gr.Dropdown(
        choices=sorted(APPLIANCES.keys()),
        label="Select Appliance",
        value="LED Bulb"
    )

    quantity = gr.Number(
        label="Quantity",
        value=1
    )

    hours = gr.Number(
        label="Hours per Day",
        value=5
    )

    output = gr.Markdown()

    calculate_button = gr.Button("Calculate Solar System")

    calculate_button.click(
        fn=solar_calculator,
        inputs=[
            appliance,
            quantity,
            hours
        ],
        outputs=output
    )

demo.launch()
