from pathlib import Path
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB = Path("data/processed/downtime.db")
OUT = Path("outputs/kpi_summary.csv")

def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB)

    # MTTR and downtime by failure mode
    q1 = """
    SELECT
      line,
      failure_code,
      COUNT(*) AS events,
      AVG(downtime_minutes) AS avg_downtime_min,
      SUM(downtime_minutes) AS total_downtime_min
    FROM downtime_events
    GROUP BY line, failure_code
    ORDER BY total_downtime_min DESC;
    """
    by_failure = pd.read_sql_query(q1, conn)

    # Approx MTBF per line using event spacing (simple & demo-friendly)
    q2 = """
    SELECT line, timestamp
    FROM downtime_events
    ORDER BY line, timestamp;
    """
    events = pd.read_sql_query(q2, conn, parse_dates=["timestamp"])
    conn.close()

    mtbf_rows = []
    for line, g in events.groupby("line"):
        g = g.sort_values("timestamp")
        diffs = g["timestamp"].diff().dropna().dt.total_seconds() / 3600.0
        mtbf_hours = diffs.mean() if len(diffs) else None
        mtbf_rows.append({"line": line, "mtbf_hours_est": mtbf_hours})

    mtbf = pd.DataFrame(mtbf_rows)

    # Merge and export
    kpi = by_failure.merge(mtbf, on="line", how="left")
    kpi.to_csv(OUT, index=False)
    print(f"✅ KPI summary saved to {OUT}")

    # Optional chart: top 10 downtime causes overall
    top10 = by_failure.groupby("failure_code", as_index=False)["total_downtime_min"].sum() \
                      .sort_values("total_downtime_min", ascending=False).head(10)
    plt.figure()
    plt.bar(top10["failure_code"], top10["total_downtime_min"])
    plt.xticks(rotation=30, ha="right")
    plt.ylabel("Total Downtime (min)")
    plt.title("Top 10 Downtime Causes")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
