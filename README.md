# downtime-analytics-pipeline

End-to-end downtime analytics pipeline using Python, SQL, and ETL to compute reliability KPIs (MTBF/MTTR) and failure-mode insights for operational systems.



\# Downtime Analytics Pipeline (ETL + SQL + KPIs)



A portable data engineering project that simulates equipment downtime events, runs ETL + data quality checks, loads data into SQLite, and produces reliability KPIs (MTBF, MTTR, Availability) and failure-mode insights.



\## Why this matters

This mirrors real manufacturing/logistics analytics:

\- ingest event logs

\- clean + validate data

\- load into a database

\- compute reliability KPIs for ops and engineering



\## Quickstart

pip install -r requirements.txt

python src/generate\_data.py

python src/etl.py

python src/quality\_checks.py

python src/load\_sqlite.py

python src/kpi\_report.py



\## Results (local run)

\- Generated 4,000 synthetic downtime events

\- Cleaned to 3,986 valid events after data quality filters

\- Loaded events into SQLite (`data/processed/downtime.db`)

\- Produced KPI output (`outputs/kpi\_summary.csv`) with 15 aggregated rows (line × failure\_code)



\### Sample KPI output (top rows)

Example (your run may vary):

\- LINE\_A — JAM: 522 events, 9,615.8 total downtime minutes, MTBF ≈ 1.56 hours

\- LINE\_A — BELT\_SLIP: 418 events, 7,713.4 total downtime minutes, MTBF ≈ 1.56 hours

\- LINE\_B — JAM: 378 events, 6,588.6 total downtime minutes, MTBF ≈ 2.08 hours



