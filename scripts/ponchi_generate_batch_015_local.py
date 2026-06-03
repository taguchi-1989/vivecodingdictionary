#!/usr/bin/env python3
"""Generate local abstract 2:1 ponchi base diagrams for ponchi-batch-015."""
from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


RAW_SIZE = (1774, 887)
FINAL_SIZE = (1254, 627)
OUT_DIR = Path("assets/ponchi/experiments/batches/ponchi-batch-015")

PALETTES = [
    ((42, 67, 101), (235, 92, 71), (46, 150, 142), (244, 184, 82)),
    ((54, 83, 70), (214, 96, 77), (70, 129, 170), (235, 198, 90)),
    ((80, 73, 120), (222, 107, 74), (65, 153, 124), (238, 189, 78)),
    ((45, 88, 111), (199, 83, 94), (93, 145, 79), (231, 176, 93)),
]

ENTRIES = [
    ("H-63", "culture"),
    ("I-1", "protocol"),
    ("I-2", "server_bridge"),
    ("I-3", "client"),
    ("I-4", "transport"),
    ("I-5", "sdk"),
    ("I-10", "access_gate"),
    ("I-11", "repo"),
    ("I-12", "vcs"),
    ("I-13", "chat"),
    ("I-20", "browser_actions"),
    ("I-21", "browser_control"),
    ("I-22", "devtools"),
    ("I-23", "code_nav"),
    ("I-24", "docs"),
    ("I-30", "workspace_docs"),
    ("I-41", "database"),
    ("I-50", "cloud"),
    ("I-80", "template"),
    ("I-81", "registration"),
]


def blend(color: tuple[int, int, int], amount: float = 0.88) -> tuple[int, int, int]:
    return tuple(int(c + (255 - c) * amount) for c in color)


