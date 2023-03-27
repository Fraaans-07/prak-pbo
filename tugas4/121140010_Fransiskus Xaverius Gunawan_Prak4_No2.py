import random

class Robot:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.jumlah_turn = 0
    
    def lakukan_aksi(self):
        self.jumlah_turn += 1
        if self.jumlah_turn % self.get_frequency() == 0:
            self.do_special_action()
        
        if self.health <= 0:
            print(f"{self.name} kalah!")
            return
        
        print(f"{self.name} menyerang sebanyak {self.damage} DMG")
    
    def terima_aksi(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} kalah!")
    
    def get_frequency(self):
        return 1
    
    def do_special_action(self):
        pass
    
    def get_hasil_permainan(pilihan_robotmu, pilihan_lawan):
        if pilihan_robotmu == "1" and pilihan_lawan == 3:
            return "menang"
        elif pilihan_robotmu == "2" and pilihan_lawan == 1:
            return "menang"
        elif pilihan_robotmu == "3" and pilihan_lawan == 2:
            return "menang"
        elif pilihan_robotmu == pilihan_lawan:
            return "seri"
        else:
            return "kalah"

class Antares(Robot):
    def __init__(self):
        super().__init__("Antares", 50000, 5000)
        self.special_damage = self.damage
    
    def get_frequency(self):
        return 3
    
    def do_special_action(self):
        self.special_damage = self.damage * 1.5
        print(f"{self.name} meningkatkan damage menjadi {self.special_damage}")
    
    def lakukan_aksi(self):
        super().lakukan_aksi()
        self.damage = self.special_damage

class Alphasetia(Robot):
    def __init__(self):
        super().__init__("Alphasetia", 40000, 6000)
    
    def get_frequency(self):
        return 2
    
    def do_special_action(self):
        self.health += 4000
        print(f"{self.name} menambah darah sebanyak 4000 HP")

class Lecalicus(Robot):
    def __init__(self):
        super().__init__("Lecalicus", 45000, 5500)
        self.special_damage = self.damage
    
    def get_frequency(self):
        return 4
    
    def do_special_action(self):
        self.health += 7000
        self.special_damage = self.damage * 2
        print(f"{self.name} meningkatkan damage menjadi {self.special_damage}")
    
    def lakukan_aksi(self):
        super().lakukan_aksi()
        self.damage = self.special_damage

def main():
    robots = [Antares(), Alphasetia(), Lecalicus()]
    print("Selamat datang di pertandingan robot Yamako")
    
    pilihan_robot = int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
    robotmu = robots[pilihan_robot-1]
    
    pilihan_lawan = int(input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
    robot_lawan = robots[pilihan_lawan-1]
    
    tangan = {"1": "batu", "2": "kertas", "3": "gunting"}
    
    while robotmu.health > 0 and robot_lawan.health > 0:
        print(f"Turn saat ini: {robotmu.jumlah_turn+1}")
        print(f"Robotmu ({robotmu.name} - {robotmu.health} HP), robot lawan ({robot_lawan.name} - {robot_lawan.health} HP)")
        
        pilihan_robotmu = input(f"Pilih tangan robotmu ({robotmu.name}): ")
        if pilihan_robotmu not in tangan:
            print("Input tidak valid!")
            continue
        
        pilihan_lawan = robot_lawan.choose_hand()
        print(f"Robot lawan memilih tangan: {tangan[str(pilihan_lawan)]}")
        
        hasil = robotmu.get_hasil_permainan(pilihan_robotmu, pilihan_lawan)
        if hasil == "menang":
            robot_lawan.health -= 10
            print(f"Selamat, {robotmu.name} menang! {robot_lawan.name} kehilangan 10 HP")
        elif hasil == "kalah":
            robotmu.health -= 10
            print(f"Sayang sekali, {robotmu.name} kalah. Kehilangan 10 HP")
        else:
            print("Seri!")
        
        robotmu.jumlah_turn += 1
        robot_lawan.jumlah_turn += 1
    
    if robotmu.health <= 0:
        print(f"Sayang sekali, {robotmu.name} kalah. Silakan coba lagi!")
    else:
        print(f"Selamat, {robotmu.name} menang! Terima kasih sudah bermain.")
