'''
    Module untuk akses method pada super-class dengan super()

    Misal class Mage punya default health = 100, 
    sedangkan class Fighter punya default health = 250
'''

class Hero:
    '''
        Super class
    '''

    def __init__(self, name:str, health:int) -> None:
        '''
            Constructor untuk class Hero
        '''
        self.name = name
        self.health = health

    def info(self) -> None:
        '''
            Method untuk menampilkan summary dari object
        '''
        print(f"Object '{self.name}' punya health: {self.health}")

class Hero_mage(Hero):
    '''
        Sub-class dari Hero, default health = 100
    '''
    def __init__(self, name: str) -> None:
        super().__init__(name, 100)
        super().info()

class Hero_fighter(Hero):
    '''
        Sub-class dari Hero, default health = 250
    '''
    def __init__(self, name: str) -> None:
        Hero.__init__(self, name, 250)
        Hero.info(self)

# Cara akses bisa dengan menggunakan super(), atau bisa dengan memanggil nama super-classnya secara langsung
# Rekomendasi: pake super()


# Instansiasi object
lunox = Hero_mage(name="Lunox") # Object 'Lunox' punya health: 100
badang = Hero_fighter(name="Badang") # Object 'Badang' punya health: 250