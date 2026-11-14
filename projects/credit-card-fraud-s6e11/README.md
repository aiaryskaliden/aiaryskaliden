# Credit Card Fraud Detection — Kaggle Playground Series S6E11

## Kaggle result (November 14, 2026)

**Public ROC-AUC: 0.95390 · Leaderboard position: #38 (snapshot).**

I participated in Kaggle's *Predicting Credit Card Fraud* challenge and tested successive prediction submissions, checked their structure, and compared public scores. My submitted results progressed through **0.95354**, **0.95388**, and **0.95390** ROC-AUC. Screenshots of my Kaggle submission history and highlighted leaderboard entry (“Kaliden Aiarys”, 7 submissions, #38) document the progression as of **November 14, 2026**.

[Competition leaderboard](https://www.kaggle.com/competitions/playground-series-s6e11/leaderboard) · [My Kaggle profile](https://www.kaggle.com/kalidenaiarys)

This is a **public leaderboard snapshot** in an active competition, not a final private-leaderboard ranking. Multiple entries share the displayed 0.95390 score.

## Reproducibility work

I checked the structure of a supplied competition submission archive, `s6e11_submission_v3.zip`, and documented its prediction-file integrity. The included CSV had:

| Check | Verified result |
| --- | --- |
| Rows × columns | 299,984 × 2 |
| Columns | `id`, `is_fraud` |
| IDs | 699960–999943, contiguous and unique |
| Predicted probabilities | Finite values in [0, 1], no missing values |
| CSV SHA-256 | `927e8583e6964a138aeda7c63fcb6995d23115f08764ca02f7a22236d37d925b` |

A small [verification script](verify_submission.py) reproduces the structural checks. This is a validation artifact, not a machine-training notebook.

## Source attribution and limits

The supplied **v3** CSV preserves frozen predictions from a public **daoviet / S6E11 GP & DVAE Orthogonal Apex** dataset. The underlying ensemble was produced by the dataset contributors; the v3 file **was not trained from scratch** by me. The public source is:

https://www.kaggle.com/datasets/daoviet/s6e11-gp-dvae-orthogonal-apex

The provenance note applies to **this particular supplied v3 CSV**. It does not establish which source code generated the newer **0.95390** Kaggle score. The screenshots demonstrate my successful submissions and resulting public scores, but do not on their own prove an independently developed model architecture, training pipeline, or novel algorithm. Those claims require the matching code and experiment log.

The original predictions are not republished here. This page documents my Kaggle result, the progression across submissions, and the reproducible validation step without misattributing third-party model work.

## Next documentation step

Add the exact training / transformation / selection notebook and submission mapping for the **0.95390** result when available, including data sources, validation split, feature processing, comparisons, and limitations.
