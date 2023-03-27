class Buku:
    def __init__(self, judul, pengarang, penerbit, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.penerbit = penerbit
        self.tahun_terbit = tahun_terbit

    def __str__(self):
        return f"{self.judul} oleh {self.pengarang}"

    def __repr__(self):
        return f"Buku('{self.judul}', '{self.pengarang}', '{self.penerbit}', {self.tahun_terbit})"

class BukuFiksi(Buku):
    def __init__(self, judul, pengarang, penerbit, tahun_terbit, genre):
        super().__init__(judul, pengarang, penerbit, tahun_terbit)
        self.genre = genre

    def __str__(self):
        return super().__str__() + f" ({self.genre})"

class BukuNonFiksi(Buku):
    def __init__(self, judul, pengarang, penerbit, tahun_terbit, subyek):
        super().__init__(judul, pengarang, penerbit, tahun_terbit)
        self.subyek = subyek

    def __str__(self):
        return super().__str__() + f" [{self.subyek}]"

    def __add__(self, other):
        if isinstance(other, BukuNonFiksi):
            return f"{self.judul} dan {other.judul} [{self.subyek}, {other.subyek}]"
        else:
            return NotImplemented

# contoh penggunaan
buku1 = Buku("Sherlock Holmes", "Arthur Conan Doyle", "Gramedia", 1892)
buku2 = BukuFiksi("The Hobbit", "J.R.R. Tolkien", "HarperCollins", 1937, "Fantasy")
buku3 = BukuNonFiksi("The Selfish Gene", "Richard Dawkins", "Oxford University Press", 1976, "Genetika")
buku4 = BukuNonFiksi("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", "Vintage", 2011, "Sejarah")

print(buku1)
# output: Sherlock Holmes oleh Arthur Conan Doyle

print(buku2)
# output: The Hobbit oleh J.R.R. Tolkien (Fantasy)

print(buku3)
# output: The Selfish Gene oleh Richard Dawkins [Genetika]

print(buku3 + buku4)
# output: The Selfish Gene dan Sapiens: A Brief History of Humankind [Genetika, Sejarah]
