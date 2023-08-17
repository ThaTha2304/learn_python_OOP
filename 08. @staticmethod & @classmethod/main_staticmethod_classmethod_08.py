'''
    Module untuk belajar decorator:
    - @staticmethod
    - @classmethod
'''

class Hero:
    '''
        Class Hero, punya private attribute "jumlah"
        Object punya private attribute "Name"; "Health"
    '''

    __jumlah = 0

    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        Hero.__jumlah += 1
    
    # Method hanya berlaku untuk objek
    def getJumlah(self) -> int:
        return self.__jumlah
    
    # Method hanya berlaku untuk class 
    def getJumlah1():
        return Hero.__jumlah
    
    # Method static (decorator)
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah
    
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah
    
hero1 = Hero("Layla", 100)
hero2 = Hero("Irithel", 100)
print(f"hero1.getJumlah(): {hero1.getJumlah()}")
# print(f"hero1.getJumlah(): {hero1.getJumlah1()}") # Akan error
print(f"Hero.getJumlah1(): {Hero.getJumlah1()}")

hero3 = Hero("Hanabi", 100)
print(f"Hero.getJumlah2(): {Hero.getJumlah2()}")

hero4 = Hero("Lunox", 100)
print(f"hero3.getJumlah2(): {hero3.getJumlah2()}")
print(f"Hero.getJumlah3(): {Hero.getJumlah3()}")
