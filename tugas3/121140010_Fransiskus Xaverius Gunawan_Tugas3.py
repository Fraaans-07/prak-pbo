# Nama : Fransiskus Xaverius Gunawan
# NIM  : 121140010
# Kelas: PBO-RB

# Nomor 1
import random

class Kotak:
    def __init__(self):
        self.isi = "bom" if random.random() < 0.2 else "kosong"
        self.status = "belum dibuka"
    
    def tampilkan(self):
        if self.status == "belum dibuka":
            return "?"
        elif self.isi == "bom":
            return "x"
        else:
            return "o"
        
    def buka_kotak(self):
        self.status = "sudah dibuka"
        
class Area:
    def __init__(self, dimensi):
        self.dimensi = dimensi
        self.kotak = [[Kotak() for j in range(dimensi)] for i in range(dimensi)]
        self.jumlah_bom = sum(k.isi == "bom" for row in self.kotak for k in row)
        
    def tampilkan(self):
        for i in range(self.dimensi):
            for j in range(self.dimensi):
                print(self.kotak[i][j].tampilkan(), end=" ")
            print()
            
    def buka_kotak(self, nomor_kotak):
        i, j = (nomor_kotak-1) // self.dimensi, (nomor_kotak-1) % self.dimensi
        k = self.kotak[i][j]
        k.buka_kotak()
        if k.isi == "bom":
            print("Game over! Kotak tersebut berisi bom.")
            return False
        elif self.jumlah_bom == sum(k.isi == "bom" for row in self.kotak for k in row if k.status == "sudah dibuka"):
            print("Selamat! Anda telah memenangkan game.")
            return False
        else:
            print("Selamat! Kotak tersebut tidak berisi bom.")
            return True

def main():
    dimensi = int(input("Masukkan dimensi area: "))
    area = Area(dimensi)
    area.tampilkan()
    
    while True:
        nomor_kotak = int(input("Masukkan nomor kotak yang ingin dibuka (1-{}): ".format(dimensi**2)))
        if not area.buka_kotak(nomor_kotak):
            break

if __name__ == "__main__":
    main()

# Nomor 2
class AkunBank:
    list_pelanggan = []
    
    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        AkunBank.list_pelanggan.append((no_pelanggan, nama_pelanggan, jumlah_saldo))
    
    def lihat_menu(self):
        print("Selamat datang di Bank Jago")
        print("Halo {}, ingin melakukan apa?".format(self.__nama_pelanggan))
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")
    
    def lihat_saldo(self):
        print("{} memiliki saldo Rp {}".format(self.__nama_pelanggan, self.__jumlah_saldo))
    
    def tarik_tunai(self):
        nominal = int(input("Masukkan jumlah nominal yang ingin ditarik: "))
        if self.__jumlah_saldo < nominal:
            print("Nominal saldo yang Anda punya tidak cukup!")
        else:
            self.__jumlah_saldo -= nominal
            print("Saldo berhasil ditarik!")
    
    def transfer(self):
        nominal = int(input("Masukkan nominal yang ingin ditransfer: "))
        no_rekening = input("Masukkan no rekening tujuan: ")
        target_pelanggan = None
        for pelanggan in AkunBank.list_pelanggan:
            if pelanggan[0] == no_rekening:
                target_pelanggan = pelanggan
                break
        if target_pelanggan is None:
            print("No rekening tujuan tidak dikenal! Kembali ke menu utama...")
        else:
            target_nama = target_pelanggan[1]
            self.__jumlah_saldo -= nominal
            target_pelanggan[2] += nominal
            print("Transfer Rp {} ke {} sukses!".format(nominal, target_nama))
    
    def run(self):
        while True:
            self.lihat_menu()
            nomor = int(input("Masukkan nomor input: "))
            if nomor == 1:
                self.lihat_saldo()
            elif nomor == 2:
                self.tarik_tunai()
            elif nomor == 3:
                self.transfer()
            else:
                break

# Simulasi penggunaan kelas AkunBank
Akun1 = AkunBank(1234, "nama_kalian", 5000000000)
Akun1.run()

# Nomor 3
class Karyawan:
    # atribut/fungsi private, tidak dapat diakses dari luar kelas
    __nama = ""
    __gaji = 0
    
    # atribut/fungsi protected, hanya dapat diakses dari dalam kelas atau subclass
    _jabatan = ""
    
    # atribut/fungsi public, dapat diakses dari luar kelas
    id_karyawan = 0
    
    # atribut kelas, bernilai konsisten antar instance
    jumlah_karyawan = 0
    
    def __init__(self, nama, gaji, jabatan):
        self.__nama = nama
        self.__gaji = gaji
        self._jabatan = jabatan
        Karyawan.jumlah_karyawan += 1
        self.id_karyawan = Karyawan.jumlah_karyawan
    
    # fungsi public, dapat diakses dari luar kelas
    def get_nama(self):
        return self.__nama
    
    # fungsi public, dapat diakses dari luar kelas
    def set_gaji(self, gaji):
        self.__gaji = gaji
    
    # fungsi public, dapat diakses dari luar kelas
    def get_gaji(self):
        return self.__gaji
    
    # fungsi protected, hanya dapat diakses dari dalam kelas atau subclass
    def get_jabatan(self):
        return self._jabatan
    
    # fungsi public, dapat diakses dari luar kelas
    def tampilkan_info(self):
        print("ID Karyawan:", self.id_karyawan)
        print("Nama Karyawan:", self.__nama)
        print("Jabatan Karyawan:", self._jabatan)
        print("Gaji Karyawan:", self.__gaji)