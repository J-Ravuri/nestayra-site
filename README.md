# Nestayra Education-Only Portal with Full Game

This site shows only the Education password gate at first.

Password:

```text
Shauri11Plus
```

After unlock it shows:

- Full Education portal
- 11 Plus Education information
- Embedded full multiple-choice no-type game
- Link to open the game full screen

The full game is included in:

```text
education-game/
```

The game direct URL is also guarded with `sessionStorage`, so casual direct access asks users to unlock the Education section first.

---

## Run locally

### 1. Unzip the project

```bash
unzip nestayra-education-only-protected-full-game.zip
cd nestayra-education-only-full-game
```

### 2. Start a local web server

```bash
python3 -m http.server 5173
```

### 3. Open the site

Open this in your browser:

```text
http://localhost:5173
```

### 4. Unlock the Education portal

Enter the password:

```text
Shauri11Plus
```

### 5. Stop the local server

When finished, go back to the terminal and press:

```text
Ctrl + C
```

---

## Run on iPhone on the same Wi-Fi

From the project folder, run:

```bash
python3 -m http.server 5173 --bind 0.0.0.0
```

On Mac, find your local IP:

```bash
ipconfig getifaddr en0
```

If that returns nothing, try:

```bash
ipconfig getifaddr en1
```

On iPhone Safari, open:

```text
http://YOUR-IP-ADDRESS:5173
```

Example:

```text
http://192.168.1.25:5173
```

---

## Check in so it becomes live

Copy the project files into your cloned GitHub repo folder, then run:

```bash
git status
git add .
git commit -m "Add protected education portal with full 11 plus game"
git push origin main
```

If your repo uses `master` instead of `main`, run:

```bash
git push origin master
```

Once pushed, your hosting provider should redeploy automatically if `nestayra.co.uk` is connected to GitHub.

---

## What to check in

For the live website, check in:

```text
index.html
education-game/
README.md
.gitignore
TEST_REPORT.txt
scripts/
source/
```

The most important live files are:

```text
index.html
education-game/index.html
education-game/questions.js
education-game/choice_map.js
README.md
.gitignore
```

Do not check in:

```text
.venv/
node_modules/
__pycache__/
*.pyc
.DS_Store
```

The `.gitignore` file handles these.

---

## Optional: exact PDF-page game setup

You do **not** need Python for GitHub or live deployment.

Python is only needed if you want to generate exact PDF question page images locally. Do not commit the original PDF unless you have permission.

Put your PDF here:

```text
source/GL-Revision-Maths.pdf
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pymupdf pillow
```

Render PDF pages:

```bash
python scripts/render_gl_pages.py
```

Extract A-E choice letters:

```bash
python scripts/extract_choice_letters.py
```

This creates or updates:

```text
education-game/gl-pages/
education-game/choice_map.js
choice_extraction_report.txt
```

After that, run locally again:

```bash
python3 -m http.server 5173
```

Open:

```text
http://localhost:5173
```

---

## Security note

This is front-end password protection for a static website. It is suitable for a simple student/family portal, but not for highly sensitive data.


## Final behaviour required

Before password unlock, the site shows only:

- Nestayra Education header
- one `Education` link
- the password box

No Education portal content, Maths content, English content, or game iframe is visible until the password is entered.

Password:

```text
Shauri11Plus
```

After unlock, the Education portal appears and embeds the full game from:

```text
education-game/index.html
```

The game data includes all selected Maths question sets from:

```text
Paper 1
Paper 2
Paper 3
Paper 4
Paper 5
Paper 6
Paper 7
Paper 8
Paper 9
```

Total selected Maths questions included:

```text
168
```


## Live page cleanup

The PDF setup note has been removed from the live webpage. PDF rendering instructions remain in this README only.


## Game-style front page

The password page has been redesigned as a kid-friendly Galaxy Obby landing screen. The old plain heading text has been removed from the visible page.


## Premium Roblox-style landing

The locked front page has been upgraded into a kid-friendly game landing screen with obby preview, challenge preview, reward cards, avatar previews and a stronger gaming look and feel.


## Final homepage behaviour

The public/home page is intentionally simple. Before password entry it only shows:
- Nestayra Education header
- one Education link
- a clean password form

All gaming visuals, learning content, and the embedded full game appear only after the correct password is entered.


## Multiple-choice answer mapping

The game uses `education-game/choice_map.js` to mark A-E choices.

Each selected question has a `correctLetter`, so clicking A, B, C, D or E is marked against the selected choice letter. It no longer compares the clicked letter against the written answer value such as `30`, `40%` or `£18`.

The `choice_map.js` file stores only correct letters, not copied option text.
