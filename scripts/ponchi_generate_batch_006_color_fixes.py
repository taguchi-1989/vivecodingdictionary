#!/usr/bin/env python3
"""Rebuild selected ponchi-batch-006 bases with the strict ponchi palette."""
from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw


OUT_DIR = Path("assets/ponchi/experiments/batches/ponchi-batch-006")
SIZE = (1254, 627)

WHITE = (255, 255, 255)
PAPER = (247, 249, 252)
BLACK = (26, 26, 26)
GRAY = (107, 114, 128)
BLUE_1 = (234, 241, 251)
BLUE_2 = (214, 230, 250)
BLUE_3 = (141, 183, 232)
BLUE_4 = (63, 127, 209)
NAVY = (18, 62, 130)


def rr(draw: ImageDraw.ImageDraw, box, fill, outline=GRAY, width=3, radius=18) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def arrow(draw: ImageDraw.ImageDraw, start, end, color=BLUE_4, width=5) -> None:
    draw.line([start, end], fill=color, width=width)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    size = width * 3.0
    left = (end[0] - size * math.cos(angle - 0.45), end[1] - size * math.sin(angle - 0.45))
    right = (end[0] - size * math.cos(angle + 0.45), end[1] - size * math.sin(angle + 0.45))
    draw.polygon([end, left, right], fill=color)


def node(draw: ImageDraw.ImageDraw, x: int, y: int, r: int, fill=BLUE_1, outline=BLUE_4) -> None:
    draw.ellipse((x - r, y - r, x + r, y + r), fill=fill, outline=outline, width=3)


def page() -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", SIZE, WHITE)
    draw = ImageDraw.Draw(image)
    for x in range(0, SIZE[0], 40):
        draw.line([(x, 185), (x, SIZE[1])], fill=BLUE_1, width=1)
    for y in range(200, SIZE[1], 40):
        draw.line([(0, y), (SIZE[0], y)], fill=PAPER, width=1)
    return image, draw


def small_line_stack(draw: ImageDraw.ImageDraw, x: int, y: int, widths: list[int], color=GRAY) -> None:
    for index, width in enumerate(widths):
        yy = y + index * 22
        draw.line([(x, yy), (x + width, yy)], fill=color, width=4)


def draw_imagen() -> Image.Image:
    image, draw = page()

    rr(draw, (42, 135, 235, 505), BLUE_1, NAVY, 4)
    small_line_stack(draw, 72, 175, [120, 92, 138, 106], NAVY)
    for y in [290, 350, 410]:
        rr(draw, (70, y, 205, y + 46), WHITE, BLUE_4, 3, 14)
        node(draw, 96, y + 23, 10, BLUE_2, BLUE_4)
        draw.line([(118, y + 23), (185, y + 23)], fill=GRAY, width=3)

    arrow(draw, (242, 320), (315, 320), BLUE_4, 6)
    rr(draw, (320, 210, 520, 445), PAPER, NAVY, 4)
    for i, (x, y) in enumerate([(380, 270), (450, 270), (415, 335), (365, 390), (470, 390)]):
        node(draw, x, y, 18, BLUE_2 if i % 2 else WHITE, BLUE_4)
    for a, b in [((380, 270), (415, 335)), ((450, 270), (415, 335)), ((415, 335), (365, 390)), ((415, 335), (470, 390))]:
        draw.line([a, b], fill=BLUE_3, width=4)
    draw.arc((350, 240, 490, 410), 205, 335, fill=BLUE_4, width=5)

    arrow(draw, (528, 320), (610, 320), BLUE_4, 6)
    for index, (x, y) in enumerate([(630, 195), (830, 195), (630, 390), (830, 390)]):
        rr(draw, (x, y, x + 160, y + 130), WHITE, BLUE_4 if index == 0 else GRAY, 4)
        draw.rectangle((x + 22, y + 24, x + 138, y + 88), fill=BLUE_1, outline=BLUE_3, width=3)
        draw.polygon([(x + 28, y + 88), (x + 72, y + 48), (x + 106, y + 88)], fill=BLUE_2, outline=BLUE_4)
        node(draw, x + 120, y + 44, 11, BLUE_3, BLUE_4)
        draw.line([(x + 28, y + 108), (x + 132, y + 108)], fill=GRAY, width=4)

    rr(draw, (1025, 255, 1165, 500), PAPER, GRAY, 3)
    for y in [305, 360, 415, 470]:
        draw.rectangle((1055, y - 16, 1085, y + 16), fill=BLUE_2, outline=BLUE_4, width=2)
        draw.line([(1100, y), (1140, y)], fill=NAVY, width=4)
    arrow(draw, (992, 360), (1020, 360), BLUE_3, 5)

    draw.line([(95, 570), (1110, 570)], fill=BLUE_3, width=5)
    for x in [95, 315, 520, 790, 1020, 1110]:
        node(draw, x, 570, 15, WHITE, BLUE_4)
    return image


