#!/usr/bin/env python3
"""Generate local abstract 2:1 ponchi base diagrams for ponchi-batch-016."""
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


OUT_DIR = Path("assets/ponchi/experiments/batches/ponchi-batch-016")

ENTRIES = [
    ("J-1", "agi"),
    ("J-2", "strong_weak"),
    ("J-3", "singularity"),
    ("J-4", "asi"),
    ("J-10", "machine_learning"),
    ("J-11", "deep_learning"),
    ("J-12", "neural_network"),
    ("J-13", "transformer"),
    ("J-14", "llm"),
    ("J-15", "vlm"),
    ("J-16", "fine_tuning"),
    ("J-17", "attention"),
    ("J-18", "moe"),
    ("J-19", "quantization"),
    ("J-20", "big_data"),
    ("J-21", "lora"),
    ("J-22", "parameter_scale"),
    ("J-23", "diffusion"),
    ("J-31", "fifth_generation"),
    ("J-32", "von_neumann"),
]


def agi(draw, p):
    node(draw, 900, 430, 115, p[0])
    for i, angle in enumerate(range(0, 360, 45)):
        x = 900 + int(math.cos(math.radians(angle)) * 365)
        y = 430 + int(math.sin(math.radians(angle)) * 245)
        card(draw, x - 100, y - 55, 200, 110, p[i % 4], p[(i + 1) % 4])
        arrow(draw, (x - int(math.cos(math.radians(angle)) * 90), y - int(math.sin(math.radians(angle)) * 60)), (900, 430), line_color(p[i % 4]), 7)
    rr(draw, (695, 300, 1105, 560), fill=blend(p[0], 0.8), outline=line_color(p[0]), width=7)
    for y in [350, 420, 490]:
        draw.line([(775, y), (1025, y)], fill=line_color(p[0]), width=10)


def strong_weak(draw, p):
    rr(draw, (130, 170, 750, 685), fill=blend(p[1], 0.9), outline=line_color(p[1]), width=6)
    rr(draw, (1010, 170, 1600, 685), fill=blend(p[2], 0.9), outline=line_color(p[2]), width=6)
    card(draw, 300, 370, 280, 120, p[1], p[3])
    for x, y, c in [(1110, 250, p[0]), (1325, 250, p[1]), (1160, 450, p[2]), (1370, 520, p[3])]:
        card(draw, x, y, 160, 110, c, p[0])
    node(draw, 1305, 410, 58, p[2])
    for target in [(1190, 305), (1405, 305), (1240, 505), (1450, 575)]:
        draw.line([(1305, 410), target], fill=line_color(p[2]), width=6)
    arrow(draw, (760, 430), (995, 430), line_color(p[3]), 10)


def singularity(draw, p):
    points = [(165, 645), (360, 610), (550, 565), (740, 500), (900, 395), (1040, 270), (1180, 185), (1395, 140), (1590, 125)]
    draw.line(points, fill=line_color(p[1]), width=14, joint="curve")
    for i, point in enumerate(points[:-1]):
        node(draw, point[0], point[1], 28 + i * 2, p[i % 4])
    rr(draw, (880, 155, 1225, 655), fill=None, outline=line_color(p[3]), width=8)
    for x, y, c in [(235, 290, p[2]), (480, 245, p[0]), (1300, 360, p[3]), (1420, 510, p[2])]:
        card(draw, x, y, 180, 100, c, p[1])


def asi(draw, p):
    for x, size, color in [(250, 120, p[1]), (625, 175, p[2]), (1150, 270, p[0])]:
        rr(draw, (x, 430 - size, x + size * 2, 430 + size), fill=blend(color, 0.85), outline=line_color(color), width=7)
        for i in range(3):
            draw.line([(x + 55, 360 + i * 55), (x + size * 2 - 55, 360 + i * 55)], fill=line_color(color), width=8)
    for x in [520, 955]:
        arrow(draw, (x, 430), (x + 95, 430), line_color(p[3]), 9)
    draw.arc((1010, 130, 1660, 730), 205, 330, fill=line_color(p[1]), width=10)


