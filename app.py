import gradio as gr
from calculator import calculate_system
from appliances import APPLIANCES

print("Step 1: All modules imported successfully")


def solar_calculator(
    led_qty, led_hours,
    fan_qty, fan_hours,
    tv_qty, tv_hours,
    fridge_qty, fridge_hours,
    laptop_qty, laptop_hours
):
    # Calculate daily energy consumption
    daily_energy = (
        led_qty * APPLIANCES["LED Bulb"] * led_hours +
        fan_qty * APPLIANCES["Standing Fan"] * fan_hours +
        tv_qty * APPLIANCES['LED TV 32"'] * tv_hours +
        fridge_qty * APPLIANCES["Refrigerator"] * fridge_hours +
        laptop_qty * APPLIANCES["Laptop"] * laptop_hours
    )

    # Calculate solar system size
    result = calculate_system(
        daily_energy,
        5,   # Peak Sun Hours
        24,  # Battery Voltage
        1    # Backup Days
    )

    return f"""
# ☀️ SolarMate AI Version 2

## Appliance Load Summary

**Daily Energy Consumption:** {daily_energy:.0f} Wh/day

## Recommended Solar System

☀️ Solar Panel Size: **{result['panel']} W**

🔋 Battery Capacity: **{result['battery']} Ah**

⚡ Inverter Size: **{result['inverter']} W**
"""


print("Step 2: Creating Gradio Interface...")

demo = gr.Interface(
    fn=solar_calculator,
    inputs=[
        gr.Number(label="LED Bulbs (Quantity)", value=0),
        gr.Number(label="LED Bulbs (Hours per Day)", value=0),

        gr.Number(label="Standing Fans (Quantity)", value=0),
        gr.Number(label="Standing Fans (Hours per Day)", value=0),

        gr.Number(label='32" LED TV (Quantity)', value=0),
        gr.Number(label='32" LED TV (Hours per Day)', value=0),

        gr.Number(label="Refrigerator (Quantity)", value=0),
        gr.Number(label="Refrigerator (Hours per Day)", value=0),

        gr.Number(label="Laptop (Quantity)", value=0),
        gr.Number(label="Laptop (Hours per Day)", value=0),
    ],
    outputs="markdown",
    title="☀️ SolarMate AI Version 2",
    description="Smart Appliance-Based Solar System Calculator",
)

print("Step 3: Launching Gradio...")

demo.launch()