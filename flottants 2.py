def encode(valeur,base):
    """ int*int -->String
    hyp valeur >=0
    hypothèse : base maxi = 16
    """
    chaine=""
    if valeur>255 or valeur<0 : 
        return ""
    for n in range (1,9) :
        calcul = valeur % base
        if (calcul)>9:
            if calcul==10:
                bit='A'
            if calcul==11:
                bit='B'
            if calcul==12:
                bit='C'
            if calcul==13:
                bit='D'
            if calcul==14:
                bit='E'
            if calcul==15:
                bit='F'
        else :
            bit=calcul
        chaine =str(bit)+chaine
        valeur = valeur // base
        n+=1
    return (chaine)

def encode2(valeur,base):
    """ float*int -->String avec 16 décimales
    hypothèse : base maxi = 16
    """
    chaine=""
    for n in range (1,17) :
        valeur=valeur*base
        calcul = int(valeur)
        if (calcul)>9:
            if calcul==10:
                bit='A'
            if calcul==11:
                bit='B'
            if calcul==12:
                bit='C'
            if calcul==13:
                bit='D'
            if calcul==14:
                bit='E'
            if calcul==15:
                bit='F'
        else :
            bit=calcul      
        chaine =chaine+str(bit)
        valeur = valeur - int(valeur)
    return (chaine)

def conv_10_Vers_B(nombre,base):
    """float*int-->String
    convertit de 10 vers b
    hyp b max = 16"""
    chaine=""
    #gestion de la partie entière
    entier=int(nombre)
    chaine=encode(entier,base)

    #gestion de la partie décimale
    chaine=chaine+"."
    decimal=nombre-entier
    chaine=chaine+encode2(decimal,base)

    return (chaine)

print(conv_10_Vers_B(16.625,2))
print(conv_10_Vers_B(63.734375,16))
print(conv_10_Vers_B(231.70314025878906,4))
print(conv_10_Vers_B(.1,2))
print(conv_10_Vers_B(.2,2))
print(conv_10_Vers_B(.3,2))
print("------------------------------------------------")

def decode2(chaine,base):
    """ String * int --> float
    hypothèse : chaine est constitué de 'bits' allant de 0 à base-1
    retourne la valeur dans la base 10 de chaine exprimé en base base"""
    valeur = 0
    i=1
    for elt in chaine :
        if elt == 'A':
            valeur = valeur + 10/base**i
        elif elt == 'B':
            valeur = valeur + 11/base**i
        elif elt == 'C':
            valeur = valeur + 12/base**i
        elif elt == 'D':
            valeur = valeur + 13/base**i
        elif elt == 'E':
            valeur = valeur + 14/base**i
        elif elt == 'F':
            valeur = valeur + 15/base**i
        else : 
            valeur = valeur + int(elt)/base**i
        i=i+1
    return (valeur)

def decode(chaine,base):
    """ String * int --> float
    hypothèse : chaine est constitué de 8 caractères
    retourne la valeur dans la base 10 de chaine exprimé en base base"""
    valeur = 0
    i=1
    for elt in chaine :
        if elt=='A':
            valeur = valeur + 10*base**(8-i)
        elif elt == 'B':
            valeur = valeur + 11*base**(8-i)
        elif elt== 'C':
            valeur = valeur + 12*base**(8-i)
        elif elt== 'D':
            valeur = valeur + 13*base**(8-i)
        elif elt == 'E':
            valeur = valeur + 14*base**(8-i)
        elif elt == 'F':
            valeur = valeur + 15*base**(8-i)
        else : 
            valeur = valeur + int(elt)*base**(8-i)
        i=i+1
    return (valeur)

def conv_B_Vers_10(chaine,base):
    """String * int--> float
    convertit de b vers 10"""
    #decoupage en 2 parties de la chaine séparateur .
    L = chaine.split(".")
    chaine1=L[0]
    chaine2=L[1]
    #gestion de la partie entière
    valeur = decode(chaine1,base)

    #gestion de la partie décimale
    valeur = valeur + decode2(chaine2,base)

    return (valeur)
print("00003213.23100001",conv_B_Vers_10("00003213.23100001",4))

print(conv_10_Vers_B(11.11,2))

print(      conv_B_Vers_10("0000000B.1C28F5C28F5C0000",2)    )