def draw_alphago() -> Image.Image:
    image, draw = page()

    rr(draw, (60, 155, 365, 470), PAPER, NAVY, 4)
    for offset in range(0, 9):
        x = 90 + offset * 32
        y = 185 + offset * 32
        draw.line([(x, 185), (x, 440)], fill=GRAY, width=2)
        draw.line([(90, y), (345, y)], fill=GRAY, width=2)
    for x, y, fill in [(154, 249, BLACK), (250, 249, WHITE), (218, 313, BLUE_4), (122, 377, BLACK), (282, 377, WHITE)]:
        node(draw, x, y, 12, fill, BLACK if fill == WHITE else fill)

    arrow(draw, (370, 310), (445, 310), BLUE_4, 6)
    rr(draw, (450, 115, 655, 500), WHITE, BLUE_4, 4)
    for index, y in enumerate([165, 225, 285, 345, 405]):
        node(draw, 510, y, 18, BLUE_2 if index % 2 else WHITE, BLUE_4)
        node(draw, 595, y, 18, WHITE if index % 2 else BLUE_2, BLUE_4)
        draw.line([(528, y), (577, y)], fill=BLUE_3, width=4)
        if index:
            draw.line([(510, y - 42), (510, y - 18)], fill=BLUE_3, width=3)
            draw.line([(595, y - 42), (595, y - 18)], fill=BLUE_3, width=3)

    rr(draw, (720, 225, 940, 445), BLUE_1, NAVY, 4)
    for branch, y in enumerate([260, 320, 380]):
        node(draw, 775, y, 16, WHITE, BLUE_4)
        node(draw, 860, y - 24, 14, BLUE_2, BLUE_4)
        node(draw, 860, y + 24, 14, WHITE, GRAY)
        draw.line([(791, y), (846, y - 24)], fill=BLUE_3, width=4)
        draw.line([(791, y), (846, y + 24)], fill=GRAY, width=3)
        if branch == 1:
            arrow(draw, (655, 305), (718, y), BLUE_4, 5)

    rr(draw, (990, 255, 1165, 455), WHITE, BLUE_4, 4)
    draw.line([(1020, 345), (1135, 345)], fill=NAVY, width=5)
    draw.line([(1078, 285), (1078, 425)], fill=NAVY, width=5)
    for x, y in [(1048, 315), (1108, 315), (1048, 375), (1108, 375)]:
        node(draw, x, y, 16, BLUE_2, BLUE_4)

    draw.line([(100, 565), (1110, 565)], fill=BLUE_3, width=5)
    for x in [100, 260, 450, 655, 820, 990, 1110]:
        node(draw, x, 565, 14, WHITE, BLUE_4)
    return image


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    targets = {
        "D-51": draw_imagen,
        "D-60": draw_alphago,
    }
    for entry_id, drawer in targets.items():
        image = drawer()
        out = OUT_DIR / f"{entry_id}_base_1254x627.png"
        image.save(out)
        print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
