# main.py

# Import seluruh modul
import Operasi_Matematika as om
# Import sebagian fungsi
from Operasi_Matematika import dari_celsius_ke_fahrenheit, dari_celsius_ke_kelvin

# Geometri
print("=== Hitung Luas dan Keliling ===")
print(f"Luas Persegi (sisi 4): {om.luas_kotak(5)}")
print(f"Keliling Persegi: {om.keliling_kotak(6)}")
print(f"Luas Persegi Panjang (5x3): {om.luas_panjang_lebar(9, 7)}")
print(f"Keliling Persegi Panjang: {om.keliling_panjang_lebar(9, 2)}")
print(f"Luas Lingkaran (r=7): {om.luas_bulat(4):.2f}")
print(f"Keliling Lingkaran: {om.keliling_bulat(8):.2f}")

# Suhu
print("\n=== Konversi Suhu ===")
print(f"30°C ke Fahrenheit: {dari_celsius_ke_fahrenheit(30):.2f}°F")
print(f"30°C ke Kelvin: {dari_celsius_ke_kelvin(30):.2f}K")
