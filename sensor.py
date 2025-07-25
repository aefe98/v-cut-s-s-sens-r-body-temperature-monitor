import random  # Rastgele sayı üretmek için gerekli modül
import time    # Zamanla ilgili işlemler (bekleme süresi gibi)

def oku_sicaklik():
    return round(random.uniform(36.0, 41.0), 1)

while True:
    sicaklik = oku_sicaklik()
    print(f"Sıcaklık: {sicaklik}°C")
    time.sleep(3)

    if sicaklik > 39.5:
        print("Ciddi ateş, Yüksek ateş tespit edildi!")
    elif sicaklik > 38.0:
        print("Yüksek ateş, müdahale gerektirir")
    elif 37.5 <= sicaklik <= 38.0:
        print("Subferil, Hafif ateş başlangıcı")
    elif sicaklik < 36.0:
        print("Hipotermi riski, Düşük vücut ısısı")
    else:
        print("Vücut ısısı normal")










