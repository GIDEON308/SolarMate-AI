import gradio as gr

from appliances import APPLIANCES
from calculator import calculate_system
from equipment import (
    recommend_panel,
    recommend_battery,
    recommend_inverter
)

from load_builder import (
    add_appliance,
    get_load_schedule,
    total_daily_energy,
    clear_load_schedule
)


def add_to_schedule(appliance, quantity, hours):



    power = APPLIANCES[appliance]

    add_appliance(
        appliance,
        power,
        quantity,
        hours
    )

    schedule = get_load_schedule()

    table_data = []

    for item in schedule:
        table_data.append([
            item["name"],
            item["power"],
            item["quantity"],
            item["hours"],
            item["energy"]
        ])

    

    return table_data


def calculate_total_system():

    daily_energy = total_daily_energy()

    if daily_energy == 0:
        return "# ⚠️ No appliances have been added."

    result = calculate_system(
        daily_energy,
        5,
        24,
        1
    )
    panel = recommend_panel(result["panel"])
    battery = recommend_battery(result["battery"])
    inverter = recommend_inverter(result["inverter"])

    return f"""
# ☀️ SolarMate AI Version 6

## Total Daily Energy

**{daily_energy:.0f} Wh/day**

---

## Recommended Solar Equipment
☀️ Solar Panels

**{panel}**

🔋 Battery Bank

**{battery}**

⚡ Inverter

**{inverter}**
"""


def clear_schedule():

    clear_load_schedule()

    return "# 📋 Load Schedule Cleared."


with gr.Blocks(title="SolarMate AI Version 6") as demo:

    gr.Markdown("# ☀️ SolarMate AI")
    gr.Markdown("## Professional Load Builder")

    appliance = gr.Dropdown(
        choices=sorted(APPLIANCES.keys()),
        label="Select Appliance",
        value="LED Bulb"
    )

    quantity = gr.Number(label="Quantity", value=1)
    hours = gr.Number(label="Hours per Day", value=5)

    with gr.Row():
        add_btn = gr.Button("➕ Add Appliance")
        calculate_btn = gr.Button("☀️ Calculate System")
        clear_btn = gr.Button("🗑️ Clear Schedule")

    schedule_table = gr.Dataframe(
        headers=["Appliance", "Power (W)", "Quantity", "Hours", "Energy (Wh/day)"],
        datatype=["str", "number", "number", "number", "number"],
        value=[],
        interactive=False
    )

    output = gr.Markdown()

    add_btn.click(
        fn=add_to_schedule,
        inputs=[appliance, quantity, hours],
        outputs=schedule_table
    )

    calculate_btn.click(
        fn=calculate_total_system,
        outputs=output
    )

    clear_btn.click(
        fn=clear_schedule,
        outputs=output
    )

demo.launch()