import streamlit as st
import pandas as pd
import plotly.express as px
from utils import set_background

st.set_page_config(
    page_title="Job Role Analysis",
    page_icon="💼",
    layout="wide"
)

set_background("images/hr_background.jpg")

@st.cache_data
def load_data():
    return pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

df = load_data()

st.title("💼 Job Role Analysis")

st.markdown("### Employee Distribution & Attrition by Job Role")

# Employee Count by Job Role
st.subheader("👥 Employees by Job Role")

job_count = df["JobRole"].value_counts().reset_index()
job_count.columns = ["Job Role", "Employees"]

fig = px.bar(
    job_count,
    x="Job Role",
    y="Employees",
    text="Employees",
    title="Employees by Job Role"
)

fig.update_layout(
    height=320,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# Attrition by Job Role
st.subheader("📉 Attrition by Job Role")

job_attrition = df[df["Attrition"] == "Yes"]["JobRole"].value_counts().reset_index()
job_attrition.columns = ["Job Role", "Attrition Count"]

fig = px.bar(
    job_attrition,
    x="Job Role",
    y="Attrition Count",
    text="Attrition Count",
    title="Attrition by Job Role"
)

fig.update_layout(
    height=320,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# Average Income by Job Role
st.subheader("💰 Average Monthly Income by Job Role")

income = df.groupby("JobRole")["MonthlyIncome"].mean().reset_index()

fig = px.bar(
    income,
    x="JobRole",
    y="MonthlyIncome",
    title="Average Monthly Income by Job Role"
)

fig.update_layout(
    height=320,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(fig, use_container_width=True)