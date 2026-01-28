from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)
from reportlab.lib import colors
from datetime import datetime


def generate_pdf(results, output_file):
    doc = SimpleDocTemplate(
        output_file,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    story = []

    # ───────────────── COVER PAGE ─────────────────
    story.append(Paragraph("<b>ASTRAEUS</b>", styles["Title"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("AI-Driven Penetration Testing Report", styles["Heading2"]))
    story.append(Spacer(1, 24))
    story.append(Paragraph(f"Generated on: {datetime.now()}", styles["Normal"]))
    story.append(PageBreak())

    # ─────────────── EXECUTIVE SUMMARY ─────────────
    story.append(Paragraph("Executive Summary", styles["Heading1"]))
    story.append(Spacer(1, 12))

    critical = len([r for r in results if r["severity"] == "CRITICAL"])
    high = len([r for r in results if r["severity"] == "HIGH"])
    medium = len([r for r in results if r["severity"] == "MEDIUM"])
    low = len([r for r in results if r["severity"] == "LOW"])

    summary_text = f"""
    The penetration test identified <b>{len(results)}</b> security findings.
    <br/>Critical: {critical}
    <br/>High: {high}
    <br/>Medium: {medium}
    <br/>Low: {low}
    """

    story.append(Paragraph(summary_text, styles["Normal"]))
    story.append(PageBreak())

    # ─────────────── RISK SUMMARY TABLE ─────────────
    story.append(Paragraph("Risk Summary", styles["Heading1"]))
    story.append(Spacer(1, 12))

    table_data = [["Severity", "Count"]]
    table_data += [
        ["Critical", critical],
        ["High", high],
        ["Medium", medium],
        ["Low", low],
    ]

    table = Table(table_data, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 1), (-1, 1), colors.red),
        ("BACKGROUND", (0, 2), (-1, 2), colors.orange),
        ("BACKGROUND", (0, 3), (-1, 3), colors.yellow),
        ("BACKGROUND", (0, 4), (-1, 4), colors.lightgrey),
    ]))

    story.append(table)
    story.append(PageBreak())

    # ─────────────── DETAILED FINDINGS ──────────────
    story.append(Paragraph("Detailed Findings", styles["Heading1"]))
    story.append(Spacer(1, 12))

    for idx, r in enumerate(results, 1):
        story.append(Paragraph(f"<b>{idx}. {r['title']}</b>", styles["Heading2"]))
        story.append(Spacer(1, 6))

        story.append(Paragraph(f"<b>Endpoint:</b> {r.get('endpoint','N/A')}", styles["Normal"]))
        story.append(Paragraph(f"<b>Severity:</b> {r['severity']}", styles["Normal"]))
        story.append(Paragraph(f"<b>Exploitability Score:</b> {r['exploitability_score']}/10", styles["Normal"]))

        if r.get("attack_chain"):
            story.append(Paragraph(f"<b>Attack Chain:</b> {r['attack_chain']}", styles["Normal"]))

        story.append(Paragraph(f"<b>OWASP:</b> {r.get('owasp','')}", styles["Normal"]))
        story.append(Paragraph(f"<b>MITRE:</b> {', '.join(r.get('mitre',[]))}", styles["Normal"]))

        story.append(Spacer(1, 6))
        story.append(Paragraph("<b>Manual Exploitation Steps:</b>", styles["Normal"]))

        for step in r.get("manual_exploitation", []):
            story.append(Paragraph(f"- {step}", styles["Normal"]))

        story.append(Spacer(1, 6))
        story.append(Paragraph(f"<b>Remediation:</b> {r.get('remediation','')}", styles["Normal"]))
        story.append(Spacer(1, 18))

    doc.build(story)
