🗓️ Day 6 — AI Integration & Intelligent Security Analysis
📌 Overview

Day 6 upgrades the Linux security monitoring system from basic automation to AI-assisted security analysis.

Instead of only counting failed SSH attempts, the system now:

Learns from historical data

Understands normal behavior (baseline)

Detects anomalies

Assigns a meaningful risk score

Produces intelligent security decisions

This makes the project AI + Cybersecurity, not just scripting.

🎯 Objectives

By the end of Day 6, the system is able to:

Analyze historical security logs

Establish baseline SSH behavior

Detect abnormal login activity

Generate a risk score (0–100)

Output AI-style security decisions

No deep learning or heavy ML frameworks are used — the focus is on interpretable, explainable intelligence.

🧠 AI Approach Used

This project follows a logic-driven AI approach, which is acceptable and widely used in security systems.

AI concepts applied:

Baseline behavior modeling

Statistical anomaly detection

Risk scoring

Decision classification

This approach is suitable for:

Hackathons

SIH / AIH

SOC-style security tools

Interviews

🔄 System Flow
Linux SSH Logs
     ↓
security.json (historical records)
     ↓
Baseline calculation
     ↓
Anomaly detection
     ↓
Risk scoring (0–100)
     ↓
AI decision output

🔍 Features Implemented
1️⃣ Historical Log Analysis

Reads past scan data from security.json

Each scan is stored as a single JSON object per line

Enables the system to learn from previous behavior

2️⃣ Baseline Behavior Calculation

Computes the average number of failed SSH login attempts

Represents normal behavior for the system

Used as a reference for detecting abnormal activity

3️⃣ Anomaly Detection

Compares current SSH failures with historical baseline

Detection logic:

current_failed_attempts > baseline × 2


Simple, effective, and explainable

4️⃣ Risk Scoring (0–100)

Security events are converted into a normalized risk score:

Condition	Risk Score
Normal behavior	20
Slight deviation	50
Clear anomaly	80
Severe attack	100

This makes security insights easy to interpret and prioritize.

5️⃣ AI Decision Layer

Based on the risk score, the system generates a high-level decision:

Risk Score	AI Decision
< 30	Normal Behavior
30–69	Suspicious Activity
≥ 70	Potential Attack

This decision acts as the final AI output.

📄 Sample JSON Output
{
  "timestamp": "2026-01-07 12:30:00",
  "user": "kali",
  "failed_ssh_attempts": 12,
  "security_status": "Alert",
  "baseline": 4.5,
  "risk_score": 80,
  "ai_decision": "Potential Attack"
}
