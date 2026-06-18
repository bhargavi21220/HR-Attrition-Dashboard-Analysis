import streamlit as st
import pandas as pd
import plotly.express as px
from utils import set_background

# ==========================
# PAGE CONFIG (FIRST COMMAND)
# ==========================

st.set_page_config(
    page_title="HR Attrition Dashboard",
    page_icon="👨‍💼",
    layout="wide"
)

# ==========================
# BACKGROUND IMAGE
# ==========================

set_background("")

# ==========================
# LOAD DATA
# ==========================

@st.cache_data
def load_data():
    return pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

df = load_data()

# ==========================
# FILTERS
# ==========================

st.sidebar.header("🔍 Filters")

department = st.sidebar.multiselect(
    "Select Department",
    options=df["Department"].unique(),
    default=df["Department"].unique()
)

gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

attrition = st.sidebar.multiselect(
    "Select Attrition",
    options=df["Attrition"].unique(),
    default=df["Attrition"].unique()
)

filtered_df = df[
    (df["Department"].isin(department)) &
    (df["Gender"].isin(gender)) &
    (df["Attrition"].isin(attrition))
]

# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("👨‍💼 HR Dashboard")

st.sidebar.markdown("---")

st.sidebar.info("""
### HR Attrition Analysis

👥 Employee Overview

🏢 Department Analysis

💼 Job Role Analysis

💰 Income Analysis

😊 Satisfaction Analysis

⚖️ Work-Life Balance

📈 Attrition Drivers

🎯 Insights & Recommendations
""")

# ==========================
# TITLE
# ==========================

st.title("👨‍💼 HR Attrition Analysis Dashboard")

st.markdown("""
### Employee Attrition Analytics & Workforce Insights

Analyze employee attrition patterns, job satisfaction,
work-life balance, salary trends, department performance,
and workforce demographics using IBM HR Analytics Dataset.
""")

st.divider()

