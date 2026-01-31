import streamlit as st
import pandas as pd
from app import *

st.set_page_config(page_title="Agentic Hospital AI", layout="wide")
st.title("🏥 Agentic AI for Hospital Patient Flow")

# =========================
# LOAD DATASET
# =========================
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_output.csv")

df = load_data()

# =========================
# SESSION STATE INIT
# =========================
for key in ["live_emergency", "live_urgent", "live_elective", "agent_memory"]:
    if key not in st.session_state:
        st.session_state[key] = []

# =========================
# SPLIT DATASET
# =========================
emergency_patients = df[df["Admission Type"] == "Emergency"]
urgent_patients = df[df["Admission Type"] == "Urgent"]
elective_patients = df[df["Admission Type"] == "Elective"]

# =========================
# METRICS
# =========================
st.header("📊 Hospital Load (Dataset)")
c1, c2, c3 = st.columns(3)
c1.metric("🚨 Emergency", len(emergency_patients))
c2.metric("⚠️ Urgent", len(urgent_patients))
c3.metric("🟢 Elective", len(elective_patients))

# =========================
# DATASET MEMBERS
# =========================
st.header("📂 Existing Patients (Dataset)")

with st.expander("🚨 Emergency Patients"):
    st.dataframe(
        emergency_patients[["Name", "Age", "Gender", "Medical Condition"]].head(50)
    )

with st.expander("⚠️ Urgent Patients"):
    st.dataframe(
        urgent_patients[["Name", "Age", "Gender", "Medical Condition"]].head(50)
    )

with st.expander("🟢 Elective Patients"):
    st.dataframe(
        elective_patients[["Name", "Age", "Gender", "Medical Condition"]].head(50)
    )

# =========================
# NEW PATIENT FORM
# =========================
st.header("🧠 New Patient Evaluation")

with st.form("patient_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", 0, 120)
    gender = st.selectbox("Gender", ["Male", "Female"])
    blood = st.selectbox("Blood Type", ["A+", "A-", "B+", "O+"])
    condition = st.text_input("Medical Condition")
    submit = st.form_submit_button("Run Agentic AI")

# =========================
# AGENT EXECUTION
# =========================
if submit and name and condition:
    risk = risk_agent(age, condition)
    resources = resource_agent()
    decision, admit = decision_agent(risk["score"], resources)
    cost = cost_agent(decision)
    confidence = confidence_agent(risk["score"], resources)

    patient = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Condition": condition,
        "Decision": decision,
        "Confidence": confidence
    }

    if decision == "Emergency":
        st.session_state.live_emergency.append(patient)
    elif decision == "Urgent":
        st.session_state.live_urgent.append(patient)
    else:
        st.session_state.live_elective.append(patient)

    explanation = llm_explanation({
        "Patient": patient,
        "Risk": risk,
        "Resources": resources,
        "Cost": cost,
        "Confidence": confidence
    })

    st.session_state.agent_memory.append({
        "patient": patient,
        "decision": decision,
        "confidence": confidence,
        "risk": risk,
        "feedback": None,
        "revised_decision": None
    })

    st.success("Decision Completed")
    st.subheader("✅ Final Decision")
    st.json({
        "Admission": decision,
        "Admit": admit,
        "Confidence": confidence,
        "Cost": cost
    })

    st.subheader("🤖 LLM Reasoning")
    st.markdown(explanation)

# =========================
# LIVE PATIENT GROUPS
# =========================
st.header("📋 Live Patients (Agent Decisions)")
c1, c2, c3 = st.columns(3)

c1.subheader("🚨 Emergency")
c1.dataframe(st.session_state.live_emergency)

c2.subheader("⚠️ Urgent")
c2.dataframe(st.session_state.live_urgent)

c3.subheader("🟢 Elective")
c3.dataframe(st.session_state.live_elective)

# =========================
# FEEDBACK + RE-EVALUATION
# =========================
st.header("🧠 Doctor Feedback & Reflection")

if st.session_state.agent_memory:
    idx = len(st.session_state.agent_memory) - 1
    record = st.session_state.agent_memory[idx]

    feedback = st.radio("Was the last decision correct?", ["Correct", "Incorrect"])

    if st.button("Save Feedback"):
        record["feedback"] = feedback

        if feedback == "Incorrect":
            revised, reason = reflection_agent(
                record["decision"],
                record["risk"],
                record["confidence"]
            )
            record["revised_decision"] = revised

            reflection_text = llm_reflection_explanation({
                "Original Decision": record["decision"],
                "Revised Decision": revised,
                "Reason": reason,
                "Patient": record["patient"]
            })

            st.warning("🔄 Decision Re-Evaluated")
            st.subheader("🆕 Revised Decision")
            st.json({
                "Revised Admission": revised,
                "Reason": reason
            })

            st.subheader("🧠 Reflection Explanation")
            st.markdown(reflection_text)

# =========================
# MEMORY VIEW
# =========================
st.header("🧠 Agent Memory Log")
st.json(st.session_state.agent_memory)