def line_color(color: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(max(0, int(c * 0.72)) for c in color)


def rr(draw: ImageDraw.ImageDraw, box, fill, outline=None, width=5, radius=28):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def arrow(draw: ImageDraw.ImageDraw, a, b, color, width=10):
    draw.line([a, b], fill=color, width=width, joint="curve")
    angle = math.atan2(b[1] - a[1], b[0] - a[0])
    size = width * 3.2
    left = (b[0] - size * math.cos(angle - 0.45), b[1] - size * math.sin(angle - 0.45))
    right = (b[0] - size * math.cos(angle + 0.45), b[1] - size * math.sin(angle + 0.45))
    draw.polygon([b, left, right], fill=color)


def small_lines(draw: ImageDraw.ImageDraw, x, y, w, color, rows=4):
    for index in range(rows):
        yy = y + index * 22
        length = int(w * (0.48 + 0.13 * ((index * 7) % 4)))
        draw.line([(x, yy), (x + length, yy)], fill=blend(color, 0.25), width=8)


def card(draw: ImageDraw.ImageDraw, x, y, w, h, color, accent=None, radius=24):
    rr(draw, (x, y, x + w, y + h), fill=blend(color, 0.86), outline=line_color(color), width=5, radius=radius)
    if accent:
        draw.rounded_rectangle((x + 24, y + 22, x + 74, y + 72), radius=14, fill=accent)
    small_lines(draw, x + 95, y + 30, w - 130, color, rows=max(2, int(h / 58)))


def node(draw: ImageDraw.ImageDraw, x, y, r, color):
    draw.ellipse((x - r, y - r, x + r, y + r), fill=blend(color, 0.72), outline=line_color(color), width=5)


def base(palette_index: int) -> tuple[Image.Image, ImageDraw.ImageDraw, tuple[tuple[int, int, int], ...]]:
    palette = PALETTES[palette_index % len(PALETTES)]
    image = Image.new("RGB", RAW_SIZE, (249, 247, 241))
    draw = ImageDraw.Draw(image)
    for y in range(0, RAW_SIZE[1], 38):
        draw.line([(0, y), (RAW_SIZE[0], y)], fill=(235, 231, 222), width=1)
    for x in range(0, RAW_SIZE[0], 38):
        draw.line([(x, 0), (x, RAW_SIZE[1])], fill=(239, 235, 227), width=1)
    draw.rounded_rectangle((52, 52, RAW_SIZE[0] - 52, RAW_SIZE[1] - 52), radius=42, fill=(255, 253, 248), outline=(222, 216, 205), width=4)
    return image, draw, palette


def culture(draw, p):
    for i, y in enumerate([185, 330, 475, 620]):
        card(draw, 130, y, 310, 105, p[i % 4], p[(i + 1) % 4])
        arrow(draw, (450, y + 52), (650, 430), line_color(p[2]), 7)
    for i, x in enumerate([690, 860, 1030, 1200]):
        node(draw, x, 430, 35, p[i % 4])
        if i:
            arrow(draw, (x - 125, 430), (x - 43, 430), line_color(p[0]), 8)
    for i, y in enumerate([255, 380, 505]):
        card(draw, 1350, y, 270, 100, p[(i + 1) % 4], p[i % 4])
        arrow(draw, (1240, 430), (1345, y + 50), line_color(p[3]), 7)


def protocol(draw, p):
    for y, c in zip([210, 360, 510], p):
        card(draw, 130, y, 310, 120, c, p[3])
        arrow(draw, (450, y + 60), (705, 430), line_color(c), 8)
    rr(draw, (710, 190, 1075, 675), fill=blend(p[0], 0.75), outline=line_color(p[0]), width=6)
    for y in [260, 365, 470, 575]:
        draw.line([(780, y), (1005, y)], fill=line_color(p[0]), width=12)
    for y, c in zip([235, 390, 545], p[1:]):
        arrow(draw, (1080, 430), (1265, y + 55), line_color(c), 8)
        card(draw, 1270, y, 330, 110, c, p[0])


def server_bridge(draw, p):
    for y, c in zip([210, 375, 540], p):
        card(draw, 120, y, 330, 120, c, p[2])
        arrow(draw, (460, y + 60), (750, 440), line_color(c), 8)
    rr(draw, (735, 245, 1075, 635), fill=blend(p[2], 0.7), outline=line_color(p[2]), width=7)
    for y in [315, 400, 485, 570]:
        draw.rounded_rectangle((800, y, 1010, y + 42), radius=14, fill=(255, 253, 248), outline=line_color(p[2]), width=4)
    for y, c in zip([240, 410, 580], p[1:]):
        arrow(draw, (1080, 440), (1280, y + 55), line_color(c), 8)
        card(draw, 1285, y, 340, 110, c, p[0])


def client(draw, p):
    rr(draw, (130, 160, 760, 705), fill=blend(p[1], 0.82), outline=line_color(p[1]), width=6)
    draw.rectangle((130, 160, 760, 230), fill=blend(p[1], 0.65))
    for i, x in enumerate([200, 280, 360]):
        node(draw, x, 195, 13, p[i])
    for y, c in zip([285, 405, 525], p):
        card(draw, 210, y, 430, 90, c, p[2])
    for x, c in zip([960, 1165, 1370], p[1:]):
        card(draw, x, 245, 170, 270, c, p[0])
        arrow(draw, (x + 85, 520), (760, 440), line_color(c), 8)


def transport(draw, p):
    for idx, y in enumerate([215, 525]):
        rr(draw, (150, y, 1580, y + 185), fill=blend(p[idx], 0.9), outline=line_color(p[idx]), width=5)
        card(draw, 230, y + 45, 270, 95, p[idx], p[2])
        for x in [650, 860, 1070]:
            node(draw, x, y + 92, 34, p[(idx + 2) % 4])
            arrow(draw, (x - 115, y + 92), (x - 42, y + 92), line_color(p[idx]), 7)
        card(draw, 1230, y + 45, 270, 95, p[(idx + 1) % 4], p[3])
        arrow(draw, (1110, y + 92), (1220, y + 92), line_color(p[idx]), 7)


def sdk(draw, p):
    for i, y in enumerate([190, 350, 510]):
        card(draw, 135, y, 300, 110, p[i], p[3])
        arrow(draw, (450, y + 55), (735, 435), line_color(p[i]), 8)
    node(draw, 885, 435, 150, p[2])
    for angle in range(0, 360, 40):
        x = 885 + int(math.cos(math.radians(angle)) * 116)
        y = 435 + int(math.sin(math.radians(angle)) * 116)
        node(draw, x, y, 16, p[3])
    for i, y in enumerate([250, 430, 610]):
        arrow(draw, (1035, 435), (1240, y), line_color(p[2]), 8)
        card(draw, 1245, y - 55, 320, 110, p[(i + 1) % 4], p[0])


def access_gate(draw, p):
    rr(draw, (130, 170, 540, 705), fill=blend(p[2], 0.86), outline=line_color(p[2]), width=6)
    for x, y in [(210, 250), (290, 350), (210, 455), (310, 570)]:
        draw.rounded_rectangle((x, y, x + 120, y + 72), radius=16, fill=blend(p[3], 0.55), outline=line_color(p[3]), width=4)
    rr(draw, (735, 260, 990, 630), fill=blend(p[0], 0.78), outline=line_color(p[0]), width=7)
    draw.arc((775, 220, 950, 375), 180, 360, fill=line_color(p[0]), width=18)
    arrow(draw, (545, 440), (725, 440), line_color(p[2]), 9)
    arrow(draw, (995, 440), (1195, 330), line_color(p[1]), 9)
    arrow(draw, (995, 470), (1195, 600), line_color(p[0]), 9)
    card(draw, 1200, 245, 360, 120, p[1], p[3])
    card(draw, 1200, 545, 360, 120, p[0], p[2])
    draw.line([(1270, 585), (1350, 635), (1490, 565)], fill=line_color(p[0]), width=18)


def repo(draw, p):
    for i, y in enumerate([200, 350, 500]):
        card(draw, 130, y, 300, 105, p[i], p[3])
        arrow(draw, (445, y + 52), (720, 430), line_color(p[i]), 8)
    rr(draw, (715, 185, 1580, 690), fill=blend(p[2], 0.88), outline=line_color(p[2]), width=6)
    for x in [820, 1020, 1220, 1420]:
        for y in [285, 435, 585]:
            draw.rounded_rectangle((x, y, x + 115, y + 72), radius=14, fill=(255, 253, 248), outline=line_color(p[2]), width=3)
    for x1, x2 in [(878, 1078), (1078, 1278), (1278, 1478)]:
        draw.line([(x1, 470), (x2, 320)], fill=line_color(p[1]), width=7)


def vcs(draw, p):
    for x, c in zip([160, 380, 600], p):
        card(draw, x, 180, 180, 260, c, p[3])
    points = [(850, 650), (980, 560), (1060, 450), (1180, 360), (1330, 280), (1500, 210)]
    draw.line(points, fill=line_color(p[0]), width=11)
    for i, point in enumerate(points):
        node(draw, point[0], point[1], 31, p[i % 4])
    draw.line([(1060, 450), (1150, 520), (1315, 550), (1470, 650)], fill=line_color(p[2]), width=9)
    for point in [(1150, 520), (1315, 550), (1470, 650)]:
        node(draw, point[0], point[1], 26, p[2])
    arrow(draw, (700, 330), (835, 620), line_color(p[3]), 8)


def chat(draw, p):
    for i, y in enumerate([170, 310, 450, 590]):
        rr(draw, (135, y, 570, y + 95), fill=blend(p[i % 4], 0.85), outline=line_color(p[i % 4]), width=5)
        node(draw, 205, y + 47, 25, p[(i + 1) % 4])
        small_lines(draw, 260, y + 28, 260, p[i % 4], 2)
        arrow(draw, (580, y + 47), (760, 425), line_color(p[i % 4]), 7)
    rr(draw, (780, 190, 1570, 690), fill=blend(p[2], 0.88), outline=line_color(p[2]), width=6)
    for x, y, c in [(900, 290, p[0]), (1120, 290, p[1]), (1340, 290, p[3]), (1010, 500, p[1]), (1230, 500, p[0])]:
        card(draw, x, y, 170, 120, c, p[2])


def browser_actions(draw, p):
    rr(draw, (160, 150, 1020, 710), fill=blend(p[0], 0.88), outline=line_color(p[0]), width=6)
    draw.rectangle((160, 150, 1020, 225), fill=blend(p[0], 0.66))
    for x in [220, 280, 340]:
        node(draw, x, 187, 14, p[1])
    for x, y, c in [(250, 300, p[1]), (500, 300, p[2]), (750, 300, p[3]), (380, 510, p[3]), (650, 510, p[1])]:
        card(draw, x, y, 170, 105, c, p[0])
    draw.polygon([(1085, 350), (1160, 545), (1110, 525), (1080, 620), (1042, 604), (1072, 512), (1020, 530)], fill=line_color(p[3]))
    for i, y in enumerate([210, 355, 500]):
        card(draw, 1260, y, 270, 100, p[i], p[2])
        arrow(draw, (1170, 420), (1250, y + 50), line_color(p[i]), 7)


def browser_control(draw, p):
    for x, c in [(140, p[0]), (890, p[2])]:
        rr(draw, (x, 185, x + 620, 635), fill=blend(c, 0.88), outline=line_color(c), width=6)
        draw.rectangle((x, 185, x + 620, 250), fill=blend(c, 0.68))
        for y in [310, 420, 530]:
            draw.rounded_rectangle((x + 90, y, x + 520, y + 45), radius=12, fill=(255, 253, 248), outline=line_color(c), width=3)
    arrow(draw, (770, 410), (880, 410), line_color(p[3]), 10)
    card(draw, 665, 660, 440, 80, p[1], p[3])


def devtools(draw, p):
    rr(draw, (145, 170, 675, 665), fill=blend(p[0], 0.88), outline=line_color(p[0]), width=6)
    draw.rectangle((145, 170, 675, 235), fill=blend(p[0], 0.66))
    rr(draw, (760, 250, 990, 585), fill=blend(p[3], 0.75), outline=line_color(p[3]), width=6)
    arrow(draw, (675, 420), (750, 420), line_color(p[0]), 8)
    for i, y in enumerate([185, 335, 485]):
        card(draw, 1130, y, 365, 105, p[i + 1], p[0])
        arrow(draw, (990, 420), (1120, y + 52), line_color(p[i + 1]), 7)
    for x in [235, 330, 425, 520]:
        h = (x % 5 + 2) * 35
        draw.rectangle((x, 595 - h, x + 48, 595), fill=blend(p[2], 0.35), outline=line_color(p[2]), width=3)


def code_nav(draw, p):
    for x in [135, 300, 465, 630]:
        card(draw, x, 190, 130, 360, p[(x // 100) % 4], p[3])
    arrow(draw, (790, 430), (920, 430), line_color(p[1]), 10)
    rr(draw, (950, 160, 1590, 700), fill=blend(p[2], 0.88), outline=line_color(p[2]), width=6)
    node(draw, 1250, 430, 75, p[1])
    for angle in range(0, 360, 45):
        x = 1250 + int(math.cos(math.radians(angle)) * 210)
        y = 430 + int(math.sin(math.radians(angle)) * 170)
        node(draw, x, y, 34, p[angle // 90])
        draw.line([(1250, 430), (x, y)], fill=line_color(p[2]), width=6)


def docs(draw, p):
    rr(draw, (130, 185, 570, 675), fill=blend(p[1], 0.88), outline=line_color(p[1]), width=6)
    for y in [285, 385, 485, 585]:
        draw.line([(205, y), (485, y)], fill=line_color(p[1]), width=9)
    arrow(draw, (585, 435), (820, 435), line_color(p[3]), 10)
    node(draw, 885, 435, 95, p[3])
    for i, y in enumerate([210, 370, 530]):
        arrow(draw, (980, 435), (1180, y + 55), line_color(p[i]), 8)
        card(draw, 1185, y, 370, 110, p[i], p[2])


def workspace_docs(draw, p):
    rr(draw, (135, 155, 660, 715), fill=blend(p[2], 0.88), outline=line_color(p[2]), width=6)
    for y, c in zip([245, 375, 505], p):
        card(draw, 220, y, 350, 88, c, p[3])
    rr(draw, (840, 190, 1545, 675), fill=blend(p[0], 0.88), outline=line_color(p[0]), width=6)
    for x in [930, 1120, 1310]:
        for y in [290, 460]:
            card(draw, x, y, 145, 100, p[(x + y) % 4], p[2])
    arrow(draw, (665, 435), (830, 435), line_color(p[1]), 10)


def database(draw, p):
    for y in [200, 360, 520]:
        card(draw, 145, y, 330, 115, p[(y // 100) % 4], p[3])
        arrow(draw, (485, y + 58), (760, 440), line_color(p[(y // 100) % 4]), 8)
    for i, y in enumerate([300, 430, 560]):
        draw.ellipse((760, y - 55, 1100, y + 55), fill=blend(p[2], 0.72), outline=line_color(p[2]), width=6)
        if i < 2:
            draw.rectangle((760, y, 1100, y + 130), fill=blend(p[2], 0.72), outline=line_color(p[2]), width=6)
    for y in [265, 425, 585]:
        arrow(draw, (1110, 440), (1275, y), line_color(p[1]), 8)
        card(draw, 1280, y - 55, 305, 110, p[1], p[0])


def cloud(draw, p):
    node(draw, 300, 420, 90, p[3])
    for angle in range(0, 360, 45):
        node(draw, 300 + int(math.cos(math.radians(angle)) * 130), 420 + int(math.sin(math.radians(angle)) * 95), 35, p[angle // 90])
    arrow(draw, (450, 420), (760, 420), line_color(p[3]), 10)
    rr(draw, (760, 240, 1010, 610), fill=blend(p[0], 0.75), outline=line_color(p[0]), width=7)
    for x, y, c in [(1200, 190, p[1]), (1400, 310, p[2]), (1215, 510, p[3]), (1450, 610, p[1])]:
        arrow(draw, (1015, 420), (x, y + 55), line_color(c), 8)
        card(draw, x, y, 210, 110, c, p[0])


def template(draw, p):
    xs = [150, 455, 760, 1065, 1370]
    for i, x in enumerate(xs):
        card(draw, x, 335, 230, 150, p[i % 4], p[(i + 1) % 4])
        if i:
            arrow(draw, (x - 85, 410), (x - 15, 410), line_color(p[i % 4]), 8)
    for i, x in enumerate(xs):
        node(draw, x + 115, 590, 30, p[(i + 2) % 4])
        draw.line([(x + 115, 485), (x + 115, 560)], fill=line_color(p[(i + 2) % 4]), width=7)


def registration(draw, p):
    rr(draw, (150, 175, 605, 690), fill=blend(p[0], 0.88), outline=line_color(p[0]), width=6)
    for y in [260, 365, 470, 575]:
        draw.rounded_rectangle((225, y, 525, y + 55), radius=14, fill=(255, 253, 248), outline=line_color(p[0]), width=3)
    for i, (x, y) in enumerate([(790, 230), (1040, 230), (790, 505), (1040, 505)]):
        card(draw, x, y, 210, 130, p[(i + 1) % 4], p[0])
    for target in [(790, 295), (1040, 295), (790, 570), (1040, 570)]:
        arrow(draw, (610, 435), target, line_color(p[3]), 7)
    rr(draw, (1320, 250, 1580, 615), fill=blend(p[2], 0.82), outline=line_color(p[2]), width=6)
    for y in [330, 430, 530]:
        node(draw, 1380, y, 24, p[1])
        draw.line([(1430, y), (1535, y)], fill=line_color(p[2]), width=9)
    arrow(draw, (1250, 435), (1310, 435), line_color(p[2]), 8)


DRAWERS = {
    "culture": culture,
    "protocol": protocol,
    "server_bridge": server_bridge,
    "client": client,
    "transport": transport,
    "sdk": sdk,
    "access_gate": access_gate,
    "repo": repo,
    "vcs": vcs,
    "chat": chat,
    "browser_actions": browser_actions,
    "browser_control": browser_control,
    "devtools": devtools,
    "code_nav": code_nav,
    "docs": docs,
    "workspace_docs": workspace_docs,
    "database": database,
    "cloud": cloud,
    "template": template,
    "registration": registration,
}


def finish(image: Image.Image, entry_id: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    raw = image.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))
    raw.save(OUT_DIR / f"{entry_id}_base_raw.png")
    final = raw.resize(FINAL_SIZE, Image.Resampling.LANCZOS)
    final.save(OUT_DIR / f"{entry_id}_base_1254x627.png")


def main() -> int:
    for index, (entry_id, variant) in enumerate(ENTRIES):
        image, draw, palette = base(index)
        DRAWERS[variant](draw, palette)
        finish(image, entry_id)
        print(f"wrote {entry_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
