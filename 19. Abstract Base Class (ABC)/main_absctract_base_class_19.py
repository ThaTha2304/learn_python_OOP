'''
    Module untuk belajar Abstract Class

    ABC = Abstract Base Class 
'''

from abc import ABC,abstractmethod

class Button(ABC):
    '''
        Abstract class
    '''

    @abstractmethod
    def click(self):
        '''
            Method abstract, harus diimplementasikan di class instance-nya

            kalau tidak di-implement, bakalan error
        '''
        pass

class PushButton(Button):
    '''
        Instance from abstract class
    '''
    def click(self):
        print("Push Button Click")

button1 = PushButton()
button1.click()
