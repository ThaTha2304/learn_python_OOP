'''
    Masih melanjutkan problem dari multiple inheritance.

    Misal terdapat super-class: class A
    class B dan class C inherit dari class A
    sedangkan class D inherit dari class B dan C

    class A, B, dan C, punya method show().
    
    Jika object D dipanggil method show(), apa yg akan terjadi?

    Ilustrasi:
        A
        /\
       B  C
       '\'/
         D
'''

class A():
    def show(self):
        print("Method show A")


class B(A):
    def show(self):
        print("Method show B")


class C(A):
    def show(self):
        print("Method show C")


class D(B,C):
    '''
        Urutan inheritancenya:
        - D
        - B (That's why method show() yg tampil punyanya B)
        - C
        - A
    '''
    pass


class E(C,B):
    '''
        Urutan inheritancenya:
        - E 
        - C (That's why method show() yg tampil punyanya C)
        - B
        - A
    '''
    pass

class F(B,C):
    '''
        Urutan inheritancenya:
        - F (That's why method show() yg tampil punyanya C)
        - C 
        - B
        - A
    '''
    def show(self):
        print("Method show E")
#Instansiasi object

d = D()
d.show() # Method show B

e = E()
e.show() # Method show C

f = F()
f.show() #Method show E