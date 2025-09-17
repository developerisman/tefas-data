import requests
import pandas as pd
from datetime import datetime
import json
from io import StringIO

def fetch_tefas(date=None):
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")

    url = f"https://www.tefas.gov.tr/MutualFunds/FonKarsilastirma.aspx?FonKod=&Tarih={date}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    r = requests.get(url, headers=headers, timeout=30)

    # pandas future warning fix: StringIO kullan
    dfs = pd.read_html(StringIO(r.text), decimal=",", thousands=".")
    if not dfs:
        raise ValueError("TEFAS tablosu bulunamadı")

    df = dfs[0]
    return df.to_dict(orient="records")

if __name__ == "__main__":
    data = fetch_tefas()
    today = datetime.now().strftime("%Y-%m-%d")

    with open(f"docs/funds_{today}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    with open("docs/latest.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

