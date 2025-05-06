# student_scores.py

data_mahasiswa = [
    {"nama": "Bayu", "nim": "22071", "uts": 80, "uas": 85, "tugas": 75},
    {"nama": "Sika", "nim": "22062", "uts": 65, "uas": 70, "tugas": 60},
    {"nama": "Dimas", "nim": "22053", "uts": 90, "uas": 95, "tugas": 90},
    {"nama": "Yohanes", "nim": "22023", "uts": 50, "uas": 55, "tugas": 45},
    {"nama": "Duwi", "nim": "22011", "uts": 70, "uas": 60, "tugas": 65}
]

def hitung_nilai_akhir(uts, uas, tugas):
    return round((0.3 * uts) + (0.4 * uas) + (0.3 * tugas), 2)

def tentukan_grade(nilai):
    if nilai >= 80:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    return "E"

def tampilkan_tabel(mahasiswa_list):
    print("\nRekap Nilai Mahasiswa:")
    header = f"{'Nama':<10} {'NIM':<8} {'UTS':<5} {'UAS':<5} {'Tugas':<6} {'Akhir':<8} {'Grade'}"
    print(header)
    print("-" * len(header))

    for m in mahasiswa_list:
        print(f"{m['nama']:<10} {m['nim']:<8} {m['uts']:<5} {m['uas']:<5} {m['tugas']:<6} {m['akhir']:<8} {m['grade']}")

def cari_extremes(mahasiswa_list):
    tertinggi = max(mahasiswa_list, key=lambda m: m["akhir"])
    terendah = min(mahasiswa_list, key=lambda m: m["akhir"])
    return tertinggi, terendah

# Proses utama
for m in data_mahasiswa:
    nilai_akhir = hitung_nilai_akhir(m["uts"], m["uas"], m["tugas"])
    m["akhir"] = nilai_akhir
    m["grade"] = tentukan_grade(nilai_akhir)

tampilkan_tabel(data_mahasiswa)

top, bottom = cari_extremes(data_mahasiswa)
print(f"\nNilai Tertinggi: {top['nama']} dengan {top['akhir']}")
print(f"Nilai Terendah : {bottom['nama']} dengan {bottom['akhir']}")
