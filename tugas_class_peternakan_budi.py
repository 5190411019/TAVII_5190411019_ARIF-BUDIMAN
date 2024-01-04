# Kelas Induk: Hewan
class Hewan:
    def __init__(self, nama, umur, pendapatan):
        self.__nama = nama
        self.umur = umur
        self.pendapatan = pendapatan

    def get_nama(self):
        return self.__nama

    def bersuara(self):
        print("Hewan bersuara: Suara hewan khas")

    def makan(self):
        print("Hewan sedang makan")

    def bergerak(self):
        print("Hewan sedang bergerak")

    def get_pendapatan(self):
        return self.pendapatan


# Kelas Anak Pertama: Mamalia
class Mamalia(Hewan):
    def __init__(self, nama, umur, jenis_bulu, pendapatan):
        super().__init__(nama, umur, pendapatan)
        self.jenis_bulu = jenis_bulu

    def menyusui(self):
        print(f"{self.get_nama()} menyusui anaknya")

    def bersuara(self):
        print("Mamalia bersuara: Suara mamalia khas")


# Kelas Anak Kedua: Unggas
class Unggas(Hewan):
    def __init__(self, nama, umur, jenis_telur, pendapatan):
        super().__init__(nama, umur, pendapatan)
        self.__jenis_telur = jenis_telur

    def bertelur(self):
        print(f"{self.get_nama()} sedang bertelur")

    def get_jenis_telur(self):
        return self.__jenis_telur

    def bersuara(self):
        print("Unggas bersuara: Kukuruyukk")


# Kelas Anak Kedua dari Mamalia: Sapi
class Sapi(Mamalia):
    def __init__(self, nama, umur, jenis_susu, pendapatan):
        super().__init__(nama, umur, "Berbulu lebat", pendapatan)
        self.jenis_susu = jenis_susu

    def bersuara(self):
        print("Sapi bersuara: Moo")


# Contoh penggunaan kelas dan konsep pewarisan, enkapsulasi, dan polimorfisme
pendapatan_ternak1 = float(input("Masukkan pendapatan untuk ternak 1: "))
ternak1 = Mamalia("Sapi Betina", 2, "Berbulu lebat", pendapatan_ternak1)

pendapatan_ayam1 = float(input("Masukkan pendapatan untuk ayam 1: "))
ayam1 = Unggas("Ayam Jago", 1, "Telur Merah", pendapatan_ayam1)

pendapatan_sapi1 = float(input("Masukkan pendapatan untuk sapi 1: "))
sapi1 = Sapi("Sapi Jantan", 3, "Susu Segar", pendapatan_sapi1)

# Contoh penggunaan operator aritmatika
total_pendapatan = ternak1.get_pendapatan() + ayam1.get_pendapatan() + sapi1.get_pendapatan()
print(f"Total pendapatan: {total_pendapatan}")

# Fungsi untuk mensimulasikan aktivitas harian di peternakan
def aktivitas_harian(hewan):
    print(f"{hewan.get_nama()} adalah ternak.")
    hewan.makan()
    hewan.bergerak()
    hewan.bersuara()
    hewan.get_pendapatan()

# Contoh penggunaan kelas dan konsep pewarisan, enkapsulasi, dan polimorfisme
hari = int(input('Masukkan jumlah hari yang dilihat: '))

# Penggunaan percabangan untuk menentukan kejadian acak
for i in range(1, hari + 1):  # Loop untuk setiap hari
    print(f"\n========== Hari {i} di Peternakan ==========")

    # Meminta input cuaca untuk setiap hari
    kejadian_acak = input("Masukkan cuaca (hujan, cerah, angin kencang): ")
    while kejadian_acak not in ["hujan", "cerah", "angin kencang"]:
        print('Cuaca tidak valid, silakan input cuaca yang benar.')
        kejadian_acak = input("Masukkan cuaca (hujan, cerah, angin kencang): ")

    # Menampilkan informasi cuaca sekali saja untuk setiap hari
    if kejadian_acak == "hujan":
        print("Hari ini hujan, sebaiknya semua hewan berada di dalam kandang.")
    elif kejadian_acak == "cerah":
        print("Hari ini cerah, hewan-hewan dapat berada di padang rumput.")
    elif kejadian_acak == "angin kencang":
        print("Hari ini angin kencang, pastikan kandang dan kios makanan hewan aman.")

    for hewan in [ternak1, ayam1, sapi1]:
        aktivitas_harian(hewan)
