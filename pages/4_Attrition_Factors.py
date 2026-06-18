import streamlit as st
import pandas as pd
import plotly.express as px
from utils import set_background

st.set_page_config(
    page_title="Attrition Factors",
    page_icon="📈",
    layout="wide"
)

set_background("images/hr_background.jpg")

@st.cache_data
def load_data():
    return pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

df = load_data()

st.title("📈 Attrition Factors Analysis")

st.markdown("### Factors Influencing Employee Attrition")

# Overtime vs Attrition
st.subheader("⏰ Overtime vs Attrition")

overtime = pd.crosstab(
    df["OverTime"],
    df["Attrition"]
)

fig = px.bar(
    overtime,
    barmode="group",
    title="Overtime Impact on Attrition"
)

fig.update_layout(
    height=320,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# Job Satisfaction
st.subheader("😊 Job Satisfaction vs Attrition")

fig = px.histogram(
    df,
    x="JobSatisfaction",
    color="Attrition",
    barmode="group",
    title="Job Satisfaction Impact"
)

fig.update_layout(
    height=320,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# Work Life Balance
st.subheader("⚖️ Work Life Balance vs Attrition")

fig = px.histogram(
    df,
    x="WorkLifeBalance",
    color="Attrition",
    barmode="group",
    title="Work Life Balance Impact"
)

fig.update_layout(
    height=320,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# Environment Satisfaction
st.subheader("🏢 Environment Satisfaction")

fig = px.histogram(
    df,
    x="EnvironmentSatisfaction",
    color="Attrition",
    barmode="group",
    title="Environment Satisfaction Impact"
)

fig.update_layout(
    height=320,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(fig, use_container_width=True)

