# Linux Security Monitoring Tool 🛡️

A Python-based Linux security monitoring tool that collects system information,
analyzes SSH authentication logs, detects suspicious login activity, and
generates structured security reports.

This project was built step-by-step as part of a cybersecurity learning path
and reflects real SOC (Security Operations Center) fundamentals.

---

## 📌 Features

- Collects system information (current user)
- Extracts network details from Linux
- Analyzes SSH authentication logs
- Detects failed SSH login attempts
- Classifies security status:
  - Normal
  - Warning
  - Alert
- Generates clean security scan reports
- Logs results persistently for auditing

---

## 📂 Project Files

| File Name | Description |
|---------|-------------|
| `system.py` | 
| `security.log` | 
| `clean_log.py` | 
| `security(1).log` | 

---

## ⚙️ How It Works

1. Runs Linux commands using Python (`subprocess`)
2. Collects:
   - Current system user
   - Network information
3. Reads real SSH logs using:
journalctl -u ssh

yaml
Copy code
4. Counts failed SSH authentication attempts
5. Applies security logic:
- `< 5` → Normal
- `5–9` → Warning
- `≥ 10` → Alert
6. Writes a structured report to `security.log`
7. Displays a clean summary in the terminal

---

## 🧠 Concepts Used

- Python subprocess module
- Linux command execution
- SSH authentication log analysis
- File handling & logging
- Functions and clean code structure
- Exception handling
- Timestamped security reporting

---

## 🖥 Example Output

========= Security Scan Report =========
Scan Time : 2025-12-25 11:45:12

Username : kali
Active IPs:
192.168.1.10

Failed SSH Attempts : 6
Security Status : WARNING
yaml
Copy code

---

## 🛠 Requirements

- Linux OS
- Python 3
- SSH service enabled
- Permission to read SSH logs

> Run with sudo if required:
```bash
sudo python3 system.py
