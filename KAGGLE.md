# Kaggle — selected competition work

A dated overview of my Kaggle competitions, notebooks and project methods. **A leaderboard snapshot is not a final rank or a medal.** This page is maintained separately from my one-page admissions CV.

## Competition results

| Competition | Recorded result | Evidence and qualification |
| --- | --- | --- |
| [Predicting Credit Card Fraud — Playground Series S6E11](https://www.kaggle.com/competitions/playground-series-s6e11/leaderboard) | **0.95354 ROC-AUC; #30 / 1,603 ranked entries (~top 1.9%)** | Public leaderboard snapshot on November 12, 2026, corroborated by the applicant's screenshot and the Kaggle leaderboard. **Active competition**; scoring uses ~20% of test data, and the private final standings may change. Submission notebook and pipeline have **not yet been retrieved or verified**. |
| [Predicting Airline Satisfaction — Playground Series S6E10](https://www.kaggle.com/competitions/playground-series-s6e10) | **213th of 3,734 teams (top 5.7%)** | Completed competition, displayed on [my Kaggle competition profile](https://www.kaggle.com/kalidenaiarys/competitions), checked November 11, 2026. The underlying notebook, score, and specific model pipeline have not yet been independently linked to this result. |
| [Spaceship Titanic](https://www.kaggle.com/competitions/spaceship-titanic) | **0.82534 public accuracy; #15 on October 19, 2026; #56 of 2,030 teams on November 12, 2026** | Historical leaderboard screenshot and reproducibility notes in the [project README](https://github.com/aiaryskaliden/Spaceship-Titanic67). A rolling leaderboard may change. |
| [Name That LLM](https://www.kaggle.com/competitions/name-that-llm) | **0.682 public score; #403 of 5,535 teams** | Successful notebook submission, version 1; observed in submission history November 11, 2026. Competition active. |
| [Enveda CASMI 2026](https://www.kaggle.com/competitions/enveda-CASMI26-molecule-id-mass-spectra) | **0.487 public score; #109 of 5,142 teams** | Successful notebook submission, version 1; observed in submission history November 11, 2026. Competition active. |
| [Gemma 4 Developer Agent](https://www.kaggle.com/competitions/gemma-4-developer-agent) | **0.17 public score; #2,234 of 5,427 teams** | Successful submission observed in history November 11, 2026. Competition active; no final standing claimed. |
| [Google Quantum AI — Verifiable Quantum Circuit Compilation](https://www.kaggle.com/competitions/google-verifiable-quantum-circuit-compilation/leaderboard) | **27.30661 public score; #194 displayed** | User-provided Kaggle leaderboard screenshot, **November 14, 2026**. Highlighted entry “Kaliden Aiarys” shows 27.30661 and 16 submissions; previous personal best displayed as 27.29699. Several leaderboard entries show the same score. Snapshot only; no final standing or verified submission-to-code linkage. |

The public quantum notebook documents earlier experiments; its title does not establish the source of the newer 27.30661 submission. Exact submission-to-code mapping is still being verified.

Public leaderboard positions above were observed November 12, 2026, **except Google Quantum AI updated from the user's November 14 screenshot**. They may change before final results.

## Selected public notebooks

- [Spaceship Titanic — TabPFN + CatBoost, LB 0.82534](https://www.kaggle.com/code/kalidenaiarys/spaceship-titanic-tabpfn-catboost-lb-0-82534): tabular features, CatBoost/LightGBM and stacked predictions. **Third-party TabPFN probability files were reused and credited, not retrained.**
- [Google Quantum AI — Circuit Compilation](https://www.kaggle.com/code/kalidenaiarys/24-80179-public-lb-quantum-circuit-compilation): circuit verification and optimization experiments.
- [Titanic Historical Record Linkage](https://www.kaggle.com/code/kalidenaiarys/titanic-historical-record-linkage-1309-verified): deterministic matching against historical data, illustrating target leakage. **Not** a survival-prediction model.
- [PLE Field Lab — Agent Harness Starter](https://www.kaggle.com/code/kalidenaiarys/ple-field-lab-agent-harness-starter): published notebook; no performance claim.
- [CarbonGlobe — Cross-Age LightGBM Baseline](https://www.kaggle.com/code/kalidenaiarys/carbonglobe-cross-age-lightgbm-baseline): published baseline; no leaderboard result claimed.

Other competitions visible on [my Kaggle profile](https://www.kaggle.com/kalidenaiarys/competitions) include Name That LLM, Gemma 4 Developer Agent, and CASMI 2026. Participation alone does not establish a medal or a rank.

## Methods and standards

- Compare against simple baselines and document validation choices and data leakage risks.
- Keep public scores distinct from development-validation scores and final private rankings.
- Attribute reused predictions, notebooks, datasets and pretrained models.
- Explain reproducibility limitations when competition data, hidden tests, or restricted code cannot be distributed.

*Last updated: November 14, 2026 (Google Quantum AI result from user-provided screenshot).*
