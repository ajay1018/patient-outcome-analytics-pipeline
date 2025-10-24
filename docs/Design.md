# System Design — Patient Outcome Analytics

## Goals
- Compute core patient KPIs (readmit & improvement rates) by diagnosis and over time.
- Reproducible local pipeline with clear DE repo structure and CI.

## Data Model (demo)
**Input:** `patients.csv` (patient_id, age, gender, diagnosis_code, outcome, visit_date)  
**Outputs:**  
- `kpi_by_diagnosis.csv` — patients, readmit_rate, improve_rate  
- `kpi_daily.csv` — visits, readmits, improves

## Pipeline
1. **Extract** (`src/extract/extract_local.py`) – reads raw CSV (FHIR/HL7-style stub).
2. **Transform** (`src/transform/transform_kpis.py`) – derives KPIs using pandas.
3. **(Optional) Load** – placeholder for warehouse (Snowflake) loader.

## Orchestration & Quality
- CI runs extract → transform and asserts outputs exist.
- Next: add Airflow DAG & simple data-quality checks (nulls/ranges/dupes).

## Tradeoffs
- Local CSVs keep the demo fast and reproducible.
- Warehouse/dbt are noted for extension but not required to understand the design.

## Runbook
- Install deps: `pip install -r requirements.txt`
- Run: `python src/extract/extract_local.py` → `python src/transform/transform_kpis.py`
- Dashboard: `streamlit run dashboards/app.py`
