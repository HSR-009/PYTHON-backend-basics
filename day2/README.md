# Day 2 – Linux Network Info Analyzer (Python Backend)

This project is part of my Python backend learning journey focused on
Linux automation and cybersecurity fundamentals.

On Day 2, I worked on executing Linux networking commands using Python,
parsing their output, and extracting meaningful information safely.

---

## 🔍 What This Script Does

- Runs the Linux command `ip a` using Python
- Captures command output using `subprocess.run()`
- Parses the output line by line
- Extracts active IPv4 network interfaces
- Ignores the loopback address (`127.0.0.1`)
- Displays a clear message if no valid IP is found
- Prints the scan time for better monitoring context

---

## 🛠 Concepts Used

- Python `subprocess.run()`
- Handling `stdout`, `stderr`, and `returncode`
- Linux command execution from Python
- Output parsing using `splitlines()`
- String filtering and conditions
- Basic error handling
- `datetime` for timestamps

---

## 🧠 Why This Matters

This task represents real-world backend and cybersecurity automation:

- Network interface detection
- System reconnaissance fundamentals
- SOC-style data extraction
- Clean and safe command execution

These skills are essential for:
- Hackathons (SIH-style problems)
- Cybersecurity scripting
- Backend system monitoring tools

---

## 🖥 Environment

- OS: Linux
- Language: Python 3
- Tools: ip (Linux networking utility)

---

## 🚀 Learning Outcome

By completing this task, I gained confidence in:
- Writing backend scripts on Linux
- Automating system-level commands
- Parsing raw system output into useful data
- Building a strong foundation for future security tools and APIs
