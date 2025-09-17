import requests
import pandas as pd
from datetime import datetime

def fetch_tefas(date=None):
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")

    url = f"https://www.tefas.gov.tr/MutualFunds/FonKarsilastirma.aspx?FonKod=&Tarih={date}"
    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(url, headers=headers, timeout=30)
    df = pd.read_html(r.text, decimal=",", thousands=".")[0]

    return df.to_dict(orient="records")

if __name__ == "__main__":
    data = fetch_tefas()
    today = datetime.now().strftime("%Y-%m-%d")

    # docs klasörüne kaydet
    import json
    with open(f"docs/funds_{today}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # her zaman latest.json da oluştur
    with open("docs/latest.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
