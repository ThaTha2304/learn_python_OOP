'''
    Module berisi pengenalan Consturctor (__init__)
'''

# Pembuatan class dengan nama "Test" --> coba constructor
class Test:
    def __init__(self) -> None:
        '''
            Constructor
        '''
        print("Hello World from Constructor")


# Ketika objek dibuat, maka dia akan menjalankan constructornya (function __init__)
test1 = Test() # akan keluar tulisan: Hello World from Constructor

# Pembuatan class dengan nama "Hero"
class Hero:
    '''
        Class Hero, contoh pembuatan class dengan constructor
    '''
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health


# Pembuatan object, langsung dimasukkan parameter constructornya
hero1 = Hero("Layla", 100)
print(hero1.__dict__) # {'name': 'Layla', 'health': 100}

hero2 = Hero("Irithel", 250)
print(hero2.__dict__) # {'name': 'Layla', 'health': 100}