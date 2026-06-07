import streamlit as st
import pandas as pd
from services.workflow_service import WorkflowService


def render_delayed_orders():

    st.title("🚚 Delayed Orders")

    data = WorkflowService.delayed_orders_page_data()

    df = pd.DataFrame(data)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Total Delayed Orders", len(df))

    with c2:
        st.metric(
            "Avg Delay",
            f"{round(df['Days Delayed'].mean(),1)} Days"
        )

    with c3:
        st.metric(
            "Escalated",
            len(df[df["Status"] == "Escalated"])
        )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )