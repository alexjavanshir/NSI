# -*- coding: utf-8 -*-
### copie de list  sans "copy" en itérant sur les élts ##

L=[0,1,2,3,4,5,6,7,8]
P=[0]*9

for i in range (len(L)):
    P[i]=L[i]
print(L==P)
P[0]=4
print(P,L)

### fonctions et passage par valeur / référence ######

obj="text"
def toto(obj):
    print(id(obj))
    obj=obj+"e"
toto(obj)
print(obj,id(obj))


obj=[1,2,3,4]
def toto2(obj):
    print(id(obj))
    obj.append(5)
toto2(obj)
print(obj,id(obj))

### découper chaine en liste d'éléments ########
txt="ceci est une chaine de caractères"
L=txt.split(" ")
print(L)

### créer une chaine à partir d'une liste ########
L=['b','o','n','j','o','u','r']
chaine=".".join(L)
print(chaine)