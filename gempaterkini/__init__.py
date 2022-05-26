import requests
from bs4 import BeautifulSoup

def ekstraksi_data():
    """
    Tanggal: 24 Agustus 2021
    Waktu: 12:05:52 WIB
    Magnitudo: 4.0
    Kedalaman: 40 km
    Lokasi: LS=1.48 BT=134.01
    Pusat Gempa: Pusat gempa berada di darat 18 km barat laut Ransiki
    Dirasakan: Dirasakan (Skala MMI): II-III Manokwari, II-III Ransiki
    :return:
    """
    try:
        content = requests.get("https://bmkg.go.id")
    except Exception:
        return None

    if  content.status_code == 200:
        soup = BeautifulSoup(content.text, "html.parser")

        result = soup.find("span", {"class": "waktu"})
        result = result.text.split(", ")
        waktu = result[1]
        tanggal = result[0]

        result = soup.find("div", {"class": "col-md-6 col-xs-6 gempabumi-detail no-padding"})
        result = result.findChildren("li")
        i = 0
        magnitudo = None
        kedalaman = None
        koordinat = None
        lu = None
        bt = None
        lokasi = None
        dirasakan = None
        for res in result:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1

        hasil = dict()
        hasil["tanggal"] = tanggal
        hasil["waktu"] = waktu
        hasil["magnitudo"] = magnitudo
        hasil["kedalaman"] = kedalaman
        hasil["koordinat"] = koordinat
        hasil["lokasi"] = lokasi
        hasil["dirasakan"] = dirasakan
        return hasil
    else:
        return None

def tampilkan_data(result):
    if result is None:
        print("Tidak bisa menemukan data gempa terkini")
        return
    print("Gempa Terakhir berdasarkan BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Koordinat {result['koordinat']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"Dirasakan {result['dirasakan']}")

