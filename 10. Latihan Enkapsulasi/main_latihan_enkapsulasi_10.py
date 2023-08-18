'''
    Latihan enkapsulasi
'''

class Hero:

    # private class variable
    __jumlah = 0

    def __init__(self, name:str, health:int, attPower:int, armor:int) -> None:
        '''
            Constructor object
        '''

        # Base Attribute object
        self.__name = name
        self.__healthBase = health
        self.__attPowerBase = attPower
        self.__armorBase = armor
        self.__level = 1
        self.__exp = 0

        # Attribute object yang dinamis sesuai dengan level
        self.__healthMax = self.__healthBase * self.__level
        self.__attPower = self.__attPowerBase * self.__level
        self.__armor = self.__armorBase * self.__level
        self.__health = self.__healthMax

        # Menambah jumlah hero
        Hero.__jumlah += 1

    @property
    def info (self):
        '''
            Method untuk menampilkan summary dari object
        '''
        return f'''\n{self.__name} level {self.__level}:
- health: {self.__health}/{self.__healthMax}
- attPower: {self.__attPower}
- armor: {self.__armor}
        '''
    
    @property
    def gainExp(self):
        '''
            Property gainExp
        '''
        pass

    @gainExp.setter
    def gainExp(self, addExp:int):
        '''
            Method untuk set exp
        '''
        # Menambah exp
        self.__exp += addExp

        # Hero level up, jika exp >= 100
        while self.__exp >= 100:
            print(f"{self.__name} leveled up!")
            # Level bertambah 1
            self.__level += 1

            # Reset exp
            self.__exp -= 100

            # Adjust attribute hero
            self.__healthMax = self.__healthBase * self.__level
            self.__attPower = self.__attPowerBase * self.__level
            self.__armor = self.__armorBase * self.__level
            self.__health = self.__healthMax

            if self.__exp < 100:
                break

    def attack(self, enemy):
        '''
            Method untuk menyerang musuh. Setiap serangan akan mendapatkan exp 50
        '''
        print(f"{self.__name} attacking {enemy.__name}!")
        self.gainExp = 50


# Instansiasi object
layla = Hero(name="Layla", health=100, attPower=10, armor=5)
irithel = Hero(name="Irithel", health=100, attPower=10, armor=5)

# Main program
print(layla.info)
print(irithel.info)

layla.attack(irithel)
layla.attack(irithel)
print(layla.info)

irithel.gainExp = 250
print(irithel.info)