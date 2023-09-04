'''
    Magic method (method-method default yg udah ada di OOP Python)

    __init__
    __repr__
    __str__
    __dict__

    ...
    dsb
'''

class Buah:

    def __init__(self, nama:str, jumlah: int) -> None:
        '''
            Constructor
        '''
        self.nama = nama
        self.jumlah = jumlah

    def __repr__(self) -> str:
        '''
            Biasanya, kalo kita panggil print(<nama_obj>), akan menghasilkan class object dengan memory addressnya

            Nahhh, kita bisa modif output itu...

            function __repr__ biasa digunakan waktu debug
        '''
        return f"Debug -- Buah {self.nama} berjumlah {self.jumlah}"

    def __str__(self) -> str:
        '''
            Biasanya, kalo kita panggil print(<nama_obj>), akan menghasilkan class object dengan memory addressnya

            Nahhh, kita bisa modif output itu...
        '''
        return f"Buah {self.nama} berjumlah {self.jumlah}"
    
    @property
    def __dict__(self):
        return "Objek ini punya nama dan jumlah"
    
    def __add__(self, objek):
        return self.jumlah + objek.jumlah


mangga = Buah("Mangga", 10)
pisang = Buah("Pisang", 12)
print(f"Mangga: {mangga}")
print(f"Pisang: {pisang}")
print(f"Mangga+Pisang: {mangga+pisang}")
print(mangga.__dict__)