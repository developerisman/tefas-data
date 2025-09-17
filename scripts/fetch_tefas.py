import requests
import xml.etree.ElementTree as ET
import json

url = "https://www.tefas.gov.tr/api/DB/BindCanceledFunds"  # örnek iptal fon servisi
headers = {"User-Agent": "Mozilla/5.0"}
r = requests.get(url, headers=headers, timeout=10)

funds = []
root = ET.fromstring(r.text)

for fund in root.findall(".//{http://schemas.datacontract.org/2004/07/TefasTr.Controllers}FundCode"):
    funds.append(fund.text)

with open("docs/latest.json", "w", encoding="utf-8") as f:
    json.dump(funds, f, ensure_ascii=False, indent=2)

print("Toplam iptal fon:", len(funds))