def machine_learning(draw, p):
    for y, c in zip([200, 340, 480, 620], p):
        card(draw, 130, y, 270, 90, c, p[3])
        arrow(draw, (410, y + 45), (720, 430), line_color(c), 7)
    rr(draw, (730, 280, 1035, 585), fill=blend(p[2], 0.78), outline=line_color(p[2]), width=7)
    for y in [345, 430, 515]:
        draw.line([(805, y), (960, y)], fill=line_color(p[2]), width=12)
    arrow(draw, (1045, 430), (1260, 350), line_color(p[1]), 9)
    card(draw, 1270, 285, 285, 130, p[1], p[0])
    arrow(draw, (1415, 420), (885, 655), line_color(p[3]), 7)


def deep_learning(draw, p):
    xs = [250, 480, 710, 940, 1170, 1400]
    for i, x in enumerate(xs):
        rr(draw, (x, 170, x + 110, 695), fill=blend(p[i % 4], 0.88), outline=line_color(p[i % 4]), width=5)
        for y in [245, 350, 455, 560, 650]:
            node(draw, x + 55, y, 20, p[(i + 1) % 4])
        if i:
            for y in [260, 410, 575]:
                draw.line([(x - 120, y), (x, y - 25)], fill=line_color(p[i % 4]), width=4)


