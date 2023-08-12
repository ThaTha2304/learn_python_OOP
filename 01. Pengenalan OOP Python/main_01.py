'''
    Module berisi pengenalan OOP
'''

# Pembuatan class dengan nama "Hero"
class Hero:
    '''
        Class Hero, contoh pembuatan class
    '''
    # pass --> class ini belum ada atribut/method apapun (kosong)
    pass

# Pembuatan object
hero1 = Hero()

# Assign atribute ke object (Bakalan ada error, tapi masih bisa jalan programnya)
hero1.name = "Layla"
hero1.health = 100

print(hero1) # <__main__.Hero object at 0x000001D70C00E750>
print(hero1.__dict__) # {'name': 'Layla', 'health': 100}

hero2 = Hero()

hero2.name = "Mozart"
hero2.health = 200
print(hero2) 
print(hero2.__dict__) # {'name': 'Mozart', 'health': 200}
