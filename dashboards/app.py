import streamlit as st, pandas as pd

st.set_page_config(page_title="Patient Outcome Analytics", layout="wide")
st.title("🏥 Patient Outcome Analytics")

kpi_by_dx = pd.read_csv("data/processed/kpi_by_diagnosis.csv")
kpi_daily = pd.read_csv("data/processed/kpi_daily.csv")

c1, c2 = st.columns(2)
with c1:
    st.subheader("Patients & Outcomes by Diagnosis")
    st.dataframe(kpi_by_dx, use_container_width=True)
with c2:
    st.subheader("Daily KPIs")
    st.dataframe(kpi_daily, use_container_width=True)

st.caption("Demo data. Replace extract with FHIR/HL7 ingestion and model with dbt later.")
