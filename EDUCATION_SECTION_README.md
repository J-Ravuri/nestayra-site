# Nestayra Education Section

This version adds a password-protected Education section to the Nestayra static site.

Password:
Shauri11Plus

Main file changed:
index.html

The education area includes:
- 11 Plus Education section
- Password gate
- 11 Plus Galaxy Obby demo game
- Original practice questions
- A-E answer buttons
- Score, coins, streaks and lives

Important:
The embedded public game uses original demo questions. It does not copy GL paper content or images.

## Test locally

From this folder:

python3 -m http.server 5173

Open:

http://localhost:5173/#education

## Check in to GitHub

git status
git add index.html EDUCATION_SECTION_README.md
git commit -m "Add password-protected education section"
git push origin main

Your hosting should redeploy automatically if nestayra.co.uk is connected to GitHub Pages or another GitHub deployment.
