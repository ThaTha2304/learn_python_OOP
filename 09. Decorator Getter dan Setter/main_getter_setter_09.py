'''
    Module untuk belajar decorator getter dan setter
'''

class Hero:
    def __init__(self, name:str, health:int, armor:int) -> None:
        self.__name = name
        self.health = health
        self.__armor = armor
        
        # Misalkan kita punya attribute untuk menampilkan summary dari object
        # self.info = f"Object:\n-name\t: {self.__name}\n-health\t: {self.health}\n-armor\t: {self.__armor}"

    '''
        Decorator @property dapat mengubah dari atribute menjadi semacam method
    '''
    @property
    def info(self):
        return f"Object:\n-name\t: {self.__name}\n-health\t: {self.health}\n-armor\t: {self.__armor}"

    @property
    def name(self):
        '''
            Property untuk attribute name
        '''
        pass

    # @<nama_decorator>.getter
    @name.getter
    def name(self):
        '''
            Method untuk getName
        '''
        return self.__name
    
    # @<nama_decorator>.setter
    @name.setter
    def name(self, inputName:str):
        '''
            Method untuk setName
        '''
        self.__name = inputName

    @name.deleter
    def name(self):
        print("Delete Name")
        self.__name = None

layla = Hero("layla", 100, 10)
print(f"Nama object: {layla.name}")
print("\nGanti nama jadi 'Hanabi'")
layla.name = "Hanabi"
print(f"Nama object modified: '{layla.name}'\n")

print("\n==== Delete Name ====")
del layla.name
print(layla.info,"\n")

badang = Hero("Badang", 120, 10)
print(badang.info)
# Kemudian dilakukan perubahan pada health misalnya
badang.health = 1000
print(badang.info) # health menjadi 1000 (berubah), menjadi dinamis...

# So, dengan menggunakan getter dan setter "pythonic way", bisa membuat seakan-akan private attribute jadi semacam public attribut...