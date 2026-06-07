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

    # c1, c2, c3, c4 = st.columns(4)

    # with c1:
    #     st.metric(
    #         "Completed",
    #         "132"
    #     )

    # with c2:
    #     st.metric(
    #         "Running",
    #         "11"
    #     )

    # with c3:
    #     st.metric(
    #         "Failed",
    #         "3"
    #     )

    # with c4:
    #     st.metric(
    #         "Success Rate",
    #         "97.8%"
    #     )