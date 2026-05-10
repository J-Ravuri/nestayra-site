# Nestayra Protected Education Section

This version protects the entire Education section behind a password.

Password:
Shauri11Plus

Main file changed:
index.html

What is included:
- Public site sections: hero, about, services, contact
- Education nav link
- Password gate for the entire Education section
- Hidden education content shown only after password
- Maths game section
- English game section
- A-E multiple-choice answers only
- Score, coins, streaks and lives

Important:
This is front-end protection for a static website. It is suitable for a simple family/student area but not for confidential data.

## Test locally

python3 -m http.server 5173

Open:

http://localhost:5173/#education

Enter:

Shauri11Plus

## Check in to GitHub

git status
git add index.html EDUCATION_SECTION_README.md
git commit -m "Protect education section and add maths and english games"
git push origin main
