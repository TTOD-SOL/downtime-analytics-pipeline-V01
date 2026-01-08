from pathlib import Path
import sqlite3
import pandas as pd

CLEAN = Path("data/processed/downtime_events_clean.csv")
DB = Path("data/processed/downtime.db")

def main():
    df = pd.read_csv(CLEAN, parse_dates=["timestamp"])

    conn = sqlite3.connect(DB)
    df.to_sql("downtime_events", conn, if_exists="replace", index=False)

    # Helpful indexes
    conn.execute("CREATE INDEX IF NOT EXISTS idx_line_asset_time ON downtime_events(line, asset_id, timestamp)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_failure ON downtime_events(failure_code)")
    conn.commit()
    conn.close()

    print(f"✅ Loaded SQLite DB at {DB}")

if __name__ == "__main__":
    main()
