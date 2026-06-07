import streamlit as st

from services.report_service import ReportService


def render_ai_insights():

    st.title("🧠 AI Insights")

    insights = ReportService.ai_insights()

    for insight in insights:

        st.markdown(
            f"""
            <div class="alert-card">

                <h4>
                    AI Recommendation
                </h4>

                <p>
                    {insight}
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.subheader(
        "Executive Summary"
    )

    st.text_area(
        "",
        value=ReportService.executive_summary(),
        height=250
    )