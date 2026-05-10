# Nestayra Education-Only Portal with Full Game

This site shows only the Education password gate at first.

Password:
Shauri11Plus

After unlock it shows:
- Full Education portal
- 11 Plus Education information
- Embedded full multiple-choice no-type game
- Link to open the game full screen

The full game is included in:
education-game/

The game direct URL is also guarded with sessionStorage, so casual direct access asks users to unlock the Education section first.

## Local test

python3 -m http.server 5173

Open:

http://localhost:5173

Enter:

Shauri11Plus

## For the full PDF-page game

Put your PDF here:

source/GL-Revision-Maths.pdf

Install renderer:

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pymupdf pillow

Render pages and choices:

python scripts/render_gl_pages.py
python scripts/extract_choice_letters.py

Then run:

python3 -m http.server 5173

## Check in

git add .
git commit -m "Make education-only protected portal with full game"
git push origin main

## Note

This is front-end password protection for a static website. It is suitable for a simple student/family portal, but not for highly sensitive data.
