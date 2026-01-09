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

python src/generate_data.py

python src/etl.py

python src/quality_checks.py

python src/load_sqlite.py

python src/kpi_report.py




