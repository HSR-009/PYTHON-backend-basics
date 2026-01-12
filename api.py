from fastapi import FastAPI
from scanner import run_security_scan

app=FastAPI(title="Secured Backend API")

@app.get("/")
def root():
    return {"status": "API running"}
@app.get("/scan")
def trigger_scan():
    result = run_security_scan()
    return result
