import gradio as gr

from appliances import APPLIANCES
from calculator import calculate_system

from equipment import (
    recommend_panel,
    recommend_battery,
    recommend_inverter
)

from pricing import estimate_cost
from quotation import generate_quote

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


def clear_schedule():

    clear_load_schedule()

    return "# 📋 Load Schedule Cleared."


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

    cost = estimate_cost(
        panel,
        battery,
        inverter
    )

    panel_cost = cost["panel_cost"]
    battery_cost = cost["battery_cost"]
    inverter_cost = cost["inverter_cost"]
    total_cost = cost["total"]

    return f"""
# ☀️ SolarMate AI Version 9

## Total Daily Energy

**{daily_energy:.0f} Wh/day**

---

## Recommended Solar Equipment

### ☀️ Solar Panels

**{panel}**

Price: **₦{panel_cost:,}**

### 🔋 Battery Bank

**{battery}**

Price: **₦{battery_cost:,}**

### ⚡ Inverter

**{inverter}**

Price: **₦{inverter_cost:,}**

### 🔧 Installation Materials

Price: **₦80,000**

---

# 💰 Estimated Project Cost

## ₦{total_cost:,}
"""


def create_pdf(customer_name):

    daily_energy = total_daily_energy()

    if daily_energy == 0:
        return None

    result = calculate_system(
        daily_energy,
        5,
        24,
        1
    )

    panel = recommend_panel(result["panel"])
    battery = recommend_battery(result["battery"])
    inverter = recommend_inverter(result["inverter"])

    cost = estimate_cost(
        panel,
        battery,
        inverter
    )

    filename = generate_quote(
        customer_name,
        daily_energy,
        panel,
        battery,
        inverter,
        cost["total"]
    )

    return filename
with gr.Blocks(title="SolarMate AI Version 9") as demo:

    gr.Markdown("# ☀️ SolarMate AI")
    gr.Markdown("## Professional Load Builder & Cost Estimator")

    customer = gr.Textbox(
        label="Customer Name",
        placeholder="Enter customer name"
    )

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

    with gr.Row():
        add_btn = gr.Button("➕ Add Appliance")
        calculate_btn = gr.Button("☀️ Calculate System")
        pdf_btn = gr.Button("📄 Generate PDF")
        clear_btn = gr.Button("🗑️ Clear Schedule")

    schedule_table = gr.Dataframe(
        headers=[
            "Appliance",
            "Power (W)",
            "Quantity",
            "Hours",
            "Energy (Wh/day)"
        ],
        datatype=[
            "str",
            "number",
            "number",
            "number",
            "number"
        ],
        value=[],
        interactive=False
    )

    output = gr.Markdown()

    pdf_output = gr.File(
        label="Download Solar Quotation"
    )
    add_btn.click(
        fn=add_to_schedule,
        inputs=[
            appliance,
            quantity,
            hours
        ],
        outputs=schedule_table
    )

    calculate_btn.click(
        fn=calculate_total_system,
        outputs=output
    )

    pdf_btn.click(
        fn=create_pdf,
        inputs=customer,
        outputs=pdf_output
    )

    clear_btn.click(
        fn=clear_schedule,
        outputs=output
    )

demo.launch()