'''
    Method resolution order dapat diketahui dari "help(<nama_object>)"

    Misal class A dan class B mempunyai method yg sama, yakni 'show()'
    Kemudian, class C inherit dari class A dan class B
    Jika object C dipanggil method show(), apa yg akan terjadi?
'''

class A():
    def show(self):
        print("Method show A")


class B():
    def show(self):
        print("Method show B")


class C(A,B):
    '''
        Urutan inheritancenya:
        - C
        - A (That's why method show() yg tampil punyanya A)
        - B
    '''
    pass


class D(B,A):
    '''
        Urutan inheritancenya:
        - D
        - B (That's why method show() yg tampil punyanya B)
        - A
    '''
    pass


class E(A,B):
    '''
        Urutan inheritancenya:
        - E (That's why method show() yg tampil punyanya E, karena dia di-define sendiri di class E)
        - A 
        - B
    '''
    def show(self):
        print("Method show E")


#Instansiasi object
c = C()
c.show() #Method show A

d = D()
d.show() # Method show B

e = E()
e.show() # Method show C