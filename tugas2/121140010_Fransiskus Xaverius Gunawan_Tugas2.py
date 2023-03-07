# Nama : Fransiskus Xaverius Gunawan
# NIM  : 121140010
# Kelas: PBO RB

# Kelas
class Frans:
    def __init__(self, nama, nim, prodi,  kelas, sks):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.kelas = kelas
        self.sks = sks

    # Method untuk menampilkan atribut dari class Frans
    def panggil_identitas(self):
        print("Nama: " + self.nama)
        print("NIM: " + str(self.nim))
        print("Prodi: " + self.prodi)
        print("Kelas: "+self.kelas)
        print("Jumlah SKS: " + str(self.sks))

# Menampilkan isi dari identitas dengan menggunakan method panggil_identitas
mahasiswa = Frans("Fransiskus", 121140010,
                  "Teknik Informatika", "PBO RB", 22)
mahasiswa.panggil_identitas()
