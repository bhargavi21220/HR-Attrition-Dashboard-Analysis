import streamlit as st
from utils import set_background

st.set_page_config(
    page_title="Insights & Recommendations",
    page_icon="🎯",
    layout="wide"
)

set_background("images/hr_background.jpg")

st.title("🎯 Insights & Recommendations")

st.markdown("### Business Insights Derived from HR Attrition Analysis")

st.success("""
### Key Insights

📌 Research & Development department has the highest employee attrition.

📌 Sales Executives and Laboratory Technicians show significant turnover.

📌 Employees working overtime are more likely to leave.

📌 Low Job Satisfaction increases attrition probability.

📌 Younger employees exhibit higher attrition rates.

📌 Monthly Income influences employee retention.

📌 Work-Life Balance has a strong impact on employee engagement.
""")

st.warning("""
### HR Recommendations

✅ Improve employee engagement programs.

✅ Reduce excessive overtime.

✅ Conduct regular satisfaction surveys.

✅ Create career growth opportunities.

✅ Introduce employee recognition programs.

✅ Enhance work-life balance initiatives.

✅ Review compensation and benefits structure.
""")

st.info("""
### Business Benefits

✔ Reduced Attrition Cost

✔ Improved Employee Retention

✔ Better Workforce Planning

✔ Higher Employee Satisfaction

✔ Increased Organizational Productivity
""")

st.markdown("---")

st.subheader("📌 Project Conclusion")

st.write("""
This HR Attrition Dashboard helps organizations identify
the major factors contributing to employee turnover.

By analyzing employee demographics, departments,
job roles, satisfaction levels, overtime patterns,
and compensation factors, HR teams can take
data-driven decisions to improve retention and
employee experience.
""")

st.markdown("---")

st.caption("HR Attrition Analysis Dashboard | Streamlit Project")