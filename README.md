# Sum up 19 November's world news in one image — make.fun entry

Bounty: https://make.fun/bounty/news-image-20261119
Reward pool: $250 USDC, 50 places paid (1st $50, 2nd $30, 3rd $15,
4th–10th $5, 11th–50th $3). Deadline: Sat Nov 21, 2026, 12:00 AM UTC
(= Nov 21, 08:00 Asia/Taipei).

## What is here

- `main.py` — the entry program (Python 3.13, Pillow only). Offline
  and deterministic: it draws the whole front-page image in code and
  writes it to `/output/entry.png`. Two runs produce identical bytes
  (verified: sha256 eb6ac25f8028f7b2e5355de9ac193dc5d6c8727964f28007a1374ce0cbfebd81).
- `entry-v3.png` — the exact output, for eyeball review before
  submitting. 1024×1024 PNG, 122,197 bytes (limit: 1 MiB).
- `LICENSE` — MIT (OSI-approved, as the brief requires).

## The image

A newspaper front page, "THE WORLD IN ONE PICTURE — Thursday,
19 November 2026":

- Hero: Shenzhen summit — Trump · Xi · Putin, first-ever trilateral
  meeting (APEC sidelines).
- Gulf War Widens — Iran strikes Gulf states, tanker hit near
  Hormuz, IEA energy-security warning.
- COP31 Deadlock — Antalya talks, draft admits 1.5°C out of reach.
- World Court Rules — ICJ Rohingya genocide case, Gambia v. Myanmar.
- AI's Record IPO — Anthropic prices at $83 ahead of Nasdaq debut.
- Footer: Crimean Bridge hit a 3rd time · Bangladesh turmoil ·
  Van Gogh record $190.4M.

News cross-checked 2026-11-19 against Horizon, OneTurn and FeedCast
daily briefs for that date.

## Submission steps (needs Daniel's go)

1. Create a NEW public GitHub repo under Daniel's account (the brief
   requires the repo be created after the competition opened) with
   `main.py`, `LICENSE`, this README.
2. Enter via the Prendclips make.fun account (@prendclips,
   fullvalueai@gmail.com) following make.fun/skill.md, and upload
   the AI coding-agent transcript of the building session with the
   submission, as the brief requires.
3. Up to 10 submissions/day, 20 total; the last one before the
   deadline is the final entry, so there is room to improve the
   image and resubmit.
4. Payouts are USDC on Solana from make.fun's reward wallet; the
   Prendclips account currently has NO Solana wallet connected —
   Daniel connects/claims that himself.
