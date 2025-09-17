import requests
import xml.etree.ElementTree as ET
import json
from datetime import datetime

def fetch_fon(fon_kod, start_date, end_date):
    url = f"https://www.tefas.gov.tr/api/DB/BindHistoryGraphData?FonKod={fon_kod}&startDate={start_date}&endDate={end_date}"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, timeout=15)

    root = ET.fromstring(r.text)
    ns = {"ns": "http://schemas.datacontract.org/2004/07/TefasTr.Controllers"}

    prices = []
    for item in root.findall(".//ns:GraphicData", ns):
        tarih = item.find("ns:Tarih", ns).text
        fiyat = item.find("ns:Value", ns).text
        prices.append({"date": tarih, "price": fiyat})

    return prices

if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    fonlar = ["AEF", "TZE", "YAY"]  # burada istediğin fon kodlarını yaz
    all_data = {}

    for kod in fonlar:
        all_data[kod] = fetch_fon(kod, "2025-01-01", today)

    with open("docs/latest.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

    print("Toplam fon:", len(all_data))
