# Nama : Fransiskus Xaverius Gunawan
# NIM  : 121140010
# Kelas: PBO RB

# Nomor 1
print("Program nomor 1: ")
n = int(input("Masukkan panjang baris dan kolom: "))
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

print("="*20)

# Nomor 2
print("Program nomor 2: ")
# username dan password
username = "informatika"
password = 12345678
percobaan = 1

for i in range(3):
    username_input = input("Masukkan username: ")
    password_input = int(input("Masukkan password: "))
    print()
    print("Username anda: " + username_input)
    print("Password anda: " + str(password_input))
    if username_input == username and password_input == password:
        print("Berhasil login!")
        break
    elif percobaan == 3 and username_input != username and password_input != password:
        print("Username atau Password salah sebanyak 3 kali dan akun diblokir.")
    else:
        print("Username atau password salah coba lagi.\n")
    percobaan += 1