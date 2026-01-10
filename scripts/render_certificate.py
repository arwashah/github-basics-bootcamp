import argparse
import datetime as dt
import json
import os
import re
import subprocess
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

    # Background with subtle vertical gradient
    base_color = colors.HexColor("#F8F9FA")
    c.setFillColor(base_color)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    gradient_steps = 24
    for i in range(gradient_steps):
        shade = 248 - int(i * (12 / gradient_steps))
        c.setFillColor(colors.Color(shade / 255, shade / 255, 250 / 255))
        y = (height / gradient_steps) * i
        c.rect(0, y, width, height / gradient_steps, fill=1, stroke=0)
    
    # Decorative corner elements
    corner_size = 0.8 * inch
    accent_color = colors.HexColor("#FF9500")  # AWS Orange
    primary_color = colors.HexColor("#232F3E")  # AWS Dark Blue
    
    # Top-left corner
    c.setFillColor(accent_color)
    c.setStrokeColor(accent_color)
    c.setLineWidth(3)
    c.line(0.5 * inch, height - 0.5 * inch, 0.5 * inch + corner_size, height - 0.5 * inch)
    c.line(0.5 * inch, height - 0.5 * inch, 0.5 * inch, height - 0.5 * inch - corner_size)
    
    # Top-right corner
    c.line(width - 0.5 * inch, height - 0.5 * inch, width - 0.5 * inch - corner_size, height - 0.5 * inch)
    c.line(width - 0.5 * inch, height - 0.5 * inch, width - 0.5 * inch, height - 0.5 * inch - corner_size)
    
    # Bottom-left corner
    c.line(0.5 * inch, 0.5 * inch, 0.5 * inch + corner_size, 0.5 * inch)
    c.line(0.5 * inch, 0.5 * inch, 0.5 * inch, 0.5 * inch + corner_size)
    
    # Bottom-right corner
    c.line(width - 0.5 * inch, 0.5 * inch, width - 0.5 * inch - corner_size, 0.5 * inch)
    c.line(width - 0.5 * inch, 0.5 * inch, width - 0.5 * inch, 0.5 * inch + corner_size)

    # Double border with gradient effect
    margin = 0.7 * inch
    c.setStrokeColor(primary_color)
    c.setLineWidth(4)
    c.rect(margin, margin, width - 2 * margin, height - 2 * margin)
    
    c.setStrokeColor(accent_color)
    c.setLineWidth(1.5)
    c.rect(margin + 0.15 * inch, margin + 0.15 * inch, 
           width - 2 * margin - 0.3 * inch, height - 2 * margin - 0.3 * inch)

    # Title block
    content_shift = -0.2 * inch
    ribbon_y = height - 1.55 * inch + content_shift
    c.setFillColor(primary_color)
    c.setFont("Helvetica-Bold", 40)
    c.drawCentredString(width / 2, ribbon_y + 0.15 * inch, "CERTIFICATE")
    c.setFillColor(colors.HexColor("#6E7681"))
    c.setFont("Helvetica", 18)
    c.drawCentredString(width / 2, ribbon_y - 0.2 * inch, "OF COMPLETION")

    # Subtitle with accent color
    c.setFillColor(accent_color)
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(
        width / 2, height - 2.85 * inch + content_shift, "GitHub Basics Bootcamp"
    )
    
    # Decorative line under subtitle
    c.setStrokeColor(accent_color)
    c.setLineWidth(2)
    line_width = 3 * inch
    c.line(width / 2 - line_width / 2, height - 2.75 * inch, 
           width / 2 + line_width / 2, height - 2.75 * inch)

    # "This certifies that" text
    c.setFillColor(primary_color)
    c.setFont("Helvetica-Oblique", 16)
    c.drawCentredString(
        width / 2, height / 2 + 0.85 * inch + content_shift, "This is to certify that"
    )

    # Name with decorative underline
    c.setFont("Helvetica-Bold", 36)
    c.setFillColor(primary_color)
    c.drawCentredString(width / 2, height / 2 + 0.15 * inch + content_shift, full_name)
    
    # Decorative line under name
    c.setStrokeColor(accent_color)
    c.setLineWidth(1.5)
    name_line_width = 5 * inch
    c.line(
        width / 2 - name_line_width / 2,
        height / 2 - 0.05 * inch + content_shift,
        width / 2 + name_line_width / 2,
        height / 2 - 0.05 * inch + content_shift,
    )

    # GitHub username with icon-like styling
    c.setFillColor(colors.HexColor("#6E7681"))
    c.setFont("Helvetica", 16)
    c.drawCentredString(width / 2, height / 2 - 0.6 * inch + content_shift, f"@{username}")

    # Achievement text
    c.setFillColor(primary_color)
    c.setFont("Helvetica", 14)
    c.drawCentredString(
        width / 2,
        height / 2 - 1.05 * inch + content_shift,
        "has successfully completed all requirements of the",
    )
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(
        width / 2, height / 2 - 1.3 * inch + content_shift, "GitHub Basics Bootcamp"
    )
    c.setFont("Helvetica", 14)
    c.drawCentredString(
        width / 2,
        height / 2 - 1.55 * inch + content_shift,
        "demonstrating proficiency in version control, collaboration,",
    )
    c.drawCentredString(
        width / 2,
        height / 2 - 1.8 * inch + content_shift,
        "and GitHub workflows",
    )

    # AWS Cloud Club branding
    c.setFillColor(accent_color)
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(width / 2, margin + 1.2 * inch, "AWS CLOUD CLUB")
    
    # Date with decorative styling
    c.setFillColor(primary_color)
    c.setFont("Helvetica", 11)
    c.drawCentredString(width / 2, margin + 0.90 * inch, f"Issued on {date_text}")
    
    # Small decorative elements around date
    c.setStrokeColor(accent_color)
    c.setLineWidth(1)
    c.line(width / 2 - 2 * inch, margin + 0.95 * inch,
           width / 2 - 0.85 * inch, margin + 0.95 * inch)
    c.line(width / 2 + 0.85 * inch, margin + 0.95 * inch,
           width / 2 + 2 * inch, margin + 0.95 * inch)

    # Seal mark
    seal_x = width - margin - 1.0 * inch
    seal_y = margin + 1.0 * inch
    c.setStrokeColor(accent_color)
    c.setLineWidth(2)
    c.circle(seal_x, seal_y, 0.55 * inch, stroke=1, fill=0)
    c.setStrokeColor(colors.HexColor("#FFD8B2"))
    c.setLineWidth(1.5)
    c.circle(seal_x, seal_y, 0.42 * inch, stroke=1, fill=0)
    c.setFillColor(primary_color)
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(seal_x, seal_y + 0.12 * inch, "AWS")
    c.setFont("Helvetica", 7)
    c.drawCentredString(seal_x, seal_y - 0.02 * inch, "CLOUD CLUB")

    c.showPage()
    c.save()


def run_git(args):
    try:
        result = subprocess.run(
            ["git", *args],
            check=True,
            capture_output=True,
            text=True,
        )
    except (subprocess.SubprocessError, FileNotFoundError):
        return None
    return result.stdout.strip()


def detect_username():
    env_owner = os.environ.get("GITHUB_REPOSITORY_OWNER")
    if env_owner:
        return env_owner.strip()

    env_actor = os.environ.get("GITHUB_ACTOR")
    if env_actor:
        return env_actor.strip()

    env_repo = os.environ.get("GITHUB_REPOSITORY")
    if env_repo and "/" in env_repo:
        return env_repo.split("/", 1)[0].strip()

    remote_url = run_git(["remote", "get-url", "origin"])
    if remote_url:
        match = re.search(r"[:/](?P<owner>[^/]+)/[^/]+(?:\\.git)?$", remote_url)
        if match:
            return match.group("owner").strip()

    return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", default="certificate/profile.json")
    parser.add_argument("--username")
    parser.add_argument("--date")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    first, last = load_profile(args.profile)
    full_name = f"{first} {last}".strip()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        username = args.username or detect_username()
        if not username:
            raise ValueError(
                "Unable to detect GitHub username. Pass --username or set GITHUB_ACTOR."
            )

        date_text = args.date or dt.date.today().isoformat()
        draw_certificate(output_path, full_name, username, date_text)
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
