import streamlit as st
import pandas as pd
import plotly.express as px
from utils import set_background

st.set_page_config(
    page_title="Department Analysis",
    page_icon="🏢",
    layout="wide"
)

set_background("images/hr_background.jpg")

@st.cache_data
def load_data():
    return pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

df = load_data()

st.title("🏢 Department Analysis")

st.markdown("### Department-wise Employee & Attrition Analysis")

# Employee Count by Department
st.subheader("👥 Employee Count by Department")

dept_count = df["Department"].value_counts().reset_index()
dept_count.columns = ["Department", "Employees"]

fig = px.bar(
    dept_count,
    x="Department",
    y="Employees",
    text="Employees",
    title="Employees by Department"
)

fig.update_layout(
    height=320,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# Attrition by Department
st.subheader("📉 Attrition by Department")

dept_attrition = df[df["Attrition"] == "Yes"]["Department"].value_counts().reset_index()
dept_attrition.columns = ["Department", "Attrition Count"]

fig = px.bar(
    dept_attrition,
    x="Department",
    y="Attrition Count",
    text="Attrition Count",
    title="Department-wise Attrition"
)

fig.update_layout(
    height=320,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# Department Percentage
st.subheader("📊 Department Distribution")

fig = px.pie(
    df,
    names="Department",
    title="Department Distribution"
)

fig.update_layout(
    height=320,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(fig, use_container_width=True)