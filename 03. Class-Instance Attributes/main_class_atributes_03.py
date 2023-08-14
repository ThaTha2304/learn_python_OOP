'''
    Module berisi pengenalan OOP
'''

# Pembuatan class dengan nama "Hero"
class Hero:
    '''
        Class Hero
    '''
    # class variables
    jumlah = 0
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        
        #Akses class variable
        Hero.jumlah += 1 # Setiap ada instansiasi object, variabel class Hero "jumlah", akan bertambah 1
        print(f"Berhasil membuat hero: {name}")


# Pembuatan object, langsung dimasukkan parameter constructornya
print(f"Jumlah Hero saat ini: {Hero.jumlah}\n") # 0

hero1 = Hero("Layla", 100)
print(hero1.__dict__) # {'name': 'Layla', 'health': 100}
print(f"Jumlah Hero saat ini: {Hero.jumlah}\n") # 1

hero2 = Hero("Irithel", 250)
print(hero2.__dict__) # {'name': 'Irithel', 'health': 250}
print(f"Jumlah Hero saat ini: {Hero.jumlah}\n") # 2