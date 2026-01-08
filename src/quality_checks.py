from pathlib import Path
import pandas as pd

CLEAN = Path("data/processed/downtime_events_clean.csv")

def assert_true(condition: bool, msg: str):
    if not condition:
        raise ValueError(f"❌ Data Quality Check Failed: {msg}")

def main():
    df = pd.read_csv(CLEAN, parse_dates=["timestamp"])

    assert_true(df["event_id"].is_unique, "event_id must be unique")
    assert_true((df["downtime_minutes"] > 0).all(), "downtime_minutes must be > 0")
    assert_true(df["asset_id"].astype(str).str.len().gt(0).all(), "asset_id must be non-empty")
    assert_true(df["failure_code"].notna().all(), "failure_code must not be null")
    assert_true(df["timestamp"].notna().all(), "timestamp must not be null")

    print("✅ All data quality checks passed")

if __name__ == "__main__":
    main()
