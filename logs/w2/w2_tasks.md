# Week 2 – Machine Learning Fundamentals (Supervised & Unsupervised)

## Goal

This week is about **intuition, not implementation**. You do not need to write any
ML code, study the math, or learn a framework (scikit-learn, etc.) this week.

As an AI Engineer working in an agent-first world, the day-to-day skill is knowing
*which kind of algorithm fits a problem* and *how to judge whether a result makes
sense* — not deriving the math or hand-coding the algorithm. So for every algorithm
below, the goal is to be able to answer: what is it doing, when would I reach for
it, and when would it fail me?

## Schedule

| Session | Format | Focus |
|---|---|---|
| Day 1 | Self-study | Classification: Naive Bayes, KNN |
| Day 2 | Self-study | Regression: Linear Regression, Decision Trees |
| Day 3 | Self-study | Clustering: K-Means, supervised vs. unsupervised recap |
| Day 4 | Self-study | Comparison exercise + use your AI agent to self-quiz |
| Day 5 | Meeting | Discuss answers, clarify confusion, preview Week 3 |

## Day 1 — Classification

### Naive Bayes
- **Intuition:** uses Bayes' theorem to estimate the probability of each class given the input features, assuming the features don't influence each other ("naive").
- **Reach for it when:** text/spam-style classification, you need a fast, cheap baseline, or you have limited data.
- **Watch out for:** the independence assumption is almost never really true — it still often works fine anyway, but it struggles when features are strongly correlated.
- **Resource:** StatQuest (Josh Starmer) — search "StatQuest Naive Bayes" on YouTube. Very clear, no heavy math, ~15 min.

### K-Nearest Neighbors (KNN)
- **Intuition:** to classify a new point, look at its `k` closest neighbors in the training data and take a majority vote. There's no real "training" step.
- **Reach for it when:** the decision boundary is irregular/non-linear and you want something simple and interpretable on small-to-medium datasets.
- **Watch out for:** gets slow and unreliable as data size and number of features grow (curse of dimensionality); sensitive to feature scaling.
- **Interactive:** Stanford's CS231n kNN demo — search "cs231n knn demo". You place points on a 2D plane, change `k`, and watch the decision regions change live. Best way to build real intuition for this one.

## Day 2 — Regression

### Linear Regression
- **Intuition:** fits the straight line (or plane) through the data that minimizes prediction error.
- **Reach for it when:** you need a fast, interpretable baseline for predicting a number, and the relationship looks roughly linear. The coefficients directly tell you "how much does the prediction change per unit of this feature."
- **Watch out for:** can't capture curved/non-linear relationships, and is sensitive to outliers.
- **Resource:** StatQuest — search "StatQuest Linear Regression".

### Decision Trees
- **Intuition:** repeatedly splits the data with yes/no questions on features, aiming for purer and purer groups at each split.
- **Reach for it when:** you want something interpretable (you can literally read the tree as a set of rules), and your data mixes feature types or has non-linear relationships.
- **Watch out for:** left to grow freely, they overfit — memorize the training data instead of generalizing.
- **Interactive:** r2d3.us — "A Visual Introduction to Machine Learning" (Part 1 and Part 2). A scroll-through visual explainer that builds a decision tree in front of you and shows overfitting happening. One of the best ML-intuition resources on the web, genuinely worth the full read for both parts.

## Day 3 — Clustering (Unsupervised)

### K-Means
- **Intuition:** given a chosen number of groups `k`, repeatedly (1) assign each point to its nearest center, (2) recompute each center as the average of its assigned points, until things stop changing.
- **Reach for it when:** you don't have labels and want to discover natural groupings — e.g. customer segmentation, grouping similar log entries.
- **Watch out for:** you have to choose `k` yourself, it assumes roughly round/blob-shaped clusters, and the result depends on where the centers start out.
- **Interactive:** naftaliharris.com/blog/visualizing-k-means-clustering — drop your own points on a canvas and step through the algorithm one iteration at a time. Excellent for seeing exactly why initialization matters.

### Supervised vs. unsupervised — recap
Write a couple of sentences in your log: what's the actual difference in *what you're given* (labels or not) and *what you get out* (a prediction vs. a grouping)?

## Day 4 — Comparison exercise + use your AI agent

Use the AI agent skills from Week 1 here — this *is* the exercise, not a shortcut around it.
Ask Claude/Copilot things like:
- "Explain [algorithm] to me like I'm new to ML, with a real-world example."
- "Give me 3 situations where you'd pick KNN over Naive Bayes, and 3 where you'd pick the opposite."
- "Quiz me with 3 questions on the difference between linear regression and decision trees."

Then, in your own words (no need for code, a few sentences is enough), answer in your log:
1. KNN vs. Naive Bayes for classification — when would you pick one over the other?
2. Linear Regression vs. Decision Tree for regression — when does each one fail?
3. Given a brand-new dataset with no labels, how would you decide whether clustering is even the right approach?

## Day 5 — Wrap-up meeting

Walk through your answers together, clear up anything confusing, and preview Week 3
(a small project that puts these ideas into practice).

---

## Alper's Log
*(append your notes below as you go — what you did, what was confusing, what you'd want explained again)*
