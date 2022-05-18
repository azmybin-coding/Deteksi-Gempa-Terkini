"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""

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
    hasil = dict()
    hasil["tanggal"] = "24 Ahustus 2021"
    hasil["waktu"] = "12:05:52 WIB"
    hasil["magnitudo"] = 4.0
    hasil["kedalaman"] = "40 km"
    hasil["lokasi"] = {"ls":1.48, "bt":134.01}
    hasil["pusat"] = "Pusat gempa berada di darat 18 km barat laut Ransiki"
    hasil["dirasakan"] = "Dirasakan (Skala MMI): II-III Manokwari, II-III Ransiki"

    return hasil

def tampilkan_data(result):
    print("Gempa Terakhir berdasarkan BMKG")
    print(f"Tanggal{result['tanggal']}")
    print(f"Waktu{result['waktu']}")
    print(f"Magnitudo{result['magnitudo']}")
    print(f"Kedalaman{result['kedalaman']}")
    print(f"Lokasi{result['lokasi']}")
    print(f"Pusat{result['pusat']}")
    print(f"Dirasakan{result['dirasakan']}")


if __name__ == "__main__":
    print("Aplikasi Utama")
    result = ekstraksi_data()
    tampilkan_data(result)
