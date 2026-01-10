import argparse
import json
import sys
from pathlib import Path


def load_profile(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    first = str(data.get("first_name", "")).strip()
    last = str(data.get("last_name", "")).strip()
    if not first or not last:
        raise ValueError("first_name and last_name are required in profile")
    if first.upper() == "FIRST" or last.upper() == "LAST":
        raise ValueError("Replace FIRST/LAST placeholders in certificate/profile.json")
    return first, last


def draw_certificate(output_path, full_name, username, date_text):
    try:
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import landscape, letter
        from reportlab.lib.units import inch
        from reportlab.pdfgen import canvas
    except ImportError as exc:
        raise RuntimeError(
            "Missing reportlab. Install with: python -m pip install reportlab"
        ) from exc

    width, height = landscape(letter)
    c = canvas.Canvas(str(output_path), pagesize=landscape(letter))

    margin = 0.6 * inch
    c.setStrokeColor(colors.HexColor("#2E4057"))
    c.setLineWidth(2)
    c.rect(margin, margin, width - 2 * margin, height - 2 * margin)

    c.setFont("Helvetica-Bold", 32)
    c.drawCentredString(width / 2, height - 1.6 * inch, "Certificate of Completion")

    c.setFont("Helvetica", 16)
    c.drawCentredString(width / 2, height - 2.2 * inch, "GitHub Basics Bootcamp")

    c.setFont("Helvetica", 14)
    c.drawCentredString(width / 2, height / 2 + 0.8 * inch, "This certifies that")

    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(width / 2, height / 2 + 0.2 * inch, full_name)

    c.setFont("Helvetica", 14)
    c.drawCentredString(width / 2, height / 2 - 0.3 * inch, f"GitHub: @{username}")

    c.setFont("Helvetica", 12)
    c.drawCentredString(width / 2, margin + 0.6 * inch, f"Date: {date_text}")

    c.showPage()
    c.save()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", default="certificate/profile.json")
    parser.add_argument("--username", required=True)
    parser.add_argument("--date", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    first, last = load_profile(args.profile)
    full_name = f"{first} {last}".strip()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        draw_certificate(output_path, full_name, args.username, args.date)
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
