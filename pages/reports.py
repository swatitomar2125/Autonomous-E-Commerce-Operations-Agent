import streamlit as st
from services.report_service import ReportService


def render_reports():

    st.title("📊 Reports")

    weekly = ReportService.weekly_report()
    monthly = ReportService.monthly_report()

    st.subheader("Weekly Report")

    cols = st.columns(4)

    items = list(weekly.items())

    for col, (key, value) in zip(cols, items):

        with col:

            st.metric(
                label=key,
                value=value
            )

    st.divider()

    st.subheader("Monthly Report")

    cols = st.columns(4)

    items = list(monthly.items())

    for col, (key, value) in zip(cols, items):

        with col:

            st.metric(
                label=key,
                value=value
            )

    st.download_button(
        "Download Report",
        data=str(monthly),
        file_name="report.txt"
    )