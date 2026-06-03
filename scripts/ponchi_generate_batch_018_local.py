#!/usr/bin/env python3
"""Generate local abstract 2:1 ponchi base diagrams for ponchi-batch-018."""
from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageFilter

from ponchi_generate_batch_015_local import (
    FINAL_SIZE,
    base,
    blend,
    card,
    line_color,
    node,
    rr,
    small_lines,
    arrow,
)


OUT_DIR = Path("assets/ponchi/experiments/batches/ponchi-batch-018")

ENTRIES = [
    ("J-77", "gpu"),
    ("J-78", "hdd"),
    ("J-79", "ssd"),
    ("J-80", "sata"),
    ("J-81", "m2"),
    ("J-90", "gui"),
    ("J-91", "cli"),
    ("J-92", "linux"),
    ("J-93", "ubuntu"),
    ("J-100", "literacy"),
]


def gpu(draw, p):
    rr(draw, (230, 210, 1470, 660), fill=blend(p[0], 0.86), outline=line_color(p[0]), width=7)
    for x in [360, 590, 820, 1050, 1280]:
        rr(draw, (x, 310, x + 140, 130 + 330), fill=blend(p[(x // 100) % 4], 0.7), outline=line_color(p[(x // 100) % 4]), width=5)
        for y in [360, 430, 500]:
            draw.line([(x + 30, y), (x + 110, y)], fill=line_color(p[(x // 100) % 4]), width=7)
    for y, c in zip([250, 440, 630], p[1:]):
        card(draw, 85, y - 45, 210, 90, c, p[0])
        arrow(draw, (300, y), (355, 410), line_color(c), 6)


def hdd(draw, p):
    rr(draw, (300, 145, 1420, 730), fill=blend(p[1], 0.88), outline=line_color(p[1]), width=7)
    for r, c in [(245, p[0]), (175, p[2]), (105, p[3])]:
        draw.ellipse((860 - r, 440 - r, 860 + r, 440 + r), outline=line_color(c), width=10)
    node(draw, 860, 440, 34, p[3])
    draw.line([(1140, 245), (900, 430)], fill=line_color(p[1]), width=16)
    node(draw, 1140, 245, 45, p[1])
    for y, c in zip([255, 440, 625], p):
        card(draw, 135, y - 45, 210, 90, c, p[1])
        arrow(draw, (350, y), (590, 440), line_color(c), 6)


def ssd(draw, p):
    rr(draw, (235, 210, 1455, 665), fill=blend(p[2], 0.86), outline=line_color(p[2]), width=7)
    rr(draw, (340, 340, 560, 520), fill=blend(p[0], 0.76), outline=line_color(p[0]), width=6)
    for x in range(690, 1300, 120):
        for y in [315, 445]:
            rr(draw, (x, y, x + 85, y + 85), fill=blend(p[(x + y) % 4], 0.72), outline=line_color(p[(x + y) % 4]), width=4)
    for y, c in zip([280, 440, 600], p[1:]):
        arrow(draw, (575, 430), (675, y), line_color(c), 6)


def sata(draw, p):
    rr(draw, (150, 250, 520, 620), fill=blend(p[0], 0.88), outline=line_color(p[0]), width=6)
    rr(draw, (1200, 260, 1540, 610), fill=blend(p[1], 0.88), outline=line_color(p[1]), width=6)
    points = [(520, 430), (680, 360), (860, 500), (1040, 380), (1200, 430)]
    draw.line(points, fill=line_color(p[3]), width=18, joint="curve")
    for x, y in points[1:-1]:
        node(draw, x, y, 28, p[2])
    for y in [345, 430, 515]:
        draw.line([(230, y), (450, y)], fill=line_color(p[0]), width=9)
        draw.line([(1270, y), (1470, y)], fill=line_color(p[1]), width=9)


def m2(draw, p):
    rr(draw, (210, 315, 1450, 520), fill=blend(p[2], 0.85), outline=line_color(p[2]), width=7)
    draw.rounded_rectangle((1320, 360, 1405, 475), radius=18, fill=(255, 253, 248), outline=line_color(p[2]), width=5)
    for x in [360, 520, 680, 840, 1000, 1160]:
        rr(draw, (x, 355, x + 95, 95 + 395), fill=blend(p[(x // 100) % 4], 0.72), outline=line_color(p[(x // 100) % 4]), width=4)
    rr(draw, (230, 610, 1430, 690), fill=blend(p[0], 0.92), outline=line_color(p[0]), width=5)
    for x in [415, 645, 875, 1105]:
        arrow(draw, (x, 610), (x, 525), line_color(p[3]), 5)


def gui(draw, p):
    rr(draw, (170, 155, 1580, 710), fill=blend(p[0], 0.9), outline=line_color(p[0]), width=6)
    draw.rectangle((170, 155, 1580, 230), fill=blend(p[0], 0.65))
    for x in [230, 290, 350]:
        node(draw, x, 192, 14, p[1])
    for x, y, c in [(270, 300, p[1]), (520, 300, p[2]), (770, 300, p[3]), (270, 520, p[2]), (600, 520, p[1])]:
        card(draw, x, y, 205, 125, c, p[0])
    draw.polygon([(1200, 330), (1280, 550), (1222, 525), (1188, 625), (1148, 606), (1184, 510), (1128, 530)], fill=line_color(p[3]))


def cli(draw, p):
    rr(draw, (190, 180, 1130, 680), fill=blend(p[0], 0.88), outline=line_color(p[0]), width=6)
    draw.rectangle((190, 180, 1130, 250), fill=blend(p[0], 0.66))
    for y in [330, 420, 510, 600]:
        draw.line([(300, y), (900, y)], fill=line_color(p[0]), width=12)
        draw.rectangle((250, y - 8, 275, y + 8), fill=line_color(p[3]))
    for y, c in zip([260, 430, 600], p[1:]):
        arrow(draw, (1135, 430), (1310, y), line_color(c), 7)
        card(draw, 1320, y - 55, 260, 110, c, p[0])


def linux(draw, p):
    node(draw, 880, 430, 110, p[2])
    layers = [
        (500, 195, 760, 105, p[0]),
        (1010, 195, 760, 105, p[1]),
        (500, 595, 760, 105, p[3]),
        (1010, 595, 760, 105, p[0]),
    ]
    for x, y, w, h, c in layers:
        card(draw, x - w // 2, y - h // 2, w, h, c, p[2])
        draw.line([(x, y), (880, 430)], fill=line_color(c), width=6)
    rr(draw, (720, 300, 1040, 560), fill=blend(p[2], 0.8), outline=line_color(p[2]), width=7)
    for y in [360, 430, 500]:
        draw.line([(780, y), (980, y)], fill=line_color(p[2]), width=10)


def ubuntu(draw, p):
    rr(draw, (175, 230, 530, 630), fill=blend(p[1], 0.9), outline=line_color(p[1]), width=6)
    rr(draw, (700, 170, 1050, 690), fill=blend(p[2], 0.9), outline=line_color(p[2]), width=6)
    rr(draw, (1205, 240, 1555, 620), fill=blend(p[3], 0.9), outline=line_color(p[3]), width=6)
    for y in [315, 405, 495]:
        draw.line([(250, y), (455, y)], fill=line_color(p[1]), width=9)
        draw.rounded_rectangle((775, y - 25, 975, y + 25), radius=12, fill=(255, 253, 248), outline=line_color(p[2]), width=3)
        draw.line([(1285, y), (1475, y)], fill=line_color(p[3]), width=9)
    arrow(draw, (535, 430), (690, 430), line_color(p[1]), 8)
    arrow(draw, (1055, 430), (1195, 430), line_color(p[3]), 8)


def literacy(draw, p):
    for i, x in enumerate([150, 430, 710, 990, 1270]):
        card(draw, x, 340, 210, 120, p[i % 4], p[(i + 1) % 4])
        node(draw, x + 105, 550, 28, p[(i + 2) % 4])
        draw.line([(x + 105, 460), (x + 105, 520)], fill=line_color(p[(i + 2) % 4]), width=6)
        if i:
            arrow(draw, (x - 75, 400), (x - 15, 400), line_color(p[i % 4]), 7)
    draw.arc((360, 165, 1220, 680), 25, 335, fill=line_color(p[3]), width=7)


DRAWERS = {
    "gpu": gpu,
    "hdd": hdd,
    "ssd": ssd,
    "sata": sata,
    "m2": m2,
    "gui": gui,
    "cli": cli,
    "linux": linux,
    "ubuntu": ubuntu,
    "literacy": literacy,
}


def finish(image: Image.Image, entry_id: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    raw = image.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
    raw.save(OUT_DIR / f"{entry_id}_base_raw.png")
    final = raw.resize(FINAL_SIZE, Image.Resampling.LANCZOS)
    final.save(OUT_DIR / f"{entry_id}_base_1254x627.png")


def main() -> int:
    for index, (entry_id, variant) in enumerate(ENTRIES):
        image, draw, palette = base(index + 1)
        DRAWERS[variant](draw, palette)
        finish(image, entry_id)
        print(f"wrote {entry_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
