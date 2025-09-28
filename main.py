# main.py
from fastapi import FastAPI
import json

app = FastAPI()

# ---- 1. tercih: doğrudan import (repo'da fonksiyon varsa)
try:
    # örnek: scripts.tefas.get_all_funds  -> repo'daki gerçek fonksiyon adını buraya yaz
    from scripts.tefas import get_all_funds as _get_funds
    def get_funds():
        return _get_funds()
except Exception as e:
    # ---- 2. fallback: eğer import yapılamazsa, repo içindeki bir script'i çalıştır ve stdout'tan JSON oku
    import subprocess
    def get_funds():
        # scripts/fetch_tefas.py örnektir; repo'da benzer bir script varsa kullan
        p = subprocess.run(["python", "scripts/fetch_tefas.py"], capture_output=True, text=True)
        try:
            return json.loads(p.stdout)
        except Exception:
            return {"error": "data fetch failed", "stdout": p.stdout, "stderr": p.stderr}

@app.get("/fonlar")
def fonlar():
    return get_funds()

