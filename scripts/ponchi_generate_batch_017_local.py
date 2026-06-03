#!/usr/bin/env python3
"""Generate local abstract 2:1 ponchi base diagrams for ponchi-batch-017."""
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


OUT_DIR = Path("assets/ponchi/experiments/batches/ponchi-batch-017")

ENTRIES = [
    ("J-33", "quantum"),
    ("J-40", "iot"),
    ("J-41", "dx"),
    ("J-42", "web3"),
    ("J-43", "saas"),
    ("J-50", "ethics"),
    ("J-51", "hallucination"),
    ("J-52", "sycophancy"),
    ("J-53", "copyright"),
    ("J-54", "management"),
    ("J-55", "personal_info"),
    ("J-56", "data_protection"),
    ("J-62", "turing"),
    ("J-70", "vram"),
    ("J-71", "ram"),
    ("J-72", "accelerator"),
    ("J-73", "next_gen"),
    ("J-74", "gpu_series"),
    ("J-75", "tensor_core"),
    ("J-76", "cpu"),
]


def quantum(draw, p):
    for y in [270, 430, 590]:
        card(draw, 160, y - 50, 240, 100, p[(y // 100) % 4], p[3])
    for i, x in enumerate([600, 760, 920]):
        node(draw, x, 430, 48, p[i])
        draw.arc((x - 85, 310, x + 85, 550), 25, 335, fill=line_color(p[i]), width=5)
    for a, b in [(600, 760), (760, 920)]:
        draw.line([(a, 430), (b, 430)], fill=line_color(p[3]), width=8)
    rr(draw, (1080, 260, 1270, 600), fill=blend(p[1], 0.82), outline=line_color(p[1]), width=6)
    arrow(draw, (970, 430), (1070, 430), line_color(p[2]), 8)
    for y, c in zip([305, 445, 585], p):
        card(draw, 1370, y - 50, 220, 100, c, p[1])
        arrow(draw, (1275, 430), (1360, y), line_color(c), 6)


def iot(draw, p):
    rr(draw, (725, 300, 1000, 585), fill=blend(p[0], 0.78), outline=line_color(p[0]), width=7)
    for i, angle in enumerate(range(0, 360, 36)):
        x = 865 + int(math.cos(math.radians(angle)) * 570)
        y = 440 + int(math.sin(math.radians(angle)) * 285)
        card(draw, x - 65, y - 45, 130, 90, p[i % 4], p[(i + 1) % 4])
        draw.line([(x, y), (865, 440)], fill=blend(p[i % 4], 0.38), width=5)
    for y in [360, 450, 540]:
        draw.line([(790, y), (930, y)], fill=line_color(p[0]), width=10)


def dx(draw, p):
    rr(draw, (120, 175, 690, 680), fill=blend(p[1], 0.9), outline=line_color(p[1]), width=6)
    for y in [255, 355, 455, 555]:
        draw.rounded_rectangle((210, y, 560, y + 50), radius=12, fill=(255, 253, 248), outline=line_color(p[1]), width=3)
    arrow(draw, (700, 430), (900, 430), line_color(p[3]), 10)
    rr(draw, (910, 175, 1600, 680), fill=blend(p[2], 0.9), outline=line_color(p[2]), width=6)
    for x, y, c in [(1030, 265, p[0]), (1230, 265, p[1]), (1130, 455, p[3]), (1370, 455, p[0])]:
        card(draw, x, y, 170, 110, c, p[2])
    for a, b in [((1115, 320), (1315, 320)), ((1315, 320), (1215, 510)), ((1215, 510), (1455, 510))]:
        arrow(draw, a, b, line_color(p[2]), 6)


def web3(draw, p):
    points = []
    for i, angle in enumerate(range(0, 360, 30)):
        x = 900 + int(math.cos(math.radians(angle)) * 430)
        y = 440 + int(math.sin(math.radians(angle)) * 270)
        points.append((x, y))
        node(draw, x, y, 30, p[i % 4])
    for i, a in enumerate(points):
        for b in [points[(i + 2) % len(points)], points[(i + 5) % len(points)]]:
            draw.line([a, b], fill=blend(p[i % 4], 0.45), width=4)
    rr(draw, (780, 320, 1020, 560), fill=blend(p[3], 0.82), outline=line_color(p[3]), width=6)
    for y in [375, 435, 495]:
        draw.line([(835, y), (965, y)], fill=line_color(p[3]), width=9)


def saas(draw, p):
    rr(draw, (700, 240, 1080, 610), fill=blend(p[0], 0.78), outline=line_color(p[0]), width=7)
    for y in [325, 415, 505]:
        draw.line([(785, y), (995, y)], fill=line_color(p[0]), width=10)
    for i, angle in enumerate(range(210, 511, 60)):
        x = 890 + int(math.cos(math.radians(angle)) * 560)
        y = 440 + int(math.sin(math.radians(angle)) * 290)
        card(draw, x - 110, y - 55, 220, 110, p[i % 4], p[3])
        arrow(draw, (1085 if x > 890 else 700, 440), (x, y), line_color(p[i % 4]), 6)
    draw.arc((610, 130, 1170, 750), 40, 320, fill=line_color(p[2]), width=9)


def ethics(draw, p):
    rr(draw, (120, 340, 390, 470), fill=blend(p[1], 0.85), outline=line_color(p[1]), width=5)
    arrow(draw, (400, 405), (560, 405), line_color(p[1]), 8)
    for i, (x, y) in enumerate([(590, 210), (835, 210), (590, 510), (835, 510)]):
        rr(draw, (x, y, x + 180, y + 130), fill=blend(p[i % 4], 0.86), outline=line_color(p[i % 4]), width=5)
        node(draw, x + 90, y + 65, 28, p[(i + 1) % 4])
    for y in [275, 575]:
        arrow(draw, (980, y), (1190, 405), line_color(p[3]), 7)
    rr(draw, (1200, 315, 1530, 500), fill=blend(p[2], 0.86), outline=line_color(p[2]), width=5)
    small_lines(draw, 1265, 365, 220, p[2], 3)


def hallucination(draw, p):
    card(draw, 130, 285, 320, 190, p[1], p[3])
    node(draw, 520, 380, 60, p[3])
    arrow(draw, (455, 380), (510, 380), line_color(p[3]), 8)
    for y, c in zip([185, 335, 485, 635], p):
        card(draw, 720, y, 245, 88, c, p[3])
        draw.line([(580, 380), (720, y + 44)], fill=line_color(c), width=6)
    arrow(draw, (980, 380), (1190, 380), line_color(p[2]), 8)
    card(draw, 1200, 290, 330, 180, p[2], p[0])
    draw.line([(1245, 420), (1325, 350), (1455, 435)], fill=line_color(p[2]), width=13)


def sycophancy(draw, p):
    rr(draw, (125, 180, 720, 680), fill=blend(p[1], 0.9), outline=line_color(p[1]), width=6)
    rr(draw, (970, 180, 1600, 680), fill=blend(p[2], 0.9), outline=line_color(p[2]), width=6)
    card(draw, 220, 360, 190, 95, p[3], p[1])
    card(draw, 480, 360, 190, 95, p[1], p[3])
    arrow(draw, (415, 407), (470, 407), line_color(p[1]), 8)
    card(draw, 1050, 260, 190, 95, p[3], p[2])
    card(draw, 1300, 260, 190, 95, p[0], p[2])
    card(draw, 1180, 500, 190, 95, p[2], p[3])
    for a, b, c in [((1245, 307), (1290, 307), p[3]), ((1145, 355), (1210, 500), p[0]), ((1375, 355), (1290, 500), p[2])]:
        arrow(draw, a, b, line_color(c), 7)


def copyright(draw, p):
    for y, c in zip([185, 330, 475, 620], p):
        card(draw, 135, y, 260, 95, c, p[3])
        arrow(draw, (405, y + 47), (650, 430), line_color(c), 6)
    rr(draw, (665, 230, 985, 640), fill=blend(p[0], 0.83), outline=line_color(p[0]), width=6)
    for y in [305, 405, 505]:
        draw.rounded_rectangle((735, y, 915, y + 48), radius=12, fill=(255, 253, 248), outline=line_color(p[0]), width=3)
    for y, c in zip([250, 430, 610], p[1:]):
        arrow(draw, (995, 430), (1225, y), line_color(c), 7)
        card(draw, 1235, y - 55, 300, 110, c, p[0])


def management(draw, p):
    node(draw, 890, 430, 105, p[2])
    labels = [(390, 250, p[0]), (1180, 250, p[1]), (1180, 560, p[3]), (390, 560, p[1])]
    for x, y, c in labels:
        card(draw, x, y, 260, 110, c, p[2])
    for a, b, c in [((650, 305), (780, 390), p[0]), ((1180, 305), (995, 390), p[1]), ((1180, 615), (995, 470), p[3]), ((650, 615), (780, 470), p[1])]:
        arrow(draw, a, b, line_color(c), 7)
    draw.arc((535, 105, 1265, 815), 20, 340, fill=line_color(p[0]), width=8)


def personal_info(draw, p):
    for y, c in zip([190, 320, 450, 580], p):
        card(draw, 130, y, 250, 90, c, p[3])
    for i, x in enumerate([520, 720, 920, 1120]):
        rr(draw, (x, 275, x + 135, 555), fill=blend(p[i % 4], 0.84), outline=line_color(p[i % 4]), width=5)
        node(draw, x + 68, 385, 30, p[(i + 1) % 4])
        if i:
            arrow(draw, (x - 80, 410), (x - 10, 410), line_color(p[i % 4]), 6)
    card(draw, 1340, 340, 240, 120, p[2], p[0])
    arrow(draw, (1260, 410), (1330, 410), line_color(p[2]), 7)


def data_protection(draw, p):
    rr(draw, (140, 170, 530, 690), fill=blend(p[2], 0.88), outline=line_color(p[2]), width=6)
    for y in [260, 360, 460, 560]:
        draw.line([(220, y), (455, y)], fill=line_color(p[2]), width=9)
    rr(draw, (760, 250, 1010, 600), fill=blend(p[0], 0.82), outline=line_color(p[0]), width=6)
    draw.arc((805, 210, 965, 375), 180, 360, fill=line_color(p[0]), width=16)
    for y, c in zip([240, 405, 570], p[1:]):
        arrow(draw, (1015, 425), (1235, y), line_color(c), 7)
        card(draw, 1245, y - 55, 310, 110, c, p[0])


def turing(draw, p):
    rr(draw, (135, 250, 450, 610), fill=blend(p[0], 0.88), outline=line_color(p[0]), width=6)
    for y in [330, 430, 530]:
        draw.line([(210, y), (380, y)], fill=line_color(p[0]), width=9)
    for x, c in [(780, p[1]), (1240, p[2])]:
        rr(draw, (x, 210, x + 260, 650), fill=blend(c, 0.88), outline=line_color(c), width=6)
        for y in [320, 440, 560]:
            card(draw, x + 55, y - 35, 150, 70, c, p[3])
        arrow(draw, (x, 430), (455, 430), line_color(c), 6)


def vram(draw, p):
    rr(draw, (300, 210, 1420, 650), fill=blend(p[0], 0.88), outline=line_color(p[0]), width=7)
    for i, x in enumerate(range(380, 1280, 150)):
        draw.rounded_rectangle((x, 300, x + 110, 560), radius=16, fill=blend(p[i % 4], 0.75), outline=line_color(p[i % 4]), width=5)
    for y, c in zip([230, 410, 610], p[1:]):
        card(draw, 120, y - 45, 210, 90, c, p[0])
        arrow(draw, (335, y), (380, y + 120 if y < 410 else y - 10), line_color(c), 6)
    card(draw, 1450, 310, 150, 130, p[1], p[0])


def ram(draw, p):
    rr(draw, (220, 310, 1460, 520), fill=blend(p[2], 0.85), outline=line_color(p[2]), width=7)
    for x in range(320, 1320, 140):
        draw.rounded_rectangle((x, 350, x + 90, 480), radius=12, fill=(255, 253, 248), outline=line_color(p[2]), width=4)
    for y, c in zip([190, 630], [p[1], p[3]]):
        for x in [300, 580, 860, 1140]:
            card(draw, x, y - 45, 170, 90, c, p[2])
            arrow(draw, (x + 85, y + 45 if y < 400 else y - 45), (x + 85, 310 if y < 400 else 520), line_color(c), 5)


def accelerator(draw, p):
    rr(draw, (260, 190, 1480, 690), fill=blend(p[0], 0.88), outline=line_color(p[0]), width=7)
    for x in [390, 620, 850, 1080, 1310]:
        for y in [300, 470]:
            rr(draw, (x, y, x + 130, y + 105), fill=blend(p[(x + y) % 4], 0.72), outline=line_color(p[(x + y) % 4]), width=5)
    for y in [260, 640]:
        draw.line([(330, y), (1400, y)], fill=line_color(p[3]), width=9)
    for x in [360, 610, 860, 1110, 1360]:
        arrow(draw, (x, 720), (x, 690), line_color(p[2]), 5)


def next_gen(draw, p):
    rr(draw, (145, 250, 575, 610), fill=blend(p[1], 0.9), outline=line_color(p[1]), width=6)
    rr(draw, (1060, 170, 1600, 690), fill=blend(p[2], 0.9), outline=line_color(p[2]), width=6)
    for x, y, c in [(240, 350, p[0]), (350, 475, p[3]), (1160, 255, p[0]), (1320, 380, p[1]), (1210, 540, p[3])]:
        card(draw, x, y, 160, 85, c, p[2])
    arrow(draw, (590, 430), (1045, 430), line_color(p[3]), 11)
    draw.arc((650, 210, 1120, 660), 210, 330, fill=line_color(p[1]), width=10)


def gpu_series(draw, p):
    sizes = [(180, 140), (430, 170), (700, 205), (1010, 245), (1335, 285)]
    for i, (x, h) in enumerate(sizes):
        rr(draw, (x, 560 - h, x + 190, 560), fill=blend(p[i % 4], 0.85), outline=line_color(p[i % 4]), width=6)
        node(draw, x + 95, 475, 35 + i * 3, p[(i + 1) % 4])
        for px in range(x + 30, x + 160, 45):
            draw.line([(px, 565), (px, 625)], fill=line_color(p[i % 4]), width=5)
    for x in [250, 525, 790, 1100, 1425]:
        card(draw, x - 85, 235, 170, 90, p[(x // 100) % 4], p[3])


def tensor_core(draw, p):
    for x in [160, 310, 460]:
        for y in [250, 400, 550]:
            rr(draw, (x, y, x + 90, y + 90), fill=blend(p[(x + y) % 4], 0.75), outline=line_color(p[(x + y) % 4]), width=4)
    arrow(draw, (590, 430), (735, 430), line_color(p[3]), 9)
    for x in [760, 905, 1050]:
        for y in [300, 445]:
            rr(draw, (x, y, x + 105, y + 105), fill=blend(p[(x + y) % 4], 0.7), outline=line_color(p[(x + y) % 4]), width=5)
    arrow(draw, (1170, 430), (1325, 430), line_color(p[1]), 9)
    card(draw, 1335, 335, 250, 150, p[1], p[0])


def cpu(draw, p):
    rr(draw, (760, 260, 1030, 560), fill=blend(p[0], 0.78), outline=line_color(p[0]), width=7)
    for x in range(700, 1100, 45):
        draw.line([(x, 230), (x, 260)], fill=line_color(p[0]), width=5)
        draw.line([(x, 560), (x, 590)], fill=line_color(p[0]), width=5)
    for y in range(300, 540, 55):
        draw.line([(825, y), (965, y)], fill=line_color(p[0]), width=9)
    for x, y, c in [(150, 210, p[1]), (160, 555, p[2]), (1320, 210, p[3]), (1320, 555, p[1])]:
        card(draw, x, y, 260, 105, c, p[0])
        arrow(draw, (x + (260 if x < 760 else 0), y + 52), (760 if x < 760 else 1030, 410), line_color(c), 7)


DRAWERS = {
    "quantum": quantum,
    "iot": iot,
    "dx": dx,
    "web3": web3,
    "saas": saas,
    "ethics": ethics,
    "hallucination": hallucination,
    "sycophancy": sycophancy,
    "copyright": copyright,
    "management": management,
    "personal_info": personal_info,
    "data_protection": data_protection,
    "turing": turing,
    "vram": vram,
    "ram": ram,
    "accelerator": accelerator,
    "next_gen": next_gen,
    "gpu_series": gpu_series,
    "tensor_core": tensor_core,
    "cpu": cpu,
}


def finish(image: Image.Image, entry_id: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    raw = image.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
    raw.save(OUT_DIR / f"{entry_id}_base_raw.png")
    final = raw.resize(FINAL_SIZE, Image.Resampling.LANCZOS)
    final.save(OUT_DIR / f"{entry_id}_base_1254x627.png")


def main() -> int:
    for index, (entry_id, variant) in enumerate(ENTRIES):
        image, draw, palette = base(index + 3)
        DRAWERS[variant](draw, palette)
        finish(image, entry_id)
        print(f"wrote {entry_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
