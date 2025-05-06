# kalkulator_bmi.py

def hitung_bmi(massa_kg, tinggi_m):
    return round(massa_kg / (tinggi_m ** 2), 2)

def klasifikasi_bmi(nilai_bmi):
    if nilai_bmi < 18.5:
        return "Kekurangan berat badan"
    elif nilai_bmi < 25:
        return "Normal"
    elif nilai_bmi < 30:
        return "Kelebihan berat badan"
    else:
        return "Obesitas"

def main():
    try:
        berat_badan = float(input("Berat badan Anda (kg): "))
        tinggi_badan = float(input("Tinggi badan Anda (m): "))

        bmi = hitung_bmi(berat_badan, tinggi_badan)
        status = klasifikasi_bmi(bmi)

        print("\n=== Hasil Perhitungan BMI ===")
        print(f"BMI: {bmi}")
        print(f"Status: {status}")

    except ValueError:
        print("Input tidak valid. Harap masukkan angka desimal atau bilangan bulat.")

if __name__ == "__main__":
    main()
