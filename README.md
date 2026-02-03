# 🏥 Agentic Hospital AI
### Intelligent Patient Flow, Risk Assessment & Resource Management System

> 🏆 Agentic AI system for real-time hospital triage and resource allocation

---

## 🚀 Overview

**Agentic Hospital AI** is an intelligent, agent-based hospital management system designed to monitor patients in real time, assess clinical risk, allocate beds and doctors, and adapt decisions using feedback.

Unlike static rule-based hospital software or Excel sheets, this system uses **Agentic AI principles** — autonomous agents that reason, act, and learn continuously.

---

## 🎯 Problem Statement

Hospitals face:
- Rapidly changing patient conditions
- ICU and bed shortages
- Manual triage decisions
- Poor real-time visibility
- Non-adaptive Excel-based workflows

---

## 💡 Solution

This system introduces an **Agentic AI workflow** that:

- Dynamically classifies patients as **Emergency, Urgent, or Elective**
- Allocates ICU and General beds in real time
- Tracks hospital capacity live
- Provides LLM-based medical reasoning
- Learns from doctor feedback
- Persists state across restarts

---

## 🧠 Core Features

### 🩺 Patient Risk Assessment
- Risk scoring based on age, condition, and vitals
- Hard safety overrides for critical conditions
- Persistent learning memory

### 🚦 Patient Categorization
| Category | Description |
|--------|------------|
| 🚨 Emergency | Life-threatening, ICU required |
| ⚠️ Urgent | Serious, needs care within hours |
| 🟢 Elective | Stable, routine or deferrable |

Critical conditions can **never** be misclassified as Elective.

---

### 🛏 Hospital Capacity Management
- ICU & General bed tracking
- Live occupancy updates
- Condition & age-group analytics

---

### ⏱ Live Patient Monitoring
- Hourly vitals simulation
- Risk re-evaluation
- Category escalation/downgrade
- History tracking per patient

---

### 🤖 LLM-Powered Reasoning
- Plain-language clinical explanations
- Risk and resource justification
- Safety-first recommendations

Powered by **Groq LLaMA-3.1**.

---

### 👨‍⚕️ Doctor Feedback & Learning
- Human-in-the-loop corrections
- Automatic safety escalation
- Persistent learning across sessions

---

### 💾 Persistent State
All data survives restarts:
- `cleaned_output.csv` – Patient dataset
- `live_patients.json` – Live patient state
- `hospital_state.json` – Bed capacity
- `learning_state.json` – AI learning memory

---

## 🏗 System Architecture

streamlit_app.py → UI & dashboards
app.py → AI agents & hospital logic
CSV / JSON files → Persistent storage
Groq LLM → Reasoning engine


---

## 🛠 Tech Stack
- Python
- Streamlit
- Groq (LLaMA-3.1)
- Pandas
- JSON / CSV storage
- Agentic AI architecture

---

## ▶️ How to Run

```bash
pip install streamlit pandas python-dotenv groq
streamlit run streamlit_app.py
🧪 Example Use Cases
Emergency triage simulation

ICU bed optimization

AI vs doctor decision comparison

Replacing Excel-based hospital workflows

🏆 Why This Is Agentic AI
✔ Autonomous agents
✔ Decision → Action → Feedback loop
✔ Persistent learning
✔ Human oversight
✔ Real-time reasoning

This is decision intelligence, not just prediction.

🔮 Future Enhancements
Discharge workflow

ICU waitlist

Role-based access,

Database backend

Exportable reports

⚠️ Disclaimer
This system is for decision support and simulation only
and does not replace medical professionals.

🙌 Built For
Hackathons · Healthcare AI · Agentic Systems · Operations Research


---

### 5️⃣ SAVE the file (`Ctrl + S`)

---

### 6️⃣ Commit & push

```bash
git add README.md
git commit -m "Improve README formatting and documentation"
git push