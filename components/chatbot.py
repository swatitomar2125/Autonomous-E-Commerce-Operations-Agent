# AI Assistant Panel — now with Voice Input + Voice Output


import streamlit as st
from components.voice_assistant import render_voice_input, speak_text, render_voice_status


def render_chatbot():

    # --------------------------------------------------
    # INITIALIZE SESSION STATE
    # --------------------------------------------------

    if "active_tab" not in st.session_state:
        st.session_state.active_tab = "AI Assistant"

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

    if "query_history" not in st.session_state:
        st.session_state.query_history = [
            {"title": "🔍 Scan Zone-3 Transit Backlog",         "date": "Yesterday"},
            {"title": "📊 Generate May SLA Performance Audit",  "date": "2 days ago"},
            {"title": "📦 Safety Stock Pipeline Analysis",      "date": "1 week ago"}
        ]

    # New: track whether voice mode is enabled
    if "voice_mode" not in st.session_state:
        st.session_state.voice_mode = False

    # New: track last agent reply (so TTS knows what to speak)
    if "last_agent_reply" not in st.session_state:
        st.session_state.last_agent_reply = ""

    # --------------------------------------------------
    # TAB NAVIGATION
    # --------------------------------------------------

    tab_col1, tab_col2 = st.columns(2)

    with tab_col1:
        if st.button(
            "✨ AI Assistant",
            use_container_width=True,
            key="btn_tab_ai",
            type="primary" if st.session_state.active_tab == "AI Assistant" else "secondary"
        ):
            st.session_state.active_tab = "AI Assistant"
            st.rerun()

    with tab_col2:
        if st.button(
            "⏱️ Query History",
            use_container_width=True,
            key="btn_tab_history",
            type="primary" if st.session_state.active_tab == "Query History" else "secondary"
        ):
            st.session_state.active_tab = "Query History"
            st.rerun()

    st.html("<hr style='border-color: #1f2937; margin: 10px 0;'>")

    # --------------------------------------------------
    # AI ASSISTANT TAB
    # --------------------------------------------------

    if st.session_state.active_tab == "AI Assistant":

        #  Header row: greeting + voice toggle 
        header_left, header_right = st.columns([2, 1])

        with header_left:
            st.html("""
            <div style="margin-bottom: 10px;">
                <div style="font-size:16px; font-weight:bold; color:#ffffff; margin-bottom:2px;">
                    👋 Hi Admin!
                </div>
                <div style="font-size:12px; color:#9ca3af;">
                    E-Commerce Operations Agent
                </div>
            </div>
            """)

        with header_right:
            # Voice ON/OFF toggle button
            voice_label = "🔇 Voice" if st.session_state.voice_mode else "🔊 Voice"
            voice_type  = "primary"   if st.session_state.voice_mode else "secondary"

            if st.button(voice_label, key="voice_toggle_btn", type=voice_type, use_container_width=True):
                st.session_state.voice_mode = not st.session_state.voice_mode
                st.rerun()

        #  Voice status indicator 
        if st.session_state.voice_mode:
            render_voice_status(is_speaking=False)
            st.markdown("<br>", unsafe_allow_html=True)

        #  Chat message thread 
        for message in st.session_state.chat_messages:
            meta       = f"{message['role']} · {message['time']}"
            card_style = (
                "background:#2563eb; color:white; margin-left:15%;"
                if message["role"] == "User"
                else "background:#1f2937; color:#e5e7eb; border:1px solid #374151;"
            )
            st.html(f"""
            <div style="{card_style} padding:12px; border-radius:10px;
                         font-size:13px; line-height:1.4; margin-bottom:10px;">
                <div style="font-size:11px; color:#9ca3af; margin-bottom:4px;">{meta}</div>
                <div>{message['msg']}</div>
            </div>
            """)

        #  Workflow step tracker 
        st.html("""
        <div style="background:#0f172a; border:1px solid #1e293b; border-radius:10px;
                    padding:12px; margin-top:10px; margin-bottom:14px;">
            <div style="font-size:11px; font-weight:bold; color:#94a3b8;
                        margin-bottom:8px; text-transform:uppercase;">⚙️ Workflow Status</div>
            <div style="display:flex; flex-direction:column; gap:6px; font-size:12px; color:#cbd5e1;">
                <div style="display:flex; justify-content:space-between;">
                    <span>🟢 Planner Agent</span> <span style="color:#10b981;">Completed</span>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span>🟢 Database Agent</span> <span style="color:#10b981;">Completed</span>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span>🟢 Policy (RAG) Agent</span> <span style="color:#10b981;">Completed</span>
                </div>
                <div style="display:flex; justify-content:space-between;">
                    <span>🔵 Report Agent</span>
                    <span style="color:#3b82f6;">In Progress</span>
                </div>
            </div>
        </div>
        """)

        #  TTS: speak last agent reply if voice mode on 
        # This fires whenever a new agent reply was added
        if st.session_state.voice_mode and st.session_state.last_agent_reply:
            speak_text(st.session_state.last_agent_reply)
            st.session_state.last_agent_reply = ""   # reset so it doesn't repeat

        # ==================================================
        # INPUT SECTION — Text OR Voice
        # ==================================================

        st.markdown(
            "<div style='font-size:12px; color:#64748B; margin-bottom:6px;'>"
            "TYPE or USE VOICE below</div>",
            unsafe_allow_html=True
        )

        #  Text input form 
        with st.form(key="chat_input_form", clear_on_submit=True):
            user_query   = st.text_input(
                "",
                placeholder="Type a message...",
                label_visibility="collapsed"
            )
            send_clicked = st.form_submit_button(
                "Send ✈️",
                use_container_width=True,
                type="primary"
            )

            if send_clicked and user_query.strip():
                _handle_new_message(user_query.strip())

        #  Voice input (only shown when voice mode is ON) 
        if st.session_state.voice_mode:
            st.markdown(
                "<div style='font-size:12px; color:#64748B; "
                "margin-top:8px; margin-bottom:4px;'>— or speak —</div>",
                unsafe_allow_html=True
            )

            spoken = render_voice_input()

            if spoken:
                st.success(f"🎤 You said: **{spoken}**")
                _handle_new_message(spoken)

    # --------------------------------------------------
    # QUERY HISTORY TAB
    # --------------------------------------------------

    elif st.session_state.active_tab == "Query History":
        st.html("""
        <div style="margin-bottom:12px; font-size:13px; color:#9ca3af;">
            Previously executed analysis queries:
        </div>
        """)

        for item in st.session_state.query_history:
            st.html(f"""
            <div style="background:#111827; border:1px solid #1f2937;
                        padding:12px; border-radius:8px; margin-bottom:8px;
                        display:flex; justify-content:space-between; align-items:center;">
                <div style="font-size:13px; color:#f3f4f6; font-weight:500;">{item['title']}</div>
                <div style="font-size:11px; color:#6b7280;">{item['date']}</div>
            </div>
            """)


# 
# HELPER — adds user message + generates agent reply
# Called by both text form and voice input
# 

def _handle_new_message(user_text: str):
    """
    Appends the user message and a mock agent reply to the chat,
    saves the agent reply for TTS, then reruns the page.
    """
    from datetime import datetime
    now = datetime.now().strftime("%I:%M %p")

    # Add user message
    st.session_state.chat_messages.append({
        "role": "User",
        "time": now,
        "msg":  user_text
    })

    # Generate a simple agent reply
    # Later your team will replace this with actual agent logic
    agent_reply = _generate_agent_reply(user_text)

    st.session_state.chat_messages.append({
        "role": "Agent",
        "time": now,
        "msg":  agent_reply
    })

    # Save for TTS to speak (only used if voice mode is ON)
    st.session_state.last_agent_reply = agent_reply

    # Add to query history
    st.session_state.query_history.insert(0, {
        "title": f"🔍 {user_text[:45]}{'...' if len(user_text) > 45 else ''}",
        "date":  "Just Now"
    })

    st.rerun()


def _generate_agent_reply(query: str) -> str:
    """
    Simple keyword-based reply generator.
    Your team's AI agents will replace this function later.
    """
    q = query.lower()

    if any(word in q for word in ["delay", "delayed", "late"]):
        return "Fetching delayed orders from the database. Found 47 delayed shipments. 12 are critical and have been escalated to the Logistics Team."

    elif any(word in q for word in ["complaint", "refund", "return"]):
        return "Analysing complaint data. 23 open refund complaints found. 5 are high priority. Initiating resolution workflow."

    elif any(word in q for word in ["sla", "violation", "breach"]):
        return "SLA audit running. 18 violations detected this week. Majority in the Shipping department. Report being generated."

    elif any(word in q for word in ["inventory", "stock", "alert"]):
        return "Inventory check complete. 8 SKUs are below safety threshold. Reorder recommendations sent to warehouse."

    elif any(word in q for word in ["report", "summary", "weekly", "monthly"]):
        return "Generating operations report. This will include order metrics, complaint trends, and SLA performance. Ready in 30 seconds."

    else:
        return f"Understood: '{query}'. Processing your request across relevant agent modules. Results will appear shortly."