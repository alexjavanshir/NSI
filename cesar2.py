import sys


#---------------------------------------------------------------
# Chiffre un test avec la méthode César
#  - Paramètre d'entrée:  -Texte à chiffrer
#                         -Code césar (Entre 1 et 25) 
#  - Paramètre de sortie: Le text chifré
#---------------------------------------------------------------
def cesar(texte, code):

    text_chiffre = ""
    offset=ord('A')

    for mot in texte.split(): 
        for lettre in mot:
            text_chiffre += chr(((ord(lettre)-offset+code) % 26) + offset)
        text_chiffre += " "

    return text_chiffre

#---------------------------------------------------------------
# Chiffre un test avec la méthode César
#  - Paramètre d'entrée:  -Texte à chiffrer
#                         -Code césar (Entre 1 et 25) 
#  - Paramètre de sortie: Le text chifré
#---------------------------------------------------------------
def cesar2(texte, code):

    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    offset=ord('A')
    correspondance={}
    i=0
    for elem in alphabet:
        correspondance[elem]=i
        i=i+1

    text_chiffre = ""

    for lettre in texte:
        position = (correspondance[lettre]+code) % 26
        text_chiffre += chr(position+offset)

    return text_chiffre


#------------------------------------------------------------------
# Main
#------------------------------------------------------------------

if (len(sys.argv) == 3):
        nomFichier = sys.argv[1]
        code = int(sys.argv[2])
        if (code <1 or code > 25):
            print("Le code doit être compris entre 1 et 25")
            exit(1)
else:
        print("Usages: cesar.py <fichier> <code cesar>")
        exit(1)

fichier = open(nomFichier, "r", encoding='utf-8')
texteChiffre= fichier.read()

print (cesar(texteChiffre, code))