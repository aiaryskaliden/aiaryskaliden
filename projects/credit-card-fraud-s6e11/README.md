# Credit Card Fraud Detection — Kaggle Playground Series S6E11

## Scope and attribution

This portfolio note documents validation of a competition submission for Kaggle Playground Series, Season 6 Episode 11 (credit-card fraud detection).

**Important provenance note:** The supplied `s6e11_submission_v3.zip` contains a single `submission.csv` with frozen predictions originating from the public **daoviet / S6E11 GP & DVAE Orthogonal Apex** Kaggle dataset. These predictions were preserved without retraining; they are **not evidence of an independently trained model**. Credit for the prediction ensemble belongs to the original contributors. The dataset metadata identifies the license as CC0.

- Original source: https://www.kaggle.com/datasets/daoviet/s6e11-gp-dvae-orthogonal-apex
- Competition: https://www.kaggle.com/competitions/playground-series-s6e11
- Source filename: `submission_summit_095370.csv`
- Provided file: `s6e11_submission_v3.zip` containing `submission.csv`
- Original public predictions are not republished in this repository; download the source from Kaggle.

## Submission validation

The supplied CSV was checked locally:

| Check | Result |
| --- | --- |
| Shape | 299,984 rows × 2 columns |
| Columns | `id`, `is_fraud` |
| IDs | 699960–999943, in continuous ascending order, no duplicates |
| Probabilities | Finite, between 0 and 1, no missing values |
| CSV SHA-256 | `927e8583e6964a138aeda7c63fcb6995d23115f08764ca02f7a22236d37d925b` |

You can reproduce these basic file-quality checks with [`verify_submission.py`](verify_submission.py). A valid CSV structure does **not** establish a leaderboard score or originality of modeling.

## Result reporting

The applicant separately reported an earlier **0.95354 public ROC-AUC** and a **#30 / 1,603** leaderboard snapshot (November 12, 2026). These figures have not been independently verified by this repository and should **not** be presented as the score of the supplied frozen v3 file. The v3 archive metadata explicitly indicates that no online submission of that candidate was made.

## Purpose

This page transparently records a reproducibility and provenance check of a Kaggle submission artifact. To document independently authored ML work, this repository should later be expanded with the actual training notebook, feature engineering, train/validation strategy, code, and a verified leaderboard record.
