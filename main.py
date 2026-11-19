#!/usr/bin/env python3
"""Sum up 19 November 2026's world news in one image.

Deterministic, offline generator for the make.fun bounty
"Sum up 19 November's world news in one image"
(https://make.fun/bounty/news-image-20261119).

Writes exactly one image to /output/entry.png. No network access,
no randomness, no timestamps: two runs produce identical bytes.

News basis (19 Nov 2026, cross-checked across Horizon, OneTurn and
FeedCast daily briefs of that date):
- Trump, Xi and Putin hold their first trilateral summit in Shenzhen
  (APEC sidelines); Ukraine and nuclear arms top the agenda.
- Gulf war widens: Iran strikes Gulf states after US strikes on
  Qeshm; a tanker is hit near the Strait of Hormuz; the IEA calls
  the Hormuz crisis the greatest threat yet to energy security.
- COP31 in Antalya enters its final stretch deadlocked; the draft
  text admits holding warming to 1.5C is no longer obtainable.
- The International Court of Justice rules on the Rohingya genocide
  case brought by Gambia against Myanmar.
- Anthropic prices a record IPO at $83/share ahead of its Nasdaq
  debut.
- Also: Ukraine hits the Crimean Bridge for the third time in a
  week; turmoil in Bangladesh; a Van Gogh sells for a record
  $190.4M.
"""

import os

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
OUT = "/output/entry.png"

PAPER = (247, 243, 234)
INK = (18, 18, 20)
RED = (178, 34, 44)
GOLD = (201, 148, 26)
BLUE = (31, 78, 140)
TEAL = (14, 116, 110)
GREEN = (22, 120, 62)
GREY = (92, 90, 84)

FONT_CANDIDATES_BOLD = [
    "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
]
FONT_CANDIDATES_REG = [
    "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
]


def font(size, bold=True):
    paths = FONT_CANDIDATES_BOLD if bold else FONT_CANDIDATES_REG
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        trial = (cur + " " + w_).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, xy, text, fnt, fill, max_w, leading=1.16):
    x, y = xy
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y


def panel(draw, box, accent):
    x0, y0, x1, y1 = box
    draw.rectangle(box, fill=(255, 255, 255), outline=INK, width=3)
    draw.rectangle([x0, y0, x1, y0 + 14], fill=accent)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead -------------------------------------------------
    d.rectangle([0, 0, W, 118], fill=INK)
    d.text((40, 18), "THE WORLD IN ONE PICTURE", font=font(34), fill=PAPER)
    d.text((40, 62), "Thursday  ·  19 November 2026", font=font(30, bold=False),
           fill=(212, 205, 188))

    # ---- Hero: Shenzhen trilateral summit -------------------------
    panel(d, [32, 142, 992, 470], RED)
    d.text((56, 174), "SHENZHEN SUMMIT", font=font(30), fill=RED)
    d.text((56, 212), "TRUMP · XI · PUTIN", font=font(62), fill=INK)
    # Country discs, right of the headline, clear of the body text
    discs = [("USA", BLUE), ("CHINA", RED), ("RUSSIA", (90, 110, 160))]
    cx = 706
    for label, col in discs:
        d.ellipse([cx, 196, cx + 76, 272], fill=col, outline=INK, width=3)
        tw = d.textlength(label, font=font(17))
        d.text((cx + 38 - tw / 2, 224), label, font=font(17), fill=(255, 255, 255))
        cx += 84
    text_block(
        d, (56, 300),
        "The US, Chinese and Russian presidents meet face to face "
        "for the first time ever. Ukraine, nuclear arms and the "
        "Iran war top the agenda.",
        font(30, bold=False), INK, 880)
    d.text((56, 428), "APEC FORUM  ·  SHENZHEN, CHINA", font=font(22), fill=GREY)

    # ---- Middle row -----------------------------------------------
    panel(d, [32, 494, 504, 756], GOLD)
    d.text((56, 528), "GULF WAR WIDENS", font=font(33), fill=INK)
    text_block(
        d, (56, 574),
        "Iran strikes Gulf states after US attacks on Qeshm. A "
        "tanker is hit near the Strait of Hormuz. The IEA calls it "
        "the greatest threat ever to energy security.",
        font(26, bold=False), INK, 424)

    panel(d, [520, 494, 992, 756], TEAL)
    d.text((544, 528), "COP31 DEADLOCK", font=font(33), fill=INK)
    text_block(
        d, (544, 574),
        "Climate talks in Antalya enter their final days, still "
        "deadlocked. The draft text admits holding warming to "
        "1.5°C is no longer obtainable.",
        font(26, bold=False), INK, 424)

    # ---- Bottom row -----------------------------------------------
    panel(d, [32, 780, 504, 936], BLUE)
    d.text((56, 810), "WORLD COURT RULES", font=font(30), fill=INK)
    text_block(
        d, (56, 852),
        "The ICJ decides the Rohingya genocide case: "
        "Gambia v. Myanmar.",
        font(25, bold=False), INK, 424)

    panel(d, [520, 780, 992, 936], GREEN)
    d.text((544, 810), "AI'S RECORD IPO", font=font(30), fill=INK)
    text_block(
        d, (544, 852),
        "Anthropic prices its debut at $83 a share ahead of its "
        "Nasdaq listing.",
        font(25, bold=False), INK, 424)

    # ---- Footer ----------------------------------------------------
    d.rectangle([0, 952, W, 1024], fill=INK)
    d.text((40, 962),
           "Also today: Ukraine hits the Crimean Bridge a 3rd time this week ·",
           font=font(22, bold=False), fill=PAPER)
    d.text((40, 990),
           "Bangladesh in turmoil · Van Gogh sells for a record $190.4M",
           font=font(22, bold=False), fill=PAPER)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