st.markdown("""
<style>
[data-testid="metric-container"] {
    background: rgba(0,0,0,0.4);
    border-radius: 12px;
    padding: 10px;
}

[data-testid="metric-container"] label {
    color: white !important;
}

[data-testid="metric-container"] div {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# KPI CARDS
# ==========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👥 Total Employees", len(filtered_df))

with col2:
    st.metric("🚪 Attrition Count",
              len(filtered_df[filtered_df["Attrition"] == "Yes"]))

with col3:
    attrition_rate = round(
        (len(filtered_df[filtered_df["Attrition"] == "Yes"]) / len(filtered_df)) * 100, 2
    )
    st.metric("📉 Attrition Rate", f"{attrition_rate}%")

with col4:
    st.metric("🎂 Average Age",
              round(filtered_df["Age"].mean(), 1))

st.divider()
st.subheader("📌 Project Workflow")

st.success("""
📂 Data Collection

🧹 Data Cleaning

⚙️ Feature Engineering

📊 Exploratory Data Analysis

📈 Data Visualization

🖥️ Dashboard Development

🎯 Business Insights & Recommendations
""")



# ==========================
# DASHBOARD SUMMARY
# ==========================

st.subheader("📈 Dashboard Summary")

col1, col2 = st.columns(2)

with col1:
    st.success("""
    ### Key Findings

    ✅ Attrition Rate Analysis

    ✅ Department Performance

    ✅ Employee Demographics

    ✅ Job Role Trends

    ✅ Satisfaction Analysis
    """)

with col2:
    st.warning("""
    ### Business Impact

    📌 High Attrition increases hiring costs

    📌 Overtime impacts retention

    📌 Satisfaction influences turnover

    📌 Work-life balance affects engagement

    📌 Income impacts employee loyalty
    """)

# ==========================
# DATASET PREVIEW
# ==========================

st.subheader("📊 Dataset Preview")

st.dataframe(
    filtered_df.head(),
    use_container_width=True
)

st.subheader("📥 Download Dataset")

with open("WA_Fn-UseC_-HR-Employee-Attrition.csv", "rb") as file:
    st.download_button(
        label="Click Here to Download Dataset",
        data=file,
        file_name="HR_Attrition_Dataset.csv",
        mime="text/csv"
    )

st.divider()
# ==========================
# ATTRITION DISTRIBUTION
# ==========================

st.subheader("📊 Attrition Distribution")

attrition_counts = filtered_df["Attrition"].value_counts()

fig = px.pie(
    values=attrition_counts.values,
    names=attrition_counts.index,
    title="Employee Attrition Distribution"
)

fig.update_layout(
    height=320,
    margin=dict(l=20, r=20, t=50, b=20)

)

st.plotly_chart(fig, use_container_width=True)



# ==========================
# DEPARTMENT ATTRITION
# ==========================

st.subheader("🏢 Attrition by Department")

dept_attrition = filtered_df[
    filtered_df["Attrition"] == "Yes"
]["Department"].value_counts().reset_index()

dept_attrition.columns = ["Department", "Attrition Count"]

fig = px.bar(
    dept_attrition,
    x="Department",
    y="Attrition Count",
    title="Department-wise Attrition",
    text="Attrition Count"
)

fig.update_layout(
    height=320,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(fig, use_container_width=True)





# ==========================
# GENDER DISTRIBUTION
# ==========================

st.subheader("👨‍💼 Gender Distribution")

gender_counts = filtered_df["Gender"].value_counts()

fig = px.pie(
    values=gender_counts.values,
    names=gender_counts.index,
    title="Gender Distribution"
)

fig.update_layout(
    height=320,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# ==========================
# AGE DISTRIBUTION
# ==========================

st.subheader("🎂 Employee Age Distribution")

fig = px.histogram(
    filtered_df,
    x="Age",
    nbins=20,
    title="Age Distribution"
)

fig.update_layout(
    height=320,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# ==========================
# JOB ROLE ATTRITION
# ==========================

st.subheader("💼 Attrition by Job Role")

job_attrition = filtered_df[
    filtered_df["Attrition"] == "Yes"
]["JobRole"].value_counts().reset_index()

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

# ==========================
# OVERTIME VS ATTRITION
# ==========================

st.subheader("⏰ Overtime vs Attrition")

overtime_data = pd.crosstab(
    filtered_df["OverTime"],
    filtered_df["Attrition"]
)

fig = px.bar(
    overtime_data,
    barmode="group",
    title="Overtime Impact on Attrition"
)

fig.update_layout(
    height=320,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# ==========================
# JOB SATISFACTION
# ==========================

st.subheader("😊 Job Satisfaction")

fig = px.histogram(
    filtered_df,
    x="JobSatisfaction",
    color="Attrition",
    barmode="group",
    title="Job Satisfaction vs Attrition"
)

fig.update_layout(
    height=320,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# ==========================
# MONTHLY INCOME
# ==========================

st.subheader("💰 Monthly Income Distribution")

fig = px.histogram(
    filtered_df,
    x="MonthlyIncome",
    nbins=30,
    title="Monthly Income Distribution"
)

fig.update_layout(
    height=320,
    margin=dict(l=20, r=20, t=50, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# ==========================
# KEY INSIGHTS
# ==========================

st.subheader("🎯 Key Insights")

st.info("""
📌 Research & Development department has significant employee attrition.

📌 Employees working overtime are more likely to leave the company.

📌 Low job satisfaction is strongly associated with attrition.

📌 Certain job roles experience higher employee turnover.

📌 Younger employees tend to show higher attrition rates.

📌 Income and work-life balance influence employee retention.
""")

# ==========================
# PROJECT HIGHLIGHTS
# ==========================

st.subheader("📌 Project Highlights")

st.success("""
✅ 1,470 Employees Analyzed

✅ Attrition Trend Analysis

✅ Department-wise Analysis

✅ Job Role Analysis

✅ Salary & Income Analysis

✅ Satisfaction Analysis

✅ Work-Life Balance Analysis

✅ Business Insights

✅ Interactive Streamlit Dashboard
""")

st.divider()

st.markdown("---")

st.caption(
    "Developed by Bhargavi Ravipati | HR Attrition Analysis Dashboard | Streamlit + Plotly + Python"
)

