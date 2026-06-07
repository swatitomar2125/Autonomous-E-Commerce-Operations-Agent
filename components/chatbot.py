import streamlit as st


def render_chatbot():

    # --------------------------------------------------
    # INITIALIZE DYNAMIC SESSIONS
    # --------------------------------------------------
    # Active panel view state
    if "active_tab" not in st.session_state:
        st.session_state.active_tab = "AI Assistant"

    # Live active chat conversation
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [
            {
                "role": "User", 
                "time": "10:23 AM", 
                "msg": "Find delayed orders and escalate critical ones."
            },
            {
                "role": "Agent", 
                "time": "10:23 AM", 
                "msg": "Sure, I will fetch delayed orders, analyze severity based on SLA policy, and escalate critical cases."
            }
        ]

    # Persistent log archive for the Query History view
    if "query_history" not in st.session_state:
        st.session_state.query_history = [
            {"title": "🔍 Scan Zone-3 Transit Backlog", "date": "Yesterday"},
            {"title": "📊 Generate May SLA Performance Audit", "date": "2 days ago"},
            {"title": "📦 Safety Stock Pipeline Analysis", "date": "1 week ago"}
        ]

    # --------------------------------------------------
    # DYNAMIC RENDER PIPELINE
    # --------------------------------------------------
    
    # 1. Custom Tab Navigation Header
    # Instead of plain HTML text, we use Streamlit columns to make the tab headers clickable!
    tab_col1, tab_col2 = st.columns(2)
    
    with tab_col1:
        # Accent background if active, normal if idle
        if st.button("✨ AI Assistant", use_container_width=True, key="btn_tab_ai", 
                     type="primary" if st.session_state.active_tab == "AI Assistant" else "secondary"):
            st.session_state.active_tab = "AI Assistant"
            st.rerun()

    with tab_col2:
        if st.button("⏱️ Query History", use_container_width=True, key="btn_tab_history", 
                     type="primary" if st.session_state.active_tab == "Query History" else "secondary"):
            st.session_state.active_tab = "Query History"
            st.rerun()

    st.html("<hr style='border-color: #1f2937; margin: 10px 0;'>")

    # --------------------------------------------------
    # VIEW CONTENT SWITCHER
    # --------------------------------------------------
    
    if st.session_state.active_tab == "AI Assistant":
        # Greeting Block
        st.html("""
        <div style="margin-bottom: 16px;">
            <div style="font-size: 16px; font-weight: bold; color: #ffffff; margin-bottom: 4px;">👋 Hi Admin!</div>
            <div style="font-size: 13px; color: #9ca3af; line-height: 1.4;">
                I'm your E-Commerce Operations Agent. How can I help you today?
            </div>
        </div>
        """)

        # Render Active Chat Thread
        for message in st.session_state.chat_messages:
            meta = f"{message['role']} · {message['time']}"
            card_style = "background: #2563eb; color: white; margin-left: 15%;" if message["role"] == "User" else "background: #1f2937; color: #e5e7eb; border: 1px solid #374151;"
            
            st.html(f"""
            <div style="{card_style} padding: 12px; border-radius: 10px; font-size: 13px; line-height: 1.4; margin-bottom: 10px;">
                <div style="font-size: 11px; color: #9ca3af; margin-bottom: 4px;">{meta}</div>
                <div>{message['msg']}</div>
            </div>
            """)

        # Workflow Execution Step-Tracker Status Box (as seen in mockup screenshot)
        st.html("""
        <div style="background: #0f172a; border: 1px solid #1e293b; border-radius: 10px; padding: 12px; margin-top: 15px;">
            <div style="font-size: 11px; font-weight: bold; color: #94a3b8; margin-bottom: 8px; text-transform: uppercase;">⚙️ Workflow Started</div>
            <div style="display: flex; flex-direction: column; gap: 6px; font-size: 12px; color: #cbd5e1;">
                <div style="display: flex; justify-content: space-between;"><span>🟢 Planner Agent</span> <span style="color: #10b981;">Completed</span></div>
                <div style="display: flex; justify-content: space-between;"><span>🟢 Database Agent</span> <span style="color: #10b981;">Completed</span></div>
                <div style="display: flex; justify-content: space-between;"><span>🟢 Policy (RAG) Agent</span> <span style="color: #10b981;">Completed</span></div>
                <div style="display: flex; justify-content: space-between;"><span>🔵 Report Agent</span> <span style="color: #3b82f6; animation: pulse 2s infinite;">In Progress</span></div>
            </div>
        </div>
        """)

        # Input box form at bottom
        with st.form(key="chat_input_form", clear_on_submit=True):
            user_query = st.text_input("", placeholder="Ask anything...", label_visibility="collapsed")
            submit_button = st.form_submit_button("Send Response ✈️", use_container_width=True, type="primary")
            
            if submit_button and user_query.strip():
                st.session_state.chat_messages.append({"role": "User", "time": "Just Now", "msg": user_query})
                st.session_state.chat_messages.append({"role": "Agent", "time": "Just Now", "msg": "Understood. Accessing relevant metric modules..."})
                st.rerun()

    # --------------------------------------------------
    # QUERY HISTORY VIEW MODE
    # --------------------------------------------------
    elif st.session_state.active_tab == "Query History":
        st.html("""
        <div style="margin-bottom: 12px; font-size: 13px; color: #9ca3af;">
            Review previously executed analysis queries:
        </div>
        """)
        
        for item in st.session_state.query_history:
            st.html(f"""
            <div style="background: #111827; border: 1px solid #1f2937; padding: 12px; border-radius: 8px; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center;">
                <div style="font-size: 13px; color: #f3f4f6; font-weight: 500;">{item['title']}</div>
                <div style="font-size: 11px; color: #6b7280;">{item['date']}</div>
            </div>
            """)