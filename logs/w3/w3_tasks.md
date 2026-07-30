# Week 3 – Jupyter, Colab, and the ML Working Style

## Goal

Before touching real TCDD data next week, get comfortable with the *environment*
ML engineers and Data Scientists actually work in day-to-day, and see each Week 2
algorithm run end-to-end, once, on a clean textbook dataset. No exploratory data
analysis, no data cleaning, no tuning this week — that's deliberate. The datasets
below are the classic education-ready ones (Iris, Diabetes — both originally from
the UCI Machine Learning Repository) built directly into scikit-learn, precisely so
there's zero friction between "open notebook" and "see the algorithm work."

## Schedule

| Session | Format | Focus |
|---|---|---|
| Day 1 | Self-study | What is Jupyter / Colab, and why ML work looks different from software engineering |
| Day 2 | Self-study | Run the classification notebooks: Naive Bayes, KNN |
| Day 3 | Self-study | Run the regression notebooks: Linear Regression, Decision Tree |
| Day 4 | Self-study | Run the clustering notebook: K-Means + write up observations |
| Day 5 | Meeting | Walk through all 5 notebooks together, preview Week 4 (real TCDD EDA) |

## Day 1 — Jupyter, Colab, and how ML work differs from software engineering

### What is a Jupyter Notebook, and why does ML use it?
A notebook is a document made of **cells** — some are code, some are text (markdown)
— that you run one at a time, in any order you like, and the output (a number, a
table, a plot) appears right below the cell that produced it.

That's the whole reason it exists: ML and data work is fundamentally **iterative and
exploratory**. You load some data, look at it, try something, look at the result,
change one thing, look again. A notebook lets you keep all your intermediate
results (data previews, charts, model scores) visible on the same page as the code
that made them, instead of re-running an entire program from scratch every time you
change one line — which is how you'd normally work as a software engineer.

### What is Google Colab?
Colab is Google's free, hosted Jupyter environment — it runs in your browser, needs
zero local setup (no Python install, no virtual environments), comes with the
common ML libraries already installed, and even gives free (limited) GPU access.
It's the easiest way to just open a notebook and start running it, which is why
every notebook below has an **"Open in Colab"** badge at the top — click it, and
it opens straight from this GitHub repo into a live, runnable Colab session (you'll
want to save a copy to your own Google Drive so your edits persist).

### How does ML/DS working style differ from software engineering?
Worth internalizing this early, since it explains *why* the tools and habits differ:

- **Exploration vs. construction.** A software engineer usually starts from a fairly
  clear spec and builds toward it. An ML engineer / data scientist often starts by
  not knowing what the data even looks like, and the first hour of work is just
  looking — that's what notebooks are built for.
- **Cells vs. programs.** Notebook code runs cell-by-cell, out of order, with state
  hanging around in memory between runs. This is great for exploration and terrible
  for the reliability guarantees software engineering usually wants (reproducibility,
  "run this from a clean state and get the same result").
- **Evaluation by metric, not pass/fail.** A unit test either passes or fails. A
  model doesn't — you get an accuracy or an error number and have to judge whether
  it's *good enough*, which is a judgment call, not a boolean.
- **Notebooks are for prototyping, not production.** Once an approach is validated
  in a notebook, it usually gets rewritten into proper scripts/pipelines (real
  functions, tests, version control that actually diffs cleanly) before it runs in
  production. Notebooks themselves diff terribly in git — that's a real, known pain
  point, not a limitation you're missing something about.

### Self-check (write in your log)
- In your own words: why does a notebook fit exploratory data work better than a
  regular script would?
- What's one thing about the notebook workflow that would worry you if this code
  were going straight to production?

## Day 2 — Classification notebooks

Run these in Colab (click the badge, save a copy to your Drive) and read the
"what to notice" cell at the end of each one before moving on.

- **Naive Bayes** — [`logs/w3/notebooks/01_naive_bayes.ipynb`](notebooks/01_naive_bayes.ipynb) — Iris dataset
- **KNN** — [`logs/w3/notebooks/02_knn.ipynb`](notebooks/02_knn.ipynb) — Iris dataset, same data as Naive Bayes so you can compare the two directly

## Day 3 — Regression notebooks

Both use the same single feature from the same dataset, on purpose — so you can see
directly how a straight line (Linear Regression) and a step-like split (Decision
Tree) fit the *same* points differently.

- **Linear Regression** — [`logs/w3/notebooks/03_linear_regression.ipynb`](notebooks/03_linear_regression.ipynb) — Diabetes dataset
- **Decision Tree** — [`logs/w3/notebooks/04_decision_tree.ipynb`](notebooks/04_decision_tree.ipynb) — Diabetes dataset

## Day 4 — Clustering notebook + wrap-up

- **K-Means** — [`logs/w3/notebooks/05_kmeans.ipynb`](notebooks/05_kmeans.ipynb) — synthetic blob dataset (generated on the spot, made for teaching clustering)

In your log, write a few sentences per notebook: what did you change (the "try
this" suggestion in each notebook), and what happened when you did?

## Day 5 — Wrap-up meeting

Walk through observations from all 5 notebooks together, answer open questions, and
preview Week 4 — his first real task on the actual TCDD project (EDA on real data).

---

## Alper's Log
*(append your notes below as you go — what you did, what was confusing, what you'd want explained again)*
