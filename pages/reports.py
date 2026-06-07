import streamlit as st
from services.report_service import ReportService


def render_reports():

    st.title("📊 Reports")

    weekly = ReportService.weekly_report()

    monthly = ReportService.monthly_report()

    c1, c2 = st.columns(2)

    with c1:

        st.subheader("Weekly Report")

        st.json(weekly)

    with c2:

        st.subheader("Monthly Report")

        st.json(monthly)

    st.download_button(
        "Download Report",
        data=str(monthly),
        file_name="report.txt"
    )