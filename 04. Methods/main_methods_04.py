'''
    Module untuk belajar methods (function) pada OOP
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
    
    # Method dengan argument
    def heal(self, potion:int) -> None:
        '''
            Method dengan argument untuk menambah jumlah health
        '''
        self.health += potion
    
    # Method dengan return
    def getArmor(self) -> int:
        '''
            Method dengan return jumlah armor object
        '''
        return self.armor
    
    # Method dengan argument dan return
    def attackUp (self, attackBonus: int) -> int:
        '''
            Method kombinasi antara argument dengan return
        '''
        self.attackPower += attackBonus
        return self.attackPower
    
layla = Hero(name="Layla", health=100, attackPower=20, armor=10)

layla.summary()

print(f"\nHealth Layla before heal: {layla.health}") # 100
layla.heal(20)
print(f"Health Layla after heal: {layla.health}") # 120

print(f"\nArmor layla: {layla.getArmor()}")

print(f"\nAttack Power Layla before buff: {layla.attackPower}") # 20
layla.attackUp(25)
print(f"Attack Power Layla after buff: {layla.attackPower}") # 45

