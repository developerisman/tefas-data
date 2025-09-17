import requests
import json
from datetime import datetime

def fetch_fon(fon_kod, start_date, end_date):
    url = f"https://www.tefas.gov.tr/api/DB/BindHistoryGraphData?FonKod={fon_kod}&startDate={start_date}&endDate={end_date}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    fonlar = ["AEF", "ASY", "TTE", "YAY", "TEF"]  # önce küçük liste dene
    all_data = {}
    for kod in fonlar:
        all_data[kod] = fetch_fon(kod, today, today)

    with open("docs/latest.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
