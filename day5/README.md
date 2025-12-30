# Linux Security Monitoring & Automation Tool 🛡️

A Python-based Linux security monitoring tool that automates system checks,
analyzes SSH authentication logs, detects suspicious activity, and stores
results in both human-readable and machine-readable formats.

This project demonstrates **SOC fundamentals, backend security automation,
and AI-ready log generation**.

---

## 📌 Key Features

- Automated security scans using cron
- SSH authentication log analysis
- Detection of failed login attempts
- Security classification:
  - Normal
  - Warning
  - Alert
- Human-readable log reports
- Machine-readable JSON logs (AI / API ready)
- Modular and structured Python backend

---

## 📂 Project Files

| File Name | Description |
|---------|-------------|
| `system.py` | Core security monitoring logic and functions |
| `demo.py` | Automated execution script (used with cron) |
| `security.log` | Human-readable security scan logs |
| `demo.log` | Execution and runtime logs for cron/debugging |
| `security.json` | Structured JSON logs (one event per scan) |

---

## ⚙️ How the System Works

1. The script collects system information:
   - Current user
   - Network information
2. Reads real SSH authentication logs using:
3. Counts failed SSH login attempts
4. Applies threat logic:
- `< 5` failed attempts → Normal
- `5–9` failed attempts → Warning
- `≥ 10` failed attempts → Alert
5. Writes results to:
- `security.log` (readable report)
- `security.json` (structured event log)
6. Runs automatically via cron at scheduled intervals

---

## 🧠 Concepts & Skills Used

- Python subprocess automation
- Linux system commands
- SSH log analysis
- File handling & logging
- JSON logging (JSON Lines format)
- Cron job automation
- Backend security engineering
- SOC-style threat detection logic

---

## 🖥 Example Terminal Output

```text
========= Security Scan Report =========
Scan Time : 2025-12-25 14:00:00

Username : kali
Active IPs:
192.168.1.10

Failed SSH Attempts : 6
Security Status : Warning
========================================
