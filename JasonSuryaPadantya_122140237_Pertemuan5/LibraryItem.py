from abc import ABC, abstractmethod

class KoleksiPerpustakaan(ABC):
    def __init__(self, kode, judul):
        self._kode = kode
        self.__judul = judul

    @property
    def judul(self):
        return self.__judul

    @abstractmethod
    def tampilkan_info(self):
        pass

class Buku(KoleksiPerpustakaan):
    def __init__(self, kode, judul, penulis):
        super().__init__(kode, judul)
        self.penulis = penulis

    def tampilkan_info(self):
        print(f"[Buku] Kode: {self._kode}, Judul: {self.judul}, Penulis: {self.penulis}")

class Majalah(KoleksiPerpustakaan):
    def __init__(self, kode, judul, edisi):
        super().__init__(kode, judul)
        self.edisi = edisi

    def tampilkan_info(self):
        print(f"[Majalah] Kode: {self._kode}, Judul: {self.judul}, Edisi: {self.edisi}")

class SistemPerpustakaan:
    def __init__(self):
        self._koleksi = []

    def tambah_koleksi(self, item):
        self._koleksi.append(item)
        print("Koleksi berhasil ditambahkan.")

    def tampilkan_koleksi(self):
        if not self._koleksi:
            print("Belum ada koleksi.")
        else:
            print("\n== Daftar Koleksi Perpustakaan ==")
            for item in self._koleksi:
                item.tampilkan_info()

    def cari_koleksi(self, kata_kunci):
        hasil = []
        for item in self._koleksi:
            if kata_kunci.lower() in item.judul.lower() or kata_kunci == item._kode:
                hasil.append(item)
        if hasil:
            print("\n== Hasil Pencarian ==")
            for item in hasil:
                item.tampilkan_info()
        else:
            print("Tidak ditemukan.")

if __name__ == "__main__":
    perpustakaan = SistemPerpustakaan()

    buku1 = Buku("BK01", "Dasar Python", "Rina")
    buku2 = Buku("BK02", "OOP Lanjut", "Doni")
    majalah1 = Majalah("MJ01", "Digital Era", "Edisi 3")

    perpustakaan.tambah_koleksi(buku1)
    perpustakaan.tambah_koleksi(buku2)
    perpustakaan.tambah_koleksi(majalah1)

    perpustakaan.tampilkan_koleksi()

    print("\n>>> Cari 'Python':")
    perpustakaan.cari_koleksi("Python")

    print("\n>>> Cari 'MJ01':")
    perpustakaan.cari_koleksi("MJ01")

    print("\n>>> Cari 'XYZ':")
    perpustakaan.cari_koleksi("XYZ")
