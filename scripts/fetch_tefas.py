import requests
import json
from datetime import datetime

def fetch_fon(fon_kod, start_date, end_date):
    url = f"https://www.tefas.gov.tr/api/DB/BindHistoryGraphData?FonKod={fon_kod}&startDate={start_date}&endDate={end_date}"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, timeout=30)
    return r.json()

if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    fonlar = [
        "AEF", "ASY", "TTE", "YAY", "TEF", "ZPE", "HDF", "TUA", "TZE", "AFH",
        "TAF", "VDF", "ISF", "AKF", "HSF", "KTF", "NNF", "QNB", "SEF", "KUF",
        "CAF", "ANF", "YKF", "YVF", "TEB", "HAL", "GAR", "VAK", "ODE", "TSF",
        "YEF", "YHF", "ASF", "BGF", "FHF", "YMF", "BNF", "ISY", "ISB", "VIO",
        "YGO", "KLF", "ETF", "NNY", "HLT", "ZAF", "IDF", "QNF", "ANB", "HSY",
        "TTF", "KDY", "KMF", "AAY", "VGF", "YNF", "SFF", "GAF", "PIF", "SDF",
        "BGY", "CAY", "BNP", "ING", "ICF", "BNR", "EAF", "KHF", "ISG", "AKY",
        "HSK", "NNH", "TGF", "VIF", "YBY"
    ]
    all_data = {}
    for kod in fonlar:
        try:
            data = fetch_fon(kod, today, today)
            all_data[kod] = data
        except Exception as e:
            all_data[kod] = {"error": str(e)}

    with open("docs/latest.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
