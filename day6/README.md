🗓️ Day 6 — Backend Intelligence & Reliability
📌 Overview

Day 6 focuses on upgrading a Linux security monitoring script from basic automation to a more intelligent and reliable backend system.

The system no longer just counts failed SSH attempts.
It now:

Learns from historical data stored in JSON

Establishes baseline system behavior

Detects abnormal deviations

Computes a normalized risk score

Produces a clear decision output

Handles errors safely for long-running execution

The emphasis of this day is backend logic, reliability, and explainability, not machine learning frameworks.

🎯 Learning Objectives

By the end of Day 6, the system can:

Read and process historical log data

Model baseline SSH authentication behavior

Detect anomalies using statistical rules

Translate raw events into a risk score (0–100)

Classify system state using a decision layer

Run safely under automation (cron-friendly)

🧠 Backend Intelligence Approach

Instead of black-box ML, this project uses logic-driven intelligence, which is common in backend monitoring systems.

Concepts applied:

Baseline behavior modeling

Statistical anomaly detection

Risk scoring

Decision classification

Defensive error handling

This approach keeps the system:

Transparent

Easy to debug

Easy to extend later

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
Decision output

🔍 Features Implemented
1️⃣ Historical Log Analysis

Reads past scan results from security.json

Each scan is stored as a single JSON object per line

Corrupted or invalid JSON lines are safely ignored

This enables the system to learn from previous runs.

2️⃣ Baseline Behavior Calculation

Computes the average number of failed SSH attempts

Represents normal behavior for the system

Used as the reference point for detecting anomalies

3️⃣ Anomaly Detection

Compares current SSH failures with historical baseline

Detection rule:

current_failed_attempts > baseline × 2


This method is:

Simple

Explainable

Suitable for backend monitoring tools

4️⃣ Risk Scoring (0–100)

Raw counts are converted into a normalized risk score:

Condition	Risk Score
Normal behavior	20
Slight deviation	50
Clear anomaly	80
Severe spike	100

This allows the backend to reason in terms of severity, not just numbers.

5️⃣ Decision Layer

Based on the risk score, the system classifies the state as:

Risk Score	Decision
< 30	Normal Behavior
30–69	Suspicious Activity
≥ 70	Potential Attack

This acts as the final backend decision output.

6️⃣ Reliability & Error Handling

All subprocess calls are non-blocking (check=False)

Missing files are handled gracefully

JSON parsing errors are ignored safely

Runtime errors are logged to error.log

The script is safe to run repeatedly via cron

This makes the system suitable for unattended execution.

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
