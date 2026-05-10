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


## English comprehension game

The protected Education portal now includes an English comprehension section:

```text
education-game/english-comprehension.html
```

It is embedded after unlock and guarded by the same Education password session.

The game uses the uploaded ReadQuest comprehension information and teaches:
- Retrieval
- Inference
- Vocabulary in context
- Main idea
- Writer's effect
- Writer's view
- Evidence-based answering

The child reads passage cards, uses hints, answers multiple-choice questions, fights boss rounds, earns XP/gems, and sees skill feedback.


## English comprehension suite upgrade

The Education portal now includes every uploaded English comprehension/learning resource:

```text
education-game/english/readquest.html
education-game/english/gl-technique-dojo.html
education-game/english/peter-pan-comprehension.html
education-game/english/11plus-english-tutor.html
education-game/english/secret-life-of-english.html
```

The English section includes a selector so the child can switch between:
- ReadQuest Adventure
- GL Technique Dojo
- Peter Pan Practice
- English Tutor
- Word Explorer

The GL Technique Dojo explicitly practises retrieval, inference, vocabulary in context, writer's effect, main idea, evidence, tone/mood and structure.


## iPad and iPhone design upgrade

The portal has been tuned for iPad and iPhone:

- simple password-only home screen
- large touch targets
- mobile quick navigation chips
- responsive study path cards
- responsive Maths and English iframes
- improved iOS safe-area handling
- better game-like dashboard after unlock
- 20-minute test-prep mission flow

Suggested child routine:
1. Maths Sprint
2. ReadQuest passage
3. GL Technique Dojo
4. Review mistakes


## Comprehension Quest Academy

A new protected English game has been added:

```text
education-game/english/comprehension-quest-academy.html
```

It uses the uploaded Pack 1, Pack 2 and Pack 3 answer keys for Practice Papers 1-9. The game focuses on comprehension-style questions and trains the RACE method:

- Read the question
- Analyse the skill type
- Collect evidence
- Eliminate traps

Modes included:
- Training
- Battle
- Boss
- Mistake Lab

The child should keep the original paper/booklet beside the game, read the passage, find proof, then choose A-E/N in the game.


## Comprehension mastery QA upgrade

Comprehension Quest Academy now includes:
- explicit skill lessons for every comprehension skill
- evidence-first habit training
- RACE method reminders
- session summary
- 5-streak celebration
- weak-skill Mistake Lab grouping
- iPhone/iPad friendly cards and touch targets

The game does not copy passage/question text. It uses paper/question references and the uploaded answer-key letters, so the child practises with the original paper beside the game.


## Full Comprehension Pro

The English section now includes:

```text
education-game/english/full-comprehension-pro.html
```

This protected game includes rendered full paper pages for Practice Papers 1-8, answer-key marking, pro technique coaching, evidence-first habit training, zoom/page controls, XP, streaks and Mistake Lab.

The child reads the full paper page inside the game, finds proof, selects the technique, then answers A-E/N.


## Visibility fix for Full Comprehension Pro

Full Comprehension Pro is now shown immediately after unlock, before the Maths iframe, with a large launch card and a direct top navigation link.

Main file:

```text
education-game/english/full-comprehension-pro.html
```

Paper page images:

```text
education-game/english/paper-pages/P1/
...
education-game/english/paper-pages/P8/
```


## Full all-sections version with visible English Pro

This version keeps the previous portal sections, Maths game, and other English games.

It adds a clear Full Comprehension Pro spotlight after unlock and keeps Full Comprehension Pro as the first/default English game.

Main English file:

```text
education-game/english/full-comprehension-pro.html
```


## Comprehension Coach simplification

The Full Comprehension Pro game has been simplified for children.

It is now called Comprehension Coach Game and uses this clearer flow:
1. Read the question
2. Find proof on the page
3. Learn the simple skill tip
4. Choose A-E/N
5. Check and learn from feedback

Main file remains:

```text
education-game/english/full-comprehension-pro.html
```


## Summary Coach format

The English comprehension game now uses only the requested format:

1. Child reads the comprehension page
2. Child writes what it is about
3. Child writes a short 1-2 sentence summary
4. Child confirms proof
5. Child answers A-E/N

This is designed to improve understanding before answering questions.


## Parent summary guide added

The Summary Coach game now includes parent-friendly model summaries and key points for all Paper 1-8 comprehension passages.

The parent summary card contains only:
- Understanding
- Short summary
- Key points

It is shown before the child writes their own summary, so the parent can check whether the child understood the passage.
