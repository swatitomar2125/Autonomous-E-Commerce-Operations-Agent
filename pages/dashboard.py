import streamlit as st
import textwrap  

from services.api_client import MockAPIClient
from services.workflow_service import WorkflowService

from components.kpi_card import render_kpi_cards
from components.charts import render_charts
from components.workflow_table import render_workflow_table


def render_dashboard():

    # ==================================================
    # FETCH MOCK DATA
    # ==================================================

    kpis = MockAPIClient.get_kpis()

    metrics = [
        {
            "icon": "📦",
            "title": "Total Orders",
            "value": f"{kpis['total_orders']:,}",
            "change": "+8.3%",
            "trend": "up",
        },
        {
            "icon": "🚚",
            "title": "Delayed Orders",
            "value": f"{kpis['delayed_orders']:,}",
            "change": "+12.5%",
            "trend": "down",
        },
        {
            "icon": "💬",
            "title": "Open Complaints",
            "value": f"{kpis['complaints']:,}",
            "change": "+4.2%",
            "trend": "up",
        },
        {
            "icon": "⚠️",
            "title": "SLA Violations",
            "value": f"{kpis['sla_violations']:,}",
            "change": "+15.6%",
            "trend": "down",
        },
        {
            "icon": "💰",
            "title": "Pending Refunds",
            "value": f"{kpis['refunds']:,}",
            "change": "+3.1%",
            "trend": "up",
        },
        {
            "icon": "📉",
            "title": "Low Stock Items",
            "value": f"{kpis['inventory_alerts']:,}",
            "change": "+2 New",
            "trend": "down",
        },
    ]

    chart_data = {
        "delayed_orders": MockAPIClient.get_delayed_order_trend(),
        "complaints": MockAPIClient.get_complaints_breakdown(),
        "sla": MockAPIClient.get_sla_data(),
    }

    workflows = WorkflowService.generate_workflows(20)
    agents = MockAPIClient.get_agent_status()
    alerts = MockAPIClient.get_notifications()

    # ==================================================
    # TOP HEADER
    # ==================================================

    left, right = st.columns([5, 2])

    with left:
        st.markdown(
            textwrap.dedent("""
            <div class="dashboard-header">
                <div>
                    <div class="page-title">
                        Welcome, Admin 👋
                    </div>
                    <div class="page-subtitle">
                        Autonomous E-Commerce Operations Agent Platform
                    </div>
                </div>
            </div>
            """),
            unsafe_allow_html=True,
        )

    with right:
        st.text_input("", placeholder="🔍 Search workflows, orders, reports...")

    st.markdown("<br>", unsafe_allow_html=True)

    # ==================================================
    # KPI SECTION
    # ==================================================

    render_kpi_cards(metrics)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==================================================
    # OPERATIONS OVERVIEW HEADER
    # ==================================================

    head1, head2 = st.columns([6, 2])

    with head1:
        st.markdown(
            textwrap.dedent("""
            <h3 style='color:white;'>
            Operations Overview
            </h3>
            """),
            unsafe_allow_html=True,
        )

    with head2:
        period = st.selectbox("", ["Today", "This Week", "This Month"])

    # ==================================================
    # CHARTS
    # ==================================================

    render_charts(chart_data)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==================================================
    # WORKFLOW SECTION
    # ==================================================

    table_col, action_col = st.columns([5, 1])

    with table_col:
        st.markdown(
            textwrap.dedent("""
            <h3 style='color:white;'>
            Recent Workflows Executed
            </h3>
            """),
            unsafe_allow_html=True,
        )

    with action_col:
        st.button("View All", width='stretch') # fixed legacy width param

    render_workflow_table(workflows)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==================================================
    # ALERT CARDS
    # ==================================================

    st.markdown(
        textwrap.dedent("""
        <h3 style='color:white;'>
        Alerts & Priorities
        </h3>
        """),
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            textwrap.dedent(f"""
            <div class="alert-card">
                <div class="kpi-title">
                    Critical Alerts
                </div>
                <div class="alert-value">
                    8
                </div>
                <div class="kpi-change-down">
                    Immediate Action Required
                </div>
            </div>
            """),
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            textwrap.dedent(f"""
            <div class="alert-card">
                <div class="kpi-title">
                    High Priority Tickets
                </div>
                <div class="alert-value">
                    15
                </div>
                <div class="kpi-change-up">
                    +4 Today
                </div>
            </div>
            """),
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            textwrap.dedent(f"""
            <div class="alert-card">
                <div class="kpi-title">
                    Unresolved Complaints
                </div>
                <div class="alert-value">
                    67
                </div>
                <div class="kpi-change-down">
                    Older Than 48 Hours
                </div>
            </div>
            """),
            unsafe_allow_html=True,
        )

    with c4:
        st.markdown(
            textwrap.dedent(f"""
            <div class="alert-card">
                <div class="kpi-title">
                    Reports Generated
                </div>
                <div class="alert-value">
                    24
                </div>
                <div class="kpi-change-up">
                    This Week
                </div>
            </div>
            """),
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ==================================================
    # AGENT STATUS STRIP
    # ==================================================

    st.markdown(
        textwrap.dedent("""
        <h3 style='color:white;'>
        Agent Health
        </h3>
        """),
        unsafe_allow_html=True,
    )

    cols = st.columns(len(agents))

    for col, agent in zip(cols, agents):
        status_icon = {"Healthy": "🟢", "Running": "🟡", "Idle": "⚪"}
        with col:
            st.markdown(
                textwrap.dedent(f"""
                <div class="agent-card">
                    <div style="font-size:18px;">
                        {status_icon.get(agent["status"], "⚪")}
                    </div>
                    <div style="font-weight:600;">
                        {agent["name"]}
                    </div>
                    <div style="color:#94A3B8; font-size:12px;">
                        {agent["status"]}
                    </div>
                </div>
                """),
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

