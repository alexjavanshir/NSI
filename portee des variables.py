# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:08:15 2019

@author: Olivier
"""

#####prévoir le résultat avant d'exécuter le code#######

a=3

def test0():
    """None->None
    affiche a, variable non déclarée dans la fonction"""
    print("valeur de a dans test0",a)

test0()  #attention, si a n'est pas init. en ligne 9, test0 provoque une erreur !

#####prévoir le résultat avant d'exécuter le code#######

def test1(a):
    """int->None
    modifie la valeur de a, variable locale sans la retourner"""
    a=1
    print("valeur de a dans test1",a,id(a))

print("avant test1",a,id(a))
test1(a)
print("après appel de test1",a,id(a))

#####prévoir le résultat avant d'exécuter le code#######

def test2(a):
    """int->int
    modifie la valeur de la variable locale a et la retourne"""
    print("valeur de a dans test2",a,id(a))
    a=4
    print("nouvelle valeur de a dans test2",a,id(a))   
    return a

a=test2(a)
print("après appel de test2",a,id(a))

#####prévoir le résultat avant d'exécuter le code#######

def test3():
    """None->None
    modifie la valeur de a (variable globale)"""
    b=10

test3()
try : 
    print("b = ",b)   #provoque une erreur car b n'existe pas en dehors de test3
except (NameError):
    print("b n'existe pas et ne peut donc pas être affiché")

#####prévoir le résultat avant d'exécuter le code#######

def test4():
    """None->None
    modifie la valeur de a (variable globale)"""
    global a
    print("valeur de a dans test4",a,id(a))
    a=5
    print("nouvelle valeur de a dans test4",a,id(a))    

test4()
print("après appel de test4",a,id(a))

