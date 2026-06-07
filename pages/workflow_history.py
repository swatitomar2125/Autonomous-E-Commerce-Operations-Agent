import streamlit as st
import pandas as pd
from services.workflow_service import WorkflowService


def render_workflow_history():

    st.title("📜 Workflow History")

    data = WorkflowService.generate_workflows(
        count=50
    )

    df = pd.DataFrame(data)

    search = st.text_input(
        "Search Workflow"
    )

    if search:

        df = df[
            df["Workflow Name"]
            .str.contains(
                search,
                case=False
            )
        ]

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=600
    )