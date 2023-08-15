'''
    Module untuk belajar Private Variable di OOP
'''

class Hero:
    # Class Variabel
    jumlah = 0

    def __init__(self, name:str, health:int) -> None:
        self.name = name
        self.health = health
    
        # Private variable (underscore '_' ada 2)
        self.__exp = 100

        # Protected Variable (underscore '-' ada 1)
        self._level = 10

layla = Hero(name="Layla", health=100)

print(layla.__dict__) # {'name': 'Layla', 'health': 100, '_Hero__exp': 100, '_level': 10} --> ada variabel private dan protected

# Coba akses global variabel (public)
print(layla.health) # 100

# Coba akses private variabel
# print(layla.__exp) # AttributeError: 'Hero' object has no attribute '__exp'

# Coba akses protected variable
print(layla._level) # 10