# Week 1 – Git & GitHub + AI Coding Agents

## Goal
Get comfortable with the day-to-day git/GitHub workflow and start using AI coding
agents (Copilot, Claude, etc.) as a self-help tool for the rest of the internship.

## Schedule

| Session | Format | Focus |
|---|---|---|
| Day 1-2 | Self-study | Learn git basics on your own, get to know the team |
| Day 3 | With mentor | Real git task: clone this repo, branch, add your log, open a PR |
| Day 4 | With mentor | Merge conflict exercise |
| Day 5 | Meeting | Review, questions, wrap-up |

## Day 1-2 — Self-study

- Git fundamentals: [learngitbranching.js.org](https://learngitbranching.js.org) — interactive, go through at least the "Introduction Sequence" and "Push & Pull" levels
- GitHub flow: read GitHub's own guide on branches and pull requests (search "GitHub flow" in GitHub Docs)
- AI coding agents: go through the quickstart for whichever tool you'll use (GitHub Copilot or Claude Code) and try it on a few small things — ask it to explain a function, write a short script, explain an error message

## Day 3 — Real task: your first PR

1. Clone this repository
2. Create a new branch for yourself
3. Add your log entry for this week under `logs/w1/`
4. Commit, push, and open a pull request
5. Mentor reviews and merges (or asks for one small change first)

## Day 4 — Merge conflict exercise

Mentor will set up a deliberate conflict (two branches editing the same line).
You resolve it, with the mentor watching and explaining as you go.

## Day 5 — Wrap-up meeting

Review the week, answer open questions, preview Week 2 (machine learning fundamentals).

---

## Alper's Log
*(append your notes below as you go — what you did, what was confusing, what you'd want explained again)*


**1-2. Gün (Kendine Çalışma):**
Git'in temel mantığını öğrendim: working directory, staging area ve commit kavramlarını 
`git add` ve `git commit` komutlarıyla pratik ederek anladım. Ayrıca kendi bilgisayarımda 
yerel bir Git deposu oluşturup (`git init`) GitHub'a bağlayarak (`git remote add`, `git push`) 
ilk push işlemimi de gerçekleştirdim.

Öğrendiğim komutlar:
- `git init` — yeni bir depo başlatma
- `git add` — değişiklikleri staging alanına ekleme
- `git commit -m "mesaj"` — değişiklikleri kalıcı olarak kaydetme
- `git status` — depo durumunu kontrol etme
- `git remote add origin <url>` — yerel depoyu GitHub'a bağlama
- `git push` — commit'leri GitHub'a gönderme
- `git checkout -b <branch-adı>` — yeni bir branch oluşturup geçiş yapma
- `git branch` — mevcut branch'leri ve aktif olanı görme

Kafamı biraz karıştıran nokta: bilgisayarımda "Masaüstü" aslında OneDrive üzerinden 
senkronize edildiği için (`OneDrive\Desktop`), dosya konumlarını bulmakta biraz zorlandım. 
Bunu çözerek dosya sistemi ve terminal komutlarını (cd, dir) daha iyi kavradım.

**3. Gün (Bu depo üzerinde çalışma):**
Bu depoyu klonladım (`git clone`), kendi adıma `alper-w1-log` adında bir branch oluşturdum 
(`git checkout -b alper-w1-log`) ve bu haftanın günlüğünü `logs/w1/w1_tasks.md` dosyasına ekledim.
