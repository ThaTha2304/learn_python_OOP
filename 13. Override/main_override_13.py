'''
    Module untuk belajar override (Menimpa) method
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

    def showInfo(self) -> None:
        '''
            Method untuk menampilkan summary dari object
        '''
        print("\nshowInfo dari super-class")
        print(f"Object '{self.name}': \n-health: {self.health}")


class Hero_mage(Hero):
    '''
        Sub-class dari Hero, default health = 100
    '''
    def __init__(self, name: str) -> None:
        super().__init__(name, 100)

    # Override
    def showInfo(self) -> None:
        print("\nshowInfo dari Hero_mage")
        print(f"Object '{self.name}': \n-type: Mage\n-health: {self.health}")


class Hero_fighter(Hero):
    '''
        Sub-class dari Hero, default health = 250
    '''
    def __init__(self, name: str) -> None:
        super().__init__(name, 250)


lunox = Hero_mage(name="Lunox")
badang = Hero_fighter(name="Badang")

lunox.showInfo() # showInfo yg dipake adalah yg di Hero_mage (override method dari super-class)
badang.showInfo() # showInfo yg dipake adalah yg di super-class (tdk override, karena di sub-class tidak didefinisikan method showInfo() )