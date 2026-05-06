import streamlit as st

import anthropic

if "page" not in st.session_state:
    st.session_state.page = "setup"
if "employee" not in st.session_state:
    st.session_state.employee = {}
if "weekly_updates" not in st.session_state:
    st.session_state.weekly_updates = []

client = anthropic.Anthropic(api_key="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")


# --------- setup page ----------

def page_setup():

    with st.form("Quarterly Goal Setup"):
        goals = st.text_area("Quarterly Goals")
        employee_num = st.text_input("Employee#")
        role = st.text_input("Role")
        location = st.text_input("Location")
        manager = st.text_input("Manager Input")
        quarter = st.selectbox("Quarter", ["Q2 2026", "Q3 2026", "Q4 2026"])

        submitted = st.form_submit_button("Submit")

    if submitted:
        st.session_state.employee = {
            "goals": goals,
            "employee_num": employee_num,
            "role": role,
            "location": location,
            "manager": manager,
            "quarter": quarter
        }
        st.session_state.page = "review"
        st.rerun()

#--------- review page ----------
def page_review():

    e = st.session_state.employee

    if st.button("Back to Setup"):
        st.session_state.page = "setup"
        st.rerun()

    st.title(f"Review for {e['employee_num']}")

    with st.expander("Goals"):
        st.write(e["goals"])

    st.divider()

    st.subheader("Weekly Updates")

    with st.form("Weekly Update"):
        week = st.selectbox("Week", list(range(1, 12)))
        update = st.text_area("What did you accomplish this week?")
        manager_feedback = st.text_area("Manager Feedback")
        add = st.form_submit_button("Add")

    if add and update and manager_feedback:
        st.session_state.weekly_updates.append({
            "week": week,
            "update": update,
            "manager_feedback": manager_feedback
        })
        st.rerun()

    st.divider()

    if st.button("Generate Review Summary for Quarter"):
        if not st.session_state.weekly_updates:
            st.warning("Add at least one weekly update before generating a review.")
        else:
            with st.spinner("Generating your review..."):
                updates_text = "\n\n".join(
                    [f"{u['week']}:\n{u['update']}" for u in st.session_state.weekly_updates]
                )
                prompt = f"""
            You are an HR assistant helping write a quarterly performance review.

            Employee: {e['employee_num']} ({e['role']})
            Quarter: {e['quarter']}

            Employee Goals:
            {e['goals']}

            Weekly Updates:
            {updates_text}

            Write a concise, professional quarterly review covering:
            1. Key achievements this quarter
            2. Progress against goals
            3. Areas for improvement
            4. Recommended focus for next quarter
            """
                response = client.messages.create(
                    model="claude-sonnet-4-6",
                    max_tokens=1000,
                    messages=[{"role": "user", "content": prompt}]
                )
                review_text = response.content[0].text

            st.subheader("Generated Review")
            st.markdown(review_text)
            st.download_button(
                "Download Review",
                data=review_text,
                file_name=f"review_{e['emploayee_num'].replace(' ', '_')}_{e['quarter']}.txt"
            )

if st.session_state.page == "setup":
    page_setup()
else:
    page_review()
