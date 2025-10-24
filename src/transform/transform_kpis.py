from pathlib import Path
import pandas as pd

RAW = Path("data/raw")
PROC = Path("data/processed"); PROC.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(RAW/"patients.csv", parse_dates=["visit_date"])
df["is_readmit"] = (df["outcome"].str.lower() == "readmit").astype(int)
df["is_improved"] = (df["outcome"].str.lower() == "improved").astype(int)

kpi_by_dx = (
    df.groupby("diagnosis_code", as_index=False)
      .agg(patients=("patient_id","count"),
           readmit_rate=("is_readmit","mean"),
           improve_rate=("is_improved","mean"))
      .sort_values("patients", ascending=False)
)
kpi_by_dx.to_csv(PROC/"kpi_by_diagnosis.csv", index=False)

kpi_daily = (
    df.groupby(df["visit_date"].dt.date, as_index=False)
      .agg(visits=("patient_id","count"),
           readmits=("is_readmit","sum"),
           improves=("is_improved","sum"))
)
kpi_daily.to_csv(PROC/"kpi_daily.csv", index=False)

df.to_csv(PROC/"patients_enriched.csv", index=False)
print("[transform] wrote:", PROC/"kpi_by_diagnosis.csv", "and", PROC/"kpi_daily.csv")
