import streamlit as st
import pandas as pd
import plotly.express as px
from utils import set_background

st.set_page_config(
    page_title="Employee Overview",
    page_icon="👥",
    layout="wide"
)

set_background("images/hr_background.jpg")

@st.cache_data
def load_data():
    return pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

df = load_data()

st.title("👥 Employee Overview")

st.markdown("### Workforce Demographics & Employee Distribution")

# Gender Distribution
st.subheader("👨‍💼 Gender Distribution")

fig = px.pie(
    df,
    names="Gender",
    title="Gender Distribution"
)

fig.update_layout(
    height=320,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# Age Distribution
st.subheader("🎂 Age Distribution")

fig = px.histogram(
    df,
    x="Age",
    nbins=20,
    title="Employee Age Distribution"
)

fig.update_layout(
    height=320,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# Marital Status
st.subheader("💍 Marital Status")

fig = px.bar(
    df["MaritalStatus"].value_counts().reset_index(),
    x="MaritalStatus",
    y="count",
    title="Marital Status Distribution"
)

fig.update_layout(
    height=320,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(fig, use_container_width=True)