'''
    Module latihan OOP (Game Sederhana)
'''

class Hero:
    def __init__(self, name:str, health:int, attackPower:int, armor:int) -> None:
        '''
            Detail: 
            - name = nama object
            - health = jumlah darahnya
            - attackPower = kekuatan serangan
            - armor = kekuatan armor
        '''
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armor = armor

    # Method tanpa argument
    def summary(self) -> None:
        '''
            Method tanpa argument untuk menampilkan summary dari object
        '''
        print(f"""\nSummary dari object:
        - Name\t\t: {self.name}
        - Health\t: {self.health}
        - Attack Power\t: {self.attackPower}
        - Armor\t\t: {self.armor}""")
    
    def menyerang(self, lawan) -> None:
        '''
            Method simulasi menyerang lawan
        '''
        print(f"\n{self.name} menyerang {lawan.name}")
        lawan.diserang(self)

    def diserang(self, lawan) -> None:
        '''
            Method simulasi diserang lawan, darah berkurang sebesar attack lawan dikurangi armor hero
        '''
        print(f"{self.name} diserang {lawan.name}")
        self.health -= (lawan.attackPower-self.armor)
        print(f"{self.name} menerima damage sebesar {lawan.attackPower}...")
        print(f"Health {self.name} tersisa {self.health}")


# Instansiasi object
layla = Hero(name="Layla", health=100, attackPower=20, armor=5)
irithel = Hero(name="Irithel", health=100, attackPower=25, armor=4)

# Perang gaes...
while True:
    layla.menyerang(irithel)
    irithel.menyerang(layla)

    if layla.health <= 0:
        print("\nLAYLA IS DEAD...")
        break
    elif irithel.health <= 0:
        print("\nIRITHEL IS DEAD...")
        break

print("\nWar is Over...")