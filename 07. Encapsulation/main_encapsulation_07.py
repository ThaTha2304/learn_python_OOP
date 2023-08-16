'''
    Module untuk belajar Encapsulation

    Class yg ter-enkapsulasi itu gimana sih?
    - Semua variabelnya private
    - Variabel diakses dengan method getter dan setter
'''

class Hero:
    '''
        Contoh class yang menerapkan prinsip encapsulation
    '''

    def __init__(self, name: str, health: int) -> None:
        '''
            Constructor untuk membuat object, attribute private
        '''
        self.__name = name
        self.__health = health

    # Getter Method
    def getName(self) -> str:
        '''
            Get name
        '''
        return self.__name
    
    def getHealth(self) -> int:
        '''
            Get health
        '''
        return self.__health
    
    # Setter method
    def setName(self, name:str) -> None:
        '''
            Set name baru
        '''
        self.__name = name

    def setHealth(self, health:int) -> None:
        '''
            Set health baru
        '''
        self.__health = health


layla = Hero(name="Layla", health=100)
print(f"Nama object: {layla.getName()} punya health: {layla.getHealth()}")
print("\nSet nama baru jadi 'Sniper' dan health jadi 250")
# Set name
layla.setName("Sniper")
# Set Health
layla.setHealth(250)
print(f"\nModified: \nNama object: {layla.getName()} punya health: {layla.getHealth()}")