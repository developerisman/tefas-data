import requests
from bs4 import BeautifulSoup
import json

def fetch_fintables_aft():
    url = "https://fintables.com/fonlar/AFT"
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, timeout=15)
    if r.status_code != 200:
        return {"error": f"Status code {r.status_code}"}
    html = r.text

    soup = BeautifulSoup(html, "html.parser")

    # Örnek: Fon Toplam Değer
    try:
        fon_toplam_deger = soup.find(text="Fon Toplam Değer").parent.get_text().split()[-2]  # Kabaca al
    except Exception as e:
        fon_toplam_deger = None

    # Örnek: Yabancı Hisse Senedi yüzdesi
    try:
        yy = soup.find(text="Yabancı Hisse Senedi").parent.get_text().split()[-1]
    except Exception as e:
        yy = None

    return {
        "fon_kodu": "AFT",
        "fon_toplam_deger": fon_toplam_deger,
        "yabanci_hisse_yuzdesi": yy
    }

if __name__ == "__main__":
    data = fetch_fintables_aft()
    print(json.dumps(data, indent=2, ensure_ascii=False))
