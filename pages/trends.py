import streamlit as st
import plotly.express as px

from services.report_service import ReportService


def render_trends():

    st.title("📈 Trends")

    df = ReportService.trend_analysis()

    fig = px.line(
        df,
        x="Month",
        y="Orders",
        markers=True
    )

    fig.update_layout(
        paper_bgcolor="#111827",
        plot_bgcolor="#111827"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(
        df,
        use_container_width=True
    )