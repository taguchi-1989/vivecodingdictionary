#!/usr/bin/env python3
"""Generate local abstract 2:1 ponchi base diagrams for ponchi-batch-001."""
from __future__ import annotations

import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

from ponchi_generate_batch_015_local import (
    FINAL_SIZE,
    blend,
    card,
    line_color,
    node,
    rr,
    arrow,
)


RAW_SIZE = (1774, 887)
OUT_DIR = Path("assets/ponchi/experiments/batches/ponchi-batch-001")
STRICT_PALETTES = [
    ((18, 62, 130), (63, 127, 209), (141, 183, 232), (214, 230, 250)),
    ((26, 26, 26), (107, 114, 128), (63, 127, 209), (234, 241, 251)),
    ((18, 62, 130), (107, 114, 128), (141, 183, 232), (247, 249, 252)),
    ((63, 127, 209), (18, 62, 130), (214, 230, 250), (107, 114, 128)),
]

ENTRIES = [
    ("A-1", "welcome"),
    ("A-2", "reading_flow"),
    ("A-3", "walking_map"),
    ("A-4", "experience_lanes"),
    ("A-5", "reader_levels"),
    ("A-6", "freshness"),
    ("A-7", "figure_types"),
    ("A-8", "symbols"),
    ("A-9", "index"),
    ("A-10", "updates"),
    ("A-11", "abbreviations"),
    ("B-1", "service_multi"),
    ("B-2", "service_docs"),
    ("B-3", "service_chat"),
    ("B-4", "service_editor"),
    ("B-5", "service_completion"),
    ("B-6", "service_agent"),
    ("B-7", "service_terminal"),
    ("B-8", "service_codex"),
    ("B-9", "service_ui"),
]


def clean_base(index: int):
    palette = STRICT_PALETTES[index % len(STRICT_PALETTES)]
    image = Image.new("RGB", RAW_SIZE, (255, 255, 255))
    draw = ImageDraw.Draw(image)
    for y in range(250, RAW_SIZE[1], 40):
        draw.line([(0, y), (RAW_SIZE[0], y)], fill=(247, 249, 252), width=1)
    for x in range(0, 1040, 40):
        draw.line([(x, 0), (x, RAW_SIZE[1])], fill=(234, 241, 251), width=1)
    return image, draw, palette


def mini_book(draw, x, y, w, h, color):
    rr(draw, (x, y, x + w, y + h), fill=blend(color, 0.86), outline=line_color(color), width=5)
    draw.line([(x + w // 2, y + 28), (x + w // 2, y + h - 28)], fill=line_color(color), width=5)
    for yy in [y + 60, y + 110, y + 160]:
        draw.line([(x + 35, yy), (x + w // 2 - 30, yy)], fill=line_color(color), width=7)
        draw.line([(x + w // 2 + 30, yy), (x + w - 35, yy)], fill=line_color(color), width=7)


def welcome(draw, p):
    mini_book(draw, 150, 300, 380, 300, p[0])
    node(draw, 700, 450, 72, p[2])
    for i, (x, y) in enumerate([(900, 270), (1120, 390), (900, 565), (610, 650)]):
        card(draw, x, y, 230, 105, p[i % 4], p[3])
        arrow(draw, (750, 450), (x, y + 52), line_color(p[i % 4]), 7)


def reading_flow(draw, p):
    xs = [125, 420, 715, 1010, 1305]
    for i, x in enumerate(xs):
        card(draw, x, 380, 220, 120, p[i % 4], p[(i + 1) % 4])
        node(draw, x + 110, 600, 30, p[(i + 2) % 4])
        if i:
            arrow(draw, (x - 70, 440), (x - 15, 440), line_color(p[i % 4]), 7)
    draw.arc((280, 230, 1340, 735), 25, 330, fill=line_color(p[3]), width=7)


def walking_map(draw, p):
    points = [(190, 655), (330, 515), (510, 590), (675, 430), (875, 490), (1060, 340), (1280, 515), (1500, 380)]
    draw.line(points, fill=line_color(p[3]), width=12, joint="curve")
    for i, point in enumerate(points):
        node(draw, point[0], point[1], 34, p[i % 4])
        if i % 2 == 0:
            card(draw, point[0] - 80, point[1] - 135, 160, 80, p[(i + 1) % 4], p[3])


def experience_lanes(draw, p):
    for i, y in enumerate([270, 400, 530, 660]):
        rr(draw, (160, y, 1480, y + 80), fill=blend(p[i % 4], 0.88), outline=line_color(p[i % 4]), width=4)
        for x in [290, 520, 750, 980, 1210]:
            node(draw, x, y + 40, 24, p[(i + x) % 4])
            if x > 290:
                arrow(draw, (x - 180, y + 40), (x - 30, y + 40), line_color(p[i % 4]), 5)


def reader_levels(draw, p):
    for i, (x, h) in enumerate([(250, 130), (560, 210), (900, 300), (1270, 385)]):
        rr(draw, (x, 720 - h, x + 240, 720), fill=blend(p[i % 4], 0.84), outline=line_color(p[i % 4]), width=6)
        card(draw, x + 35, 665 - h, 170, 80, p[(i + 1) % 4], p[3])
    arrow(draw, (210, 740), (1520, 300), line_color(p[3]), 8)


def freshness(draw, p):
    card(draw, 150, 430, 280, 130, p[0], p[3])
    for i, x in enumerate([580, 790, 1000]):
        node(draw, x, 500, 54, p[i + 1])
        arrow(draw, (x - 140, 500), (x - 65, 500), line_color(p[i]), 7)
    card(draw, 1195, 380, 330, 150, p[2], p[0])
    draw.arc((520, 245, 1270, 720), 35, 330, fill=line_color(p[3]), width=8)
    for x in [630, 850, 1070]:
        draw.line([(x, 300), (x + 55, 355)], fill=line_color(p[1]), width=8)


def figure_types(draw, p):
    positions = [(150, 300), (450, 300), (750, 300), (1050, 300), (1350, 300)]
    for i, (x, y) in enumerate(positions):
        rr(draw, (x, y, x + 220, y + 260), fill=blend(p[i % 4], 0.88), outline=line_color(p[i % 4]), width=5)
        if i == 0:
            arrow(draw, (x + 50, y + 130), (x + 170, y + 130), line_color(p[i % 4]), 5)
        elif i == 1:
            for yy in [y + 70, y + 130, y + 190]:
                draw.line([(x + 45, yy), (x + 175, yy)], fill=line_color(p[i % 4]), width=7)
        elif i == 2:
            for a in [(x + 60, y + 80), (x + 160, y + 90), (x + 105, y + 185)]:
                node(draw, a[0], a[1], 22, p[(i + 1) % 4])
            draw.line([(x + 60, y + 80), (x + 160, y + 90), (x + 105, y + 185), (x + 60, y + 80)], fill=line_color(p[i % 4]), width=5)
        elif i == 3:
            for xx in [x + 55, x + 110, x + 165]:
                node(draw, xx, y + 130, 24, p[(i + 1) % 4])
        else:
            card(draw, x + 45, y + 90, 130, 90, p[(i + 1) % 4], p[3])


def symbols(draw, p):
    for i, x in enumerate([180, 380, 580, 780, 980, 1180, 1380]):
        node(draw, x, 400, 42, p[i % 4])
        draw.rounded_rectangle((x - 55, 520, x + 55, 610), radius=18, fill=blend(p[i % 4], 0.82), outline=line_color(p[i % 4]), width=5)
    arrow(draw, (280, 700), (1460, 700), line_color(p[3]), 7)


def index_map(draw, p):
    for i, y in enumerate([250, 360, 470, 580, 690]):
        card(draw, 125, y, 230, 80, p[i % 4], p[3])
        arrow(draw, (365, y + 40), (720, 485), line_color(p[i % 4]), 5)
    rr(draw, (735, 330, 1020, 620), fill=blend(p[2], 0.8), outline=line_color(p[2]), width=6)
    for i, (x, y) in enumerate([(1190, 270), (1390, 390), (1190, 570), (980, 705)]):
        card(draw, x, y, 210, 90, p[(i + 1) % 4], p[0])
        arrow(draw, (1025, 485), (x, y + 45), line_color(p[(i + 1) % 4]), 5)


def updates(draw, p):
    for i, x in enumerate([160, 450, 740, 1030, 1320]):
        card(draw, x, 430, 220, 110, p[i % 4], p[(i + 1) % 4])
        if i:
            arrow(draw, (x - 70, 485), (x - 15, 485), line_color(p[i % 4]), 7)
    draw.arc((330, 245, 1320, 720), 30, 335, fill=line_color(p[3]), width=7)
    for x in [510, 830, 1150]:
        node(draw, x, 325, 28, p[(x // 100) % 4])


def abbreviations(draw, p):
    for i, y in enumerate([290, 430, 570]):
        card(draw, 180, y, 170, 85, p[i % 4], p[3])
        arrow(draw, (360, y + 43), (650, 465), line_color(p[i % 4]), 6)
    rr(draw, (660, 315, 960, 625), fill=blend(p[2], 0.85), outline=line_color(p[2]), width=6)
    for i, y in enumerate([285, 430, 575]):
        card(draw, 1150, y, 280, 95, p[(i + 1) % 4], p[0])
        arrow(draw, (965, 465), (1140, y + 47), line_color(p[(i + 1) % 4]), 6)


def service_scene(draw, p, variant):
    rr(draw, (150, 280, 560, 670), fill=blend(p[variant % 4], 0.86), outline=line_color(p[variant % 4]), width=6)
    for y in [350, 445, 540, 635]:
        draw.line([(235, y), (480, y)], fill=line_color(p[variant % 4]), width=9)
    node(draw, 785, 480, 80, p[(variant + 1) % 4])
    arrow(draw, (565, 480), (705, 480), line_color(p[3]), 8)
    motifs = [(1020, 330), (1280, 440), (1040, 610), (620, 710)]
    for i, (x, y) in enumerate(motifs):
        card(draw, x, y, 230, 95, p[(variant + i + 2) % 4], p[0])
        arrow(draw, (865, 480), (x, y + 48), line_color(p[(variant + i + 2) % 4]), 6)
    if variant in {3, 4, 6, 7}:
        for y in [330, 405, 480]:
            draw.line([(250, y), (465, y)], fill=line_color(p[(variant + 2) % 4]), width=6)
    if variant in {0, 2, 8}:
        rr(draw, (1090, 585, 1430, 735), fill=blend(p[2], 0.86), outline=line_color(p[2]), width=5)
    lower_context_rail(draw, p)


def _connector_cloud(draw, p, cx, cy):
    node(draw, cx, cy, 88, p[1])
    for angle in range(0, 360, 60):
        x = cx + int(math.cos(math.radians(angle)) * 118)
        y = cy + int(math.sin(math.radians(angle)) * 82)
        node(draw, x, y, 20, p[(angle // 60) % 4])
        draw.line([(cx, cy), (x, y)], fill=line_color(p[1]), width=5)


def lower_context_rail(draw, p):
    """Add meaningful lower workflow mass while keeping the logo clearspace blank."""
    y = 850
    xs = [160, 420, 680, 940, 1200, 1460]
    draw.line([(xs[0], y), (xs[-1], y)], fill=(141, 183, 232), width=6)
    for index, x in enumerate(xs):
        draw.ellipse((x - 24, y - 24, x + 24, y + 24), fill=(234, 241, 251), outline=(63, 127, 209), width=4)
        if index % 2 == 0:
            draw.rounded_rectangle(
                (x - 64, y - 92, x + 64, y - 48),
                radius=18,
                fill=(247, 249, 252),
                outline=(107, 114, 128),
                width=4,
            )


def service_chat_scene(draw, p):
    """Neutral chat-assistant loop with no product UI and a blank logo corner."""
    rr(draw, (110, 290, 465, 665), fill=blend(p[0], 0.88), outline=line_color(p[0]), width=6)
    for y in [360, 435, 510, 585]:
        draw.line([(175, y), (390, y)], fill=line_color(p[0]), width=8)
    node(draw, 505, 410, 36, p[3])
    arrow(draw, (470, 430), (635, 430), line_color(p[3]), 8)

    _connector_cloud(draw, p, 760, 430)
    for i, (x, y, w) in enumerate([(555, 655, 260), (835, 655, 260), (1120, 590, 290)]):
        card(draw, x, y, w, 110, p[(i + 1) % 4], p[0])
        for dx in [40, 92, 144]:
            node(draw, x + dx, y + 56, 16, p[(i + 2) % 4])
        arrow(draw, (760, 520), (x + 40, y + 20), line_color(p[(i + 1) % 4]), 5)

    rr(draw, (1010, 315, 1505, 500), fill=blend(p[2], 0.9), outline=line_color(p[2]), width=6)
    for x in [1085, 1195, 1305, 1415]:
        node(draw, x, 380, 22, p[(x // 100) % 4])
        draw.line([(x - 32, 430), (x + 32, 430)], fill=line_color(p[2]), width=6)
    arrow(draw, (865, 430), (1000, 405), line_color(p[2]), 8)
    lower_context_rail(draw, p)


def service_codex_scene(draw, p):
    """Generic coding-agent board; no readable code, product UI, or logo."""
    rr(draw, (110, 315, 395, 690), fill=blend(p[0], 0.88), outline=line_color(p[0]), width=6)
    for i, y in enumerate([380, 460, 540, 620]):
        card(draw, 155, y, 195, 48, p[(i + 1) % 4], p[3])

    rr(draw, (520, 250, 895, 695), fill=blend(p[1], 0.9), outline=line_color(p[1]), width=6)
    for i, y in enumerate([315, 420, 525, 630]):
        node(draw, 585, y, 26, p[(i + 2) % 4])
        draw.line([(635, y), (820, y)], fill=line_color(p[1]), width=7)
        if i:
            arrow(draw, (585, y - 70), (585, y - 35), line_color(p[1]), 5)

    node(draw, 1030, 475, 82, p[3])
    arrow(draw, (900, 475), (945, 475), line_color(p[3]), 8)

    for i, (x, y) in enumerate([(1165, 335), (1355, 455), (1165, 610)]):
        rr(draw, (x, y, x + 240, y + 95), fill=blend(p[(i + 2) % 4], 0.88), outline=line_color(p[(i + 2) % 4]), width=5)
        for xx in [x + 55, x + 120, x + 185]:
            node(draw, xx, y + 48, 15, p[(i + 1) % 4])
        arrow(draw, (1110, 475), (x, y + 48), line_color(p[(i + 2) % 4]), 5)
    lower_context_rail(draw, p)


DRAWERS = {
    "welcome": welcome,
    "reading_flow": reading_flow,
    "walking_map": walking_map,
    "experience_lanes": experience_lanes,
    "reader_levels": reader_levels,
    "freshness": freshness,
    "figure_types": figure_types,
    "symbols": symbols,
    "index": index_map,
    "updates": updates,
    "abbreviations": abbreviations,
    "service_chat": service_chat_scene,
    "service_codex": service_codex_scene,
}


def finish(image: Image.Image, entry_id: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    raw = image.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
    raw.save(OUT_DIR / f"{entry_id}_base_raw.png")
    final = raw.resize(FINAL_SIZE, Image.Resampling.LANCZOS)
    final.save(OUT_DIR / f"{entry_id}_base_1254x627.png")


def main() -> int:
    selected = set(sys.argv[1:])
    for index, (entry_id, variant) in enumerate(ENTRIES):
        if selected and entry_id not in selected:
            continue
        image, draw, palette = clean_base(index)
        if variant in DRAWERS:
            DRAWERS[variant](draw, palette)
        elif variant.startswith("service_"):
            service_scene(draw, palette, index - 11)
        else:
            DRAWERS[variant](draw, palette)
        finish(image, entry_id)
        print(f"wrote {entry_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
