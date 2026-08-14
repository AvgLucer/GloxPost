import re

from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER


def create_safe_filename(title):
    """Create a clean filename from the original video title."""

    safe_title = re.sub(r'[<>:"/\\|?*]', '', title)
    safe_title = re.sub(r'\s+', '_', safe_title.strip())

    # Keep filenames manageable
    safe_title = safe_title[:80].rstrip('_')

    if not safe_title:
        safe_title = "glox_content_report"

    return safe_title


def format_output(
    title,
    context,
    analysis,
    generated,
    evaluation
):

    # ========================================
    # DETERMINE WINNER
    # ========================================

    if evaluation["winner"] == "title_1":
        recommended = generated["titles"][0]
        winner_data = evaluation["title_1"]
    else:
        recommended = generated["titles"][1]
        winner_data = evaluation["title_2"]


    # ========================================
    # CREATE FILENAMES
    # ========================================

    safe_title = create_safe_filename(title)

    txt_filename = f"{safe_title}.txt"
    pdf_filename = f"{safe_title}.pdf"


    # ========================================
    # PREPARE TEXT
    # ========================================

    curiosity_text = "\n".join(
        f"- {item}"
        for item in analysis["curiosity_opportunities"]
    )

    weaknesses_text = "\n".join(
        f"- {item}"
        for item in analysis["title_weaknesses"]
    )


    # ========================================
    # TEXT REPORT
    # ========================================

    report = f"""
========================================
        GLOX CONTENT AGENT REPORT
========================================

1. ORIGINAL INPUT
----------------------------------------

Original YouTube Title:
{title}

Context:
{context}


2. CONTENT ANALYSIS
----------------------------------------

Main Topic:
{analysis["main_topic"]}

Target Audience:
{analysis["target_audience"]}

Content Category:
{analysis["content_category"]}

Viewer Value:
{analysis["viewer_value"]}

Main Hook:
{analysis["main_hook"]}

Keywords:
{", ".join(analysis["keywords"])}

Tone:
{analysis["tone"]}

Curiosity Opportunities:
{curiosity_text}

Title Weaknesses:
{weaknesses_text}


3. GENERATED YOUTUBE TITLES
----------------------------------------

Title 1:
{generated["titles"][0]}

Title 2:
{generated["titles"][1]}


4. TITLE PERFORMANCE ANALYSIS
----------------------------------------

TITLE 1

Hook Strength:
{evaluation["title_1"]["hook"]}/100

Curiosity:
{evaluation["title_1"]["curiosity"]}/100

Clarity:
{evaluation["title_1"]["clarity"]}/100

Audience Appeal:
{evaluation["title_1"]["audience_appeal"]}/100

Search Potential:
{evaluation["title_1"]["search_potential"]}/100

Overall:
{evaluation["title_1"]["overall"]}/100

Reason:
{evaluation["title_1"]["reason"]}


TITLE 2

Hook Strength:
{evaluation["title_2"]["hook"]}/100

Curiosity:
{evaluation["title_2"]["curiosity"]}/100

Clarity:
{evaluation["title_2"]["clarity"]}/100

Audience Appeal:
{evaluation["title_2"]["audience_appeal"]}/100

Search Potential:
{evaluation["title_2"]["search_potential"]}/100

Overall:
{evaluation["title_2"]["overall"]}/100

Reason:
{evaluation["title_2"]["reason"]}


5. RECOMMENDED TITLE
----------------------------------------

{recommended}

Content Potential:
{winner_data["overall"]}/100

Why It Won:
{evaluation["winner_reason"]}


6. YOUTUBE DESCRIPTIONS
----------------------------------------

DESCRIPTION 1

{generated["descriptions"][0]}


DESCRIPTION 2

{generated["descriptions"][1]}


7. INSTAGRAM CAPTIONS
----------------------------------------

CAPTION 1

{generated["captions"][0]}


CAPTION 2

{generated["captions"][1]}


========================================
          END OF GLOX REPORT
========================================
"""


    # ========================================
    # SAVE TXT
    # ========================================

    with open(txt_filename, "w", encoding="utf-8") as file:
        file.write(report)


    # ========================================
    # CREATE PDF
    # ========================================

    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=A4,
        rightMargin=45,
        leftMargin=45,
        topMargin=45,
        bottomMargin=45
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER

    heading_style = styles["Heading2"]
    body_style = styles["BodyText"]

    story = []

    def add_heading(text):
        story.append(Spacer(1, 10))
        story.append(Paragraph(text, heading_style))
        story.append(Spacer(1, 5))

    def add_text(label, text):
        safe_text = str(text).replace("&", "&amp;")
        safe_text = safe_text.replace("<", "&lt;")
        safe_text = safe_text.replace(">", "&gt;")
        safe_text = safe_text.replace("\n", "<br/>")

        story.append(
            Paragraph(
                f"<b>{label}</b> {safe_text}",
                body_style
            )
        )

        story.append(Spacer(1, 5))


    # ========================================
    # PDF CONTENT
    # ========================================

    story.append(
        Paragraph(
            "GLOX CONTENT AGENT REPORT",
            title_style
        )
    )

    story.append(Spacer(1, 20))


    # Original Input
    add_heading("1. Original Input")

    add_text(
        "Original YouTube Title:",
        title
    )

    add_text(
        "Context:",
        context
    )


    # Analysis
    add_heading("2. Content Analysis")

    add_text(
        "Main Topic:",
        analysis["main_topic"]
    )

    add_text(
        "Target Audience:",
        analysis["target_audience"]
    )

    add_text(
        "Content Category:",
        analysis["content_category"]
    )

    add_text(
        "Viewer Value:",
        analysis["viewer_value"]
    )

    add_text(
        "Main Hook:",
        analysis["main_hook"]
    )

    add_text(
        "Keywords:",
        ", ".join(analysis["keywords"])
    )

    add_text(
        "Tone:",
        analysis["tone"]
    )

    add_text(
        "Curiosity Opportunities:",
        "<br/>".join(
            f"• {item}"
            for item in analysis["curiosity_opportunities"]
        )
    )

    add_text(
        "Title Weaknesses:",
        "<br/>".join(
            f"• {item}"
            for item in analysis["title_weaknesses"]
        )
    )


    # Generated Titles
    add_heading("3. Generated YouTube Titles")

    add_text(
        "Title 1:",
        generated["titles"][0]
    )

    add_text(
        "Title 2:",
        generated["titles"][1]
    )


    # Evaluation
    add_heading("4. Title Performance Analysis")

    for number in ["title_1", "title_2"]:

        data = evaluation[number]

        current_title = (
            generated["titles"][0]
            if number == "title_1"
            else generated["titles"][1]
        )

        add_text(
            "Title:",
            current_title
        )

        add_text(
            "Hook Strength:",
            f'{data["hook"]}/100'
        )

        add_text(
            "Curiosity:",
            f'{data["curiosity"]}/100'
        )

        add_text(
            "Clarity:",
            f'{data["clarity"]}/100'
        )

        add_text(
            "Audience Appeal:",
            f'{data["audience_appeal"]}/100'
        )

        add_text(
            "Search Potential:",
            f'{data["search_potential"]}/100'
        )

        add_text(
            "Overall:",
            f'{data["overall"]}/100'
        )

        add_text(
            "Reason:",
            data["reason"]
        )


    # Winner
    add_heading("5. Recommended Title")

    add_text(
        "Recommended Title:",
        recommended
    )

    add_text(
        "Content Potential:",
        f'{winner_data["overall"]}/100'
    )

    add_text(
        "Why It Won:",
        evaluation["winner_reason"]
    )


    # YouTube Descriptions
    add_heading("6. YouTube Descriptions")

    add_text(
        "Description 1:",
        generated["descriptions"][0]
    )

    add_text(
        "Description 2:",
        generated["descriptions"][1]
    )


    # Instagram Captions
    add_heading("7. Instagram Captions")

    add_text(
        "Caption 1:",
        generated["captions"][0]
    )

    add_text(
        "Caption 2:",
        generated["captions"][1]
    )


    # Build PDF
    doc.build(story)


    # ========================================
    # DONE
    # ========================================

    print("\n========================================")
    print("       GLOX REPORTS GENERATED")
    print("========================================")
    print(f"\nTXT: {txt_filename}")
    print(f"PDF: {pdf_filename}\n")

    return report