# Day 3 – SSH Log Analysis & Threat Detection (Python Backend)

This project is part of my Python backend and cybersecurity learning journey.
Day 3 focuses on analyzing real Linux SSH authentication logs to detect
suspicious login activity.

The goal is to understand how SOC (Security Operations Center) systems
monitor authentication events and raise alerts based on failed login attempts.

---

## 🔍 What This Script Does

- Reads real SSH authentication logs from the system
- Detects failed SSH login attempts
- Counts the number of failed password attempts
- Classifies system security status as:
  - Normal
  - Warning
  - Alert

---

## 🛠 Concepts Used

- Linux SSH authentication logs
- `journalctl -u ssh`
- Python `subprocess.run()`
- Handling command output (`stdout`, `returncode`)
- Output parsing using `splitlines()`
- Conditional logic for threat classification
- Basic SOC-style alert thresholds

---

## 🚨 Threat Detection Logic

The script applies simple security rules:

- **< 5 failed attempts** → Normal
- **5–9 failed attempts** → Warning
- **≥ 10 failed attempts** → Alert

These thresholds simulate basic intrusion detection logic used in SOC tools.

---

## 📂 File Included

- `ssh_log_analysis.py` – Python script for SSH log analysis

---

## 🖥 Environment

- OS: Linux
- Language: Python 3
- Services: OpenSSH Server
- Log Source: `journalctl -u ssh`

> Note: The script may require `sudo` privileges to access system logs.

---

## 🧠 Learning Outcome

By completing this task, I learned how to:
- Work with real system authentication logs
- Detect suspicious login behavior
- Build simple threat detection logic
- Think like a SOC analyst using backend scripting

This forms a strong foundation for more advanced security automation
and monitoring systems.
