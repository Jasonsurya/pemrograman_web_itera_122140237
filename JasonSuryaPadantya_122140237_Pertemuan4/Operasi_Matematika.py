# Konstanta
PI = 3.14159

# Fungsi Bangun Datar
def luas_kotak(sisi):
    return sisi ** 2

def keliling_kotak(sisi):
    return 4 * sisi

def luas_panjang_lebar(panjang, lebar):
    return panjang * lebar

def keliling_panjang_lebar(panjang, lebar):
    return 2 * (panjang + lebar)

def luas_bulat(radius):
    return PI * radius * radius

def keliling_bulat(radius):
    return 2 * PI * radius

# Fungsi Konversi Suhu
def dari_celsius_ke_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def dari_celsius_ke_kelvin(celsius):
    return celsius + 273.15

# Contoh penggunaan (opsional)
if __name__ == "__main__":
    print("Luas persegi sisi 5:", luas_kotak(5))
    print("Keliling persegi panjang 4x6:", keliling_panjang_lebar(4, 6))
    print("Luas lingkaran jari-jari 7:", luas_bulat(7))
    print("30°C dalam Fahrenheit:", dari_celsius_ke_fahrenheit(30))
    print("30°C dalam Kelvin:", dari_celsius_ke_kelvin(30))
