from pathlib import Path
import numpy as np
import pandas as pd

def main():
    rng = np.random.default_rng(42)
    out_dir = Path("data/raw")
    out_dir.mkdir(parents=True, exist_ok=True)

    n = 4000
    lines = ["LINE_A", "LINE_B", "LINE_C"]
    assets = [f"ASSET_{i:03d}" for i in range(1, 41)]
    failure_codes = ["SENSOR_FAULT", "MOTOR_OVERHEAT", "JAM", "BELT_SLIP", "PLC_RESET"]

    # Random start times over ~120 days
    start = pd.Timestamp("2025-01-01")
    ts = start + pd.to_timedelta(rng.integers(0, 120 * 24 * 60, size=n), unit="m")

    df = pd.DataFrame({
        "event_id": [f"EVT_{i:06d}" for i in range(n)],
        "timestamp": ts,
        "line": rng.choice(lines, size=n, p=[0.45, 0.35, 0.20]),
        "asset_id": rng.choice(assets, size=n),
        "failure_code": rng.choice(failure_codes, size=n, p=[0.20, 0.18, 0.28, 0.22, 0.12]),
        "downtime_minutes": np.clip(rng.gamma(shape=2.2, scale=8.0, size=n), 1, 240).round(1)
    })

    # Inject a small amount of bad data (for quality checks demo)
    bad_idx = rng.choice(df.index, size=20, replace=False)
    df.loc[bad_idx[:8], "downtime_minutes"] = -5
    df.loc[bad_idx[8:14], "failure_code"] = None
    df.loc[bad_idx[14:], "asset_id"] = ""

    df.to_csv(out_dir / "downtime_events_raw.csv", index=False)
    print(f"✅ Wrote {out_dir / 'downtime_events_raw.csv'} with {len(df)} rows")

if __name__ == "__main__":
    main()
