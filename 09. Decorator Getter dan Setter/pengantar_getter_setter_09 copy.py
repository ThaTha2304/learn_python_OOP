'''
    Module untuk belajar decorator getter dan setter
'''

class Hero:
    def __init__(self, name:str, health:int, armor:int) -> None:
        self.__name = name
        self.health = health
        self.__armor = armor
        
        # Misalkan kita punya attribute untuk menampilkan summary dari object
        self.info = f"Object:\n-name\t: {self.__name}\n-health\t: {self.health}\n-armor\t: {self.__armor}"

layla = Hero("layla", 100, 10)
badang = Hero("Badang", 120, 10)
# Menampilkan informasi summary object
print(layla.info)
#  Ada kelemahan, yakni bisa dilakukkan assign dengan nilai tertentu
layla.info = "info"
print(layla.info) # output --> info

# Selain itu, ada kelemahan yg lain, yakni tidak dapat melakukan update data secara dinamis
print(badang.info)
# Kemudian dilakukan perubahan pada health misalnya
badang.health = 1000
print(badang.info) # health tetap 120 (nilai awal)

# Oleh karena itu, digunakan property getter dan setter

