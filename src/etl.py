from pathlib import Path
import pandas as pd

RAW = Path("data/raw/downtime_events_raw.csv")
OUT = Path("data/processed/downtime_events_clean.csv")

def main():
    df = pd.read_csv(RAW, parse_dates=["timestamp"])

    # Basic cleaning
    df["asset_id"] = df["asset_id"].astype(str).str.strip()
    df["failure_code"] = df["failure_code"].astype("string")

    # Remove obviously invalid downtime
    df = df[df["downtime_minutes"].notna()]
    df = df[df["downtime_minutes"] > 0]

    # Drop rows missing key fields
    df = df[df["asset_id"].str.len() > 0]
    df = df[df["failure_code"].notna()]

    # Sort for downstream KPI computations
    df = df.sort_values(["line", "asset_id", "timestamp"]).reset_index(drop=True)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False)
    print(f"✅ Clean data written to {OUT} ({len(df)} rows)")

if __name__ == "__main__":
    main()
