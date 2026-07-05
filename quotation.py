from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()


def generate_quote(
    customer,
    daily_energy,
    panel,
    battery,
    inverter,
    total_cost
):
    filename = "SolarMate_Quotation.pdf"

    pdf = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>SolarMate AI</b>", styles["Title"]))

    story.append(Paragraph("Professional Solar Quotation", styles["Heading2"]))

    story.append(Paragraph(f"<b>Customer:</b> {customer}", styles["Normal"]))

    story.append(Paragraph(f"<b>Daily Energy:</b> {daily_energy:.0f} Wh/day", styles["Normal"]))

    story.append(Paragraph(f"<b>Solar Panels:</b> {panel}", styles["Normal"]))

    story.append(Paragraph(f"<b>Battery:</b> {battery}", styles["Normal"]))

    story.append(Paragraph(f"<b>Inverter:</b> {inverter}", styles["Normal"]))

    story.append(Paragraph(f"<b>Total Cost:</b> ₦{total_cost:,}", styles["Heading1"]))

    pdf.build(story)

    return filename
    