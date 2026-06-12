import pandas as pd
import streamlit as st


def render_workflow_table(workflows):

    st.markdown(
        """
        <div class="workflow-card">
        </div>
        """,
        unsafe_allow_html=True
    )

    df = pd.DataFrame(workflows)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=350
    )

    st.markdown("")
