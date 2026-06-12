import streamlit as st
from services.report_service import ReportService

def render_ai_insights():
    st.title("🧠 AI Insights")

    insights = ReportService.ai_insights()

    for insight in insights:
        
        card_html = (
            f'<div class="alert-card">'
            f'<h4>AI Recommendation</h4>'
            f'<p>{insight}</p>'
            f'</div>'
        )
        
        st.markdown(card_html, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("Executive Summary")

    st.text_area(
        "",
        value=ReportService.executive_summary(),
        height=250
    )