# Day 7 — Backend Logic Refactor & API Integration

## Overview

Day 7 focuses on converting an existing Python backend script into a **reusable backend module** and exposing it through a **minimal HTTP API**.

The goal of this day is not to add new features, but to learn how:
- backend logic is separated from execution
- the same logic can be reused by different interfaces
- APIs interact with existing backend systems

This day introduces **API development fundamentals** using FastAPI.

---

## What Was Done on Day 7

### 1. Backend Logic Refactor

The core security scanning logic was refactored into a callable function:

run_security_scan()

yaml
Copy code

This function:
- Collects system and SSH log data
- Computes baseline behavior from historical logs
- Calculates a risk score
- Generates a high-level security decision
- Writes results to log files
- Returns structured data as a Python dictionary

This refactor ensures the logic:
- does not auto-run on import
- can be reused by cron jobs, APIs, or other services

---

### 2. File Separation by Responsibility

Two main backend files are used:

#### `scanner.py`
Contains **only core backend logic**:
- system data collection
- analysis
- decision-making
- logging

No web or HTTP-related code exists in this file.

#### `api.py`
Acts as a **thin interface layer**:
- receives HTTP requests
- calls backend logic from `scanner.py`
- returns JSON responses

This separation follows real backend design principles.

---

### 3. API Integration Using FastAPI

A minimal FastAPI application was created to expose backend functionality.

The API provides:

#### `GET /`
Health-check endpoint to confirm the API is running.

Example response:
```json
{
  "status": "API running"
}
GET /scan
Triggers a real-time backend security scan.

Behavior:

Calls run_security_scan()

Executes full backend logic

Returns scan result as JSON

Example response:

json
Copy code
{
  "timestamp": "2026-01-08 12:32:10",
  "failed_ssh_attempts": 5,
  "baseline": 2.6,
  "risk_score": 50,
  "ai_decision": "Suspicious Activity"
}