def neural_network(draw, p):
    columns = [(260, 4), (580, 5), (900, 5), (1220, 3), (1490, 2)]
    node_positions = []
    for ci, (x, count) in enumerate(columns):
        col = []
        for j in range(count):
            y = 240 + j * (410 // max(1, count - 1))
            node(draw, x, y, 26, p[(ci + j) % 4])
            col.append((x, y))
        node_positions.append(col)
    for left, right in zip(node_positions, node_positions[1:]):
        for a in left:
            for b in right:
                draw.line([a, b], fill=blend(p[0], 0.45), width=3)


def transformer(draw, p):
    for i, x in enumerate([170, 310, 450, 590, 730]):
        card(draw, x, 185, 105, 105, p[i % 4], p[3])
    for a, b in [(225, 505), (365, 645), (505, 225), (645, 365), (785, 505)]:
        draw.arc((a - 170, 260, b + 170, 560), 190, 350, fill=line_color(p[(a + b) % 4]), width=5)
    for i, x in enumerate([920, 1110, 1300]):
        rr(draw, (x, 260, x + 145, 610), fill=blend(p[(i + 1) % 4], 0.84), outline=line_color(p[(i + 1) % 4]), width=5)
        for y in [335, 435, 535]:
            draw.line([(x + 35, y), (x + 110, y)], fill=line_color(p[(i + 1) % 4]), width=7)
    arrow(draw, (805, 410), (910, 410), line_color(p[3]), 8)


def llm(draw, p):
    for x in range(150, 700, 110):
        for y in [235, 345, 455, 565]:
            card(draw, x, y, 85, 72, p[(x + y) % 4], p[2])
    arrow(draw, (730, 430), (880, 430), line_color(p[3]), 10)
    node(draw, 1010, 430, 120, p[0])
    arrow(draw, (1140, 430), (1290, 430), line_color(p[1]), 10)
    card(draw, 1300, 330, 300, 200, p[1], p[3])


def vlm(draw, p):
    for i, (x, y) in enumerate([(150, 220), (360, 220), (150, 465), (360, 465)]):
        rr(draw, (x, y, x + 160, y + 150), fill=blend(p[i % 4], 0.86), outline=line_color(p[i % 4]), width=5)
        node(draw, x + 80, y + 75, 36, p[(i + 1) % 4])
    for x in [610, 720, 830]:
        card(draw, x, 300, 90, 90, p[(x // 100) % 4], p[3])
        card(draw, x, 430, 90, 90, p[(x // 120) % 4], p[2])
    node(draw, 1080, 410, 110, p[2])
    arrow(draw, (930, 410), (960, 410), line_color(p[3]), 9)
    card(draw, 1290, 290, 310, 220, p[1], p[0])
    arrow(draw, (1195, 410), (1280, 410), line_color(p[1]), 9)


def fine_tuning(draw, p):
    card(draw, 130, 300, 285, 180, p[0], p[3])
    for y, c in zip([180, 310, 440, 570], p):
        card(draw, 520, y, 220, 90, c, p[1])
        arrow(draw, (750, y + 45), (875, 405), line_color(c), 6)
    rr(draw, (860, 250, 1120, 570), fill=blend(p[2], 0.8), outline=line_color(p[2]), width=7)
    arrow(draw, (425, 390), (850, 390), line_color(p[3]), 8)
    arrow(draw, (1130, 405), (1275, 405), line_color(p[1]), 9)
    card(draw, 1285, 300, 300, 180, p[1], p[0])


def attention(draw, p):
    node(draw, 360, 430, 58, p[3])
    targets = []
    for i, angle in enumerate(range(-70, 71, 20)):
        x = 980 + int(math.cos(math.radians(angle)) * 330)
        y = 430 + int(math.sin(math.radians(angle)) * 250)
        targets.append((x, y, p[i % 4]))
        node(draw, x, y, 32, p[i % 4])
    for i, (x, y, c) in enumerate(targets):
        width = 4 + (i % 4) * 3
        draw.line([(360, 430), (x, y)], fill=line_color(c), width=width)
    rr(draw, (230, 300, 490, 560), fill=None, outline=line_color(p[3]), width=7)


def moe(draw, p):
    card(draw, 140, 360, 250, 130, p[3], p[1])
    arrow(draw, (400, 425), (635, 425), line_color(p[3]), 9)
    rr(draw, (640, 285, 850, 565), fill=blend(p[0], 0.78), outline=line_color(p[0]), width=7)
    for i, y in enumerate([160, 275, 390, 505, 620]):
        c = p[i % 4]
        alpha = 0.68 if i in {1, 3} else 0.91
        card(draw, 1040, y, 245, 90, c, p[2])
        draw.line([(855, 425), (1040, y + 45)], fill=line_color(c) if i in {1, 3} else blend(c, 0.5), width=8 if i in {1, 3} else 3)
        if alpha > 0.8:
            draw.rectangle((1305, y + 25, 1375, y + 65), fill=blend(c, 0.65))
    arrow(draw, (1385, 390), (1540, 390), line_color(p[1]), 8)
    card(draw, 1545, 335, 105, 110, p[1], p[0])


def quantization(draw, p):
    card(draw, 140, 250, 380, 260, p[0], p[3])
    for i, x in enumerate([610, 710, 810]):
        node(draw, x, 380 + i * 25, 32, p[(i + 1) % 4])
    arrow(draw, (530, 380), (600, 380), line_color(p[3]), 8)
    arrow(draw, (850, 430), (1050, 430), line_color(p[2]), 8)
    card(draw, 1060, 310, 240, 170, p[2], p[0])
    for w, y, c in [(350, 590, p[0]), (210, 655, p[2])]:
        rr(draw, (140, y, 140 + w, y + 42), fill=blend(c, 0.55), outline=line_color(c), width=4)
    for x in [1360, 1460, 1560]:
        draw.rounded_rectangle((x, 300, x + 75, 520), radius=16, fill=blend(p[1], 0.78), outline=line_color(p[1]), width=5)


def big_data(draw, p):
    for i, y in enumerate([165, 275, 385, 495, 605]):
        card(draw, 130, y, 245, 80, p[i % 4], p[3])
        arrow(draw, (385, y + 40), (685, 430), line_color(p[i % 4]), 6)
    for i, y in enumerate([315, 445, 575]):
        draw.ellipse((690, y - 55, 1040, y + 55), fill=blend(p[2], 0.75), outline=line_color(p[2]), width=6)
        if i < 2:
            draw.rectangle((690, y, 1040, y + 130), fill=blend(p[2], 0.75), outline=line_color(p[2]), width=6)
    for y, c in zip([230, 395, 560], p[1:]):
        arrow(draw, (1050, 430), (1250, y + 50), line_color(c), 7)
        card(draw, 1260, y, 300, 100, c, p[0])


def lora(draw, p):
    card(draw, 190, 260, 440, 260, p[0], p[3])
    draw.line([(410, 185), (410, 595)], fill=line_color(p[0]), width=9)
    node(draw, 410, 185, 25, p[1])
    node(draw, 410, 595, 25, p[1])
    for y, c in zip([240, 365, 490], p[1:]):
        card(draw, 760, y, 210, 90, c, p[0])
        arrow(draw, (635, 390), (750, y + 45), line_color(c), 6)
    arrow(draw, (980, 395), (1220, 395), line_color(p[3]), 9)
    card(draw, 1230, 300, 300, 180, p[2], p[0])


def parameter_scale(draw, p):
    sizes = [(180, 105), (330, 150), (540, 215), (830, 300), (1240, 390)]
    for i, (x, size) in enumerate(sizes):
        rr(draw, (x, 650 - size, x + size, 650), fill=blend(p[i % 4], 0.82), outline=line_color(p[i % 4]), width=6)
        for j in range(3):
            draw.line([(x + 25, 625 - j * 48), (x + size - 25, 625 - j * 48)], fill=line_color(p[i % 4]), width=6)
    for i, x in enumerate([205, 410, 650, 980, 1430]):
        node(draw, x, 735, 22, p[i % 4])


def diffusion(draw, p):
    for i, x in enumerate([130, 370, 610, 850, 1090, 1330]):
        rr(draw, (x, 250, x + 180, 260 + 260), fill=blend(p[i % 4], 0.86), outline=line_color(p[i % 4]), width=5)
        step = max(8, 32 - i * 5)
        for px in range(x + 30, x + 150, step):
            for py in range(295, 475, step):
                node(draw, px, py, max(3, 8 - i), p[(i + px + py) % 4])
        if i:
            arrow(draw, (x - 50, 380), (x - 10, 380), line_color(p[i % 4]), 6)


def fifth_generation(draw, p):
    rr(draw, (150, 170, 560, 700), fill=blend(p[3], 0.88), outline=line_color(p[3]), width=6)
    for x, y, c in [(250, 280, p[0]), (360, 420, p[1]), (240, 570, p[2])]:
        card(draw, x, y, 210, 90, c, p[3])
    rr(draw, (760, 210, 1050, 650), fill=blend(p[0], 0.84), outline=line_color(p[0]), width=6)
    for y in [300, 400, 500, 600]:
        draw.rounded_rectangle((830, y, 985, y + 42), radius=12, fill=(255, 253, 248), outline=line_color(p[0]), width=3)
    for x, y, c in [(1260, 240, p[1]), (1400, 400, p[2]), (1200, 570, p[3])]:
        arrow(draw, (1055, 430), (x, y + 50), line_color(c), 7)
        card(draw, x, y, 230, 100, c, p[0])


def von_neumann(draw, p):
    rr(draw, (650, 250, 1080, 590), fill=blend(p[0], 0.82), outline=line_color(p[0]), width=7)
    for y in [330, 420, 510]:
        draw.line([(735, y), (995, y)], fill=line_color(p[0]), width=10)
    positions = [(200, 210, p[1]), (200, 540, p[2]), (1270, 210, p[3]), (1270, 540, p[1])]
    for x, y, c in positions:
        card(draw, x, y, 260, 130, c, p[0])
        arrow(draw, (x + (260 if x < 650 else 0), y + 65), (650 if x < 650 else 1080, 420), line_color(c), 7)
    draw.line([(460, 420), (1270, 420)], fill=line_color(p[3]), width=14)


DRAWERS = {
    "agi": agi,
    "strong_weak": strong_weak,
    "singularity": singularity,
    "asi": asi,
    "machine_learning": machine_learning,
    "deep_learning": deep_learning,
    "neural_network": neural_network,
    "transformer": transformer,
    "llm": llm,
    "vlm": vlm,
    "fine_tuning": fine_tuning,
    "attention": attention,
    "moe": moe,
    "quantization": quantization,
    "big_data": big_data,
    "lora": lora,
    "parameter_scale": parameter_scale,
    "diffusion": diffusion,
    "fifth_generation": fifth_generation,
    "von_neumann": von_neumann,
}


def finish(image: Image.Image, entry_id: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    raw = image.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
    raw.save(OUT_DIR / f"{entry_id}_base_raw.png")
    final = raw.resize(FINAL_SIZE, Image.Resampling.LANCZOS)
    final.save(OUT_DIR / f"{entry_id}_base_1254x627.png")


def main() -> int:
    for index, (entry_id, variant) in enumerate(ENTRIES):
        image, draw, palette = base(index + 2)
        DRAWERS[variant](draw, palette)
        finish(image, entry_id)
        print(f"wrote {entry_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
