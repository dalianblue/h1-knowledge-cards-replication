# Replication Package — Distilled Knowledge Cards vs Chunk Retrieval

Replication data and code for:

> **Saying less, being wrong less: distilled knowledge cards versus chunk retrieval for numeric fidelity in a production anesthesia knowledge service**

Pre-registered four-arm controlled experiment embedded in a production clinical anesthesia knowledge service. See `preregistered_protocol_v2.md` for the protocol finalized before any generation run.

## Contents

| Path | Description |
|---|---|
| `question_bank.json` | 45 verbatim reader-submitted clinical questions (5 knowledge strata) |
| `sample_table_strata.json` | Stratified sampling table with pre-registration adjustments |
| `preregistered_protocol_v2.md` | Protocol v2.0 — hypotheses, endpoints, and analysis plan, finalized before execution |
| `answers/arm{1,2,3,C}/` | 174 anonymized answers: bare LLM / distilled-card pipeline / chunk RAG / chunk+schema ablation |
| `scores/` | Claim-level scoring records (GLM-4.6, thinking disabled): supported / wrong / unverifiable per numeric assertion, plus usability & traceability |
| `results_*.json` | Aggregated statistics: four-arm summary, bootstrap CIs, McNemar paired tests, ablation results, P2 improvement A/B, human-evaluation analysis |
| `scripts/` | Figure & table generation code (matplotlib) |
| `quiz/` | Title-level quiz bank and answer key used for examinee-proficiency validity check |

## Reproduction

```bash
# Tables and figures regenerate from deposited scores:
python3 scripts/make_tables.py
# Figures require matplotlib
pip install matplotlib
python3 scripts/fig1_forest.py  # etc.
```

All analyses in the manuscript are repeatable from `scores/`, `results_*.json`, and `scripts/` alone.

## License

Data: CC0. Figures/code: MIT.

## Correspondence

See the manuscript's title page.
