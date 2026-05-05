import streamlit as st
from ReviewAssist import summary, extract_followup

# --------- SESSION STATE ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "followup_question" not in st.session_state:
    st.session_state.followup_question = None


# --------- UI ----------
st.title("Performance Review Assistant")

goals = st.text_area("Quarterly Goals")
employee = st.text_area("Employee Details")


# --------- STEP 1: GENERATE ----------
if st.button("Generate Review"):
    st.session_state.messages = []
    st.session_state.followup_question = None

    user_input = f"Goals:\n{goals}\n\nEmployee:\n{employee}"

    st.session_state.messages.append({"role": "user", "content": user_input})

    response = summary(st.session_state.messages)

    st.session_state.messages.append({"role": "assistant", "content": response})

    st.session_state.followup_question = extract_followup(response)


# --------- DISPLAY OUTPUT ----------
for msg in st.session_state.messages:
    if msg["role"] == "assistant":
        # Strip the FOLLOW_UP line from display so it doesn't show raw
        display_text = msg["content"].split("FOLLOW_UP:")[0].strip()
        st.markdown(display_text)


# --------- STEP 2: FOLLOW-UP ----------
if st.session_state.followup_question:
    st.markdown("### Additional Information Needed")
    st.write(st.session_state.followup_question)

    # Store in session state to survive reruns
    if "follow_input" not in st.session_state:
        st.session_state.follow_input = ""

    follow_input = st.text_area("Your response", key="follow_input")

    if st.button("Submit Additional Info"):
        st.session_state.messages.append({"role": "user", "content": follow_input})

        response = summary(st.session_state.messages)

        st.session_state.messages.append({"role": "assistant", "content": response})

        st.session_state.followup_question = extract_followup(response)
