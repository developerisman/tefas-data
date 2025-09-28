from fastapi import FastAPI
import json
import subprocess

app = FastAPI()

def get_funds():
    # fetch.py yerine fetch_tefas.py kullanıyoruz
    p = subprocess.run(
        ["python", "scripts/fetch_tefas.py"],
        capture_output=True,
        text=True
    )
    try:
        return json.loads(p.stdout)
    except Exception:
        return {
            "error": "data fetch failed",
            "stdout": p.stdout,
            "stderr": p.stderr
        }

@app.get("/fonlar")
def fonlar():
    return get_funds()

