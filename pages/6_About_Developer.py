import streamlit as st
from utils import set_background

st.set_page_config(
    page_title="About Developer",
    page_icon="👩‍💻",
    layout="wide"
)

set_background("images/hr_background.jpg")

st.title("👩‍💻 About Developer")

st.markdown("---")

col1, col2 = st.columns([1,3])

with col1:
    st.image("images/bhagi pho.jpeg", width=200)

with col2:
    st.markdown("""
### 👩‍💻 Developer Profile

**Name:** Bhargavi Ravipati

**Role:** Aspiring Data Analyst

**Education:** B.Tech - Computer Science Engineering (CSE)

**Mobile Number:** 9849448216
""")

st.markdown("## 💻 Career Objective")

st.info("""
Aspiring Data Analyst passionate about transforming data into actionable business insights through analytics and visualization.
""")

st.markdown("## ⬇️ Technical Skills")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("""
    ### Programming

    ✔ Python

    ✔ SQL
    """)

with col2:
    st.info("""
    ### Libraries

    ✔ Pandas

    ✔ NumPy
    """)

with col3:
    st.info("""
    ### Visualization

    ✔ Plotly

    ✔ Matplotlib

    ✔ Seaborn
    """)

with col4:
    st.info("""
    ### BI & Dashboard

    ✔ Power BI

    ✔ Streamlit

    ✔ Data Storytelling
    """)

st.markdown("## 📊 Project Skills Demonstrated")

st.write("""
📈 Exploratory Data Analysis

📉 HR Attrition Analysis

📊 Data Visualization

🎯 Business Insights Generation

💻 Interactive Dashboard Development

📂 Data Cleaning & Processing
""")

st.markdown("## 🧰 Tools Used")

st.write("""
• Python

• Pandas

• Plotly

• Streamlit

• IBM HR Analytics Dataset
""")

st.markdown("---")

st.markdown("## 📬 Contact Information")

st.write("📧 Email: bhargaviravipati04@gmail.com")

st.write("🔗 LinkedIn: https://www.linkedin.com/in/bhargavi-ravipati")

st.write("💻 GitHub: https://github.com/bhargavi21220")

st.markdown("---")

st.markdown("---")

st.subheader("🚀 End-to-End Data Analytics Project")

st.success("""
Data Collection ➡ Data Cleaning ➡ Feature Engineering ➡ Exploratory Data Analysis ➡ Data Visualization ➡ Dashboard Development ➡ Business Insights
""")

st.info("""
Built using Python, Plotly, Streamlit, and modern data analytics techniques.
""")

st.markdown("---")

st.caption("Developed by Bhargavi Ravipati | HR Attrition Analysis Dashboard")