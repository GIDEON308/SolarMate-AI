import gradio as gr
from calculator import calculate_system
from appliances import APPLIANCES


def solar_calculator(
    led_qty, led_hours,
    fan_qty, fan_hours,
    tv_qty, tv_hours,
    fridge_qty, fridge_hours,
    laptop_qty, laptop_hours
):

    daily_energy = (
        led_qty * APPLIANCES["LED Bulb"] * led_hours +
        fan_qty * APPLIANCES["Standing Fan"] * fan_hours +
        tv_qty * APPLIANCES['LED TV 32"'] * tv_hours +
        fridge_qty * APPLIANCES["Refrigerator"] * fridge_hours +
        laptop_qty * APPLIANCES["Laptop"] * laptop_hours
    )

    result = calculate_system(
        daily_energy,
        5,
        24,
        1
    )

    return f"""
# ☀️ SolarMate AI Version 3

## Appliance Load Summary

**Daily Energy:** {daily_energy:.0f} Wh/day

---

### Recommended Solar System

☀️ Solar Panel: **{result['panel']} W**

🔋 Battery: **{result['battery']} Ah**

⚡ Inverter: **{result['inverter']} W**
"""


with gr.Blocks(title="SolarMate AI") as demo:

    gr.Markdown("# ☀️ SolarMate AI")
    gr.Markdown("### Smart Solar PV Sizing Assistant")

    with gr.Row():

        with gr.Column():

            led_qty = gr.Number(label="LED Bulbs (Qty)", value=0)
            led_hours = gr.Number(label="LED Bulbs (Hours)", value=0)

            fan_qty = gr.Number(label="Standing Fans (Qty)", value=0)
            fan_hours = gr.Number(label="Standing Fans (Hours)", value=0)

            tv_qty = gr.Number(label='32" LED TV (Qty)', value=0)
            tv_hours = gr.Number(label='32" LED TV (Hours)', value=0)

            fridge_qty = gr.Number(label="Refrigerator (Qty)", value=0)
            fridge_hours = gr.Number(label="Refrigerator (Hours)", value=0)

            laptop_qty = gr.Number(label="Laptop (Qty)", value=0)
            laptop_hours = gr.Number(label="Laptop (Hours)", value=0)

            calculate_btn = gr.Button("Calculate Solar System")

        with gr.Column():

            output = gr.Markdown()

    calculate_btn.click(
        fn=solar_calculator,
        inputs=[
            led_qty, led_hours,
            fan_qty, fan_hours,
            tv_qty, tv_hours,
            fridge_qty, fridge_hours,
            laptop_qty, laptop_hours
        ],
        outputs=output
    )

demo.launch()
