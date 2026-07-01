print("Step 1: Starting app")

import gradio as gr
print("Step 2: Gradio imported")

from calculator import calculate_system
print("Step 3: Calculator imported")

def solar_calculator(daily_energy, sun_hours, battery_voltage, backup_days):
    result = calculate_system(
        daily_energy,
        sun_hours,
        battery_voltage,
        backup_days
    )

    return f"""
# SolarMate AI

Solar Panel: {result['panel']} W

Battery: {result['battery']} Ah

Inverter: {result['inverter']} W
"""

print("Step 4: Creating interface")

demo = gr.Interface(
    fn=solar_calculator,
    inputs=[
        gr.Number(label="Daily Energy"),
        gr.Number(label="Sun Hours"),
        gr.Number(label="Battery Voltage"),
        gr.Number(label="Backup Days"),
    ],
    outputs="markdown",
)

print("Step 5: Launching")

demo.launch()


