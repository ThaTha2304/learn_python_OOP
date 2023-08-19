'''
    Module untuk belajar inheritance.

    Misal kita punya super-class Hero. Class ini punya beberapa attribute seperti
    name dan health. Hero ini bisa punya banyak jenis, ada Hero Mage, Hero Marksman, dsb.

    Hero Mage dan Hero Marksman itu pada dasarnya adalah Hero yang dimodifikasi attributenya, misal Mage punya 
    magicPower lebih gedhe dan Marksman punya attPower yang lebih gedhe. Kedua class ini disebut sebagai sub-class
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

# class <nama_sub-class>(<nama_super-class>)
class Hero_mage(Hero):
    '''
        Sub-class dari Hero
    '''
    pass

class Hero_marksman(Hero):
    '''
        Sub-class dari Hero
    '''
    pass


# Instansiasi Objek
nana = Hero(name="Layla", health=100)
print(nana.__class__) # <class '__main__.Hero'>

hanabi = Hero_marksman(name="Hanabi", health=100)
print(hanabi.__class__) # <class '__main__.Hero_marksman'>

lunox = Hero_mage(name="Lunox", health=100)
print(lunox.__class__) # <class '__main__.Hero_mage'>