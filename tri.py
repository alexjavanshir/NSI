import sys
import random
from timeit import default_timer as timer
import time
import matplotlib.pyplot as plt

DEBUG=False

#---------------------------------------------------------------
# Genère une liste d'entiers
#  - Paramètre d'entrée: La taille de la liste
#  - Paramètre de sortie: La liste généré 
#---------------------------------------------------------------
def genere_list(taille):
    if (DEBUG): print("Generation d'une Liste de nombre alétoires")
    liste = [random.randrange(1, 1000, 1) for i in range(taille)]
    return liste

#---------------------------------------------------------------
# Vérifier si une liste est triée ou non
#  - Paramètre d'entrée: La liste à vérifier
#  - Paramètre de sortie: True si triée, False sinon
#---------------------------------------------------------------
def est_triee(liste):
    for i in range(len(liste)-1):
        if liste[i] > liste[i+1]:
            return False
    return True

#---------------------------------------------------------------
# Trier une liste en utilisant le tri par selection
#  - Paramètre d'entrée: La liste à trier
#  - Paramètre de sortie: La liste tiée
#---------------------------------------------------------------
def tri_selection(liste):
    debut = time.perf_counter()
    
    for i in range(len(liste)):
        # Trouver le min
        min = i
        for j in range(i+1, len(liste)):
            if  liste[j] <liste[min]:
                min = j
                    
        if (min != i):
            tmp = liste[i]
            liste[i] = liste[min]
            liste[min] = tmp
    
    fin = time.perf_counter()
    duree = fin-debut

    return liste, duree

#---------------------------------------------------------------
# Trier une liste en utilisant le tri par insertion
#  - Paramètre d'entrée: La liste à trier
#  - Paramètre de sortie: La liste tiée
#---------------------------------------------------------------
def tri_insertion(liste):
    debut = time.perf_counter()
    
    for i in range(1, len(liste)): 
        valeur_i = liste[i] 
        j = i-1
        while j >= 0 and liste[j] > valeur_i : 
                liste[j + 1] = liste[j] 
                j -= 1
        liste[j + 1] = valeur_i

    fin = time.perf_counter()
    duree = fin-debut
    
    return liste, duree

#---------------------------------------------------------------
# Fusionne
#  - Paramètre d'entrée: La liste à trier
#                        Borne inferieur
#                        Milieu
#                        Born supérieur 
#  - Paramètre de sortie: La liste tiée
#--------------------------------------------------------------- 
def fusionne(liste, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 

    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 

    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = liste[l + i] 

    for j in range(0 , n2): 
        R[j] = liste[m + 1 + j] 

    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 

    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            liste[k] = L[i] 
            i += 1
        else: 
            liste[k] = R[j] 
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        liste[k] = L[i] 
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        liste[k] = R[j] 
        j += 1
        k += 1

#---------------------------------------------------------------
# Trier une liste en utilisant le tri par fusion
#  - Paramètre d'entrée: La liste à trier
#                        Borne inferieur
#                        Born supérieur 
#  - Paramètre de sortie: La liste tiée
#--------------------------------------------------------------- 
def tri_fusion(liste,l,r): 
    debut = time.perf_counter()
    
    if l < r: 

        # Same as (l+r)//2, but avoids overflow for 
        # large l and h 
        m = (l+(r-1))//2

        # Sort first and second halves 
        tri_fusion(liste, l, m) 
        tri_fusion(liste, m+1, r) 
        fusionne(liste, l, m, r) 
    
    fin = time.perf_counter()
    duree = fin-debut

    return liste, duree

#---------------------------------------------------------------
# Programme principale 
#---------------------------------------------------------------
def main():

    tailleListe = 8
    
    if (len(sys.argv) == 2):
        tailleListe = int(sys.argv[1])

    nombreTests = 10

    # x axis values 
    tailles = list(range(1000, 21000, 1000))
    # tempsSelection = []
    # tempsInsertion = []
    tempsFusion = []

    for tailleListe in tailles:
        # tempsTotalSelection=0
        # tempsTotalInsertion=0
        tempsTotalFusion=0

        for j in range(nombreTests):

            listeNonTriee = genere_list(tailleListe)
            if (DEBUG):
                print ("Liste à trier : " +  str(listeNonTriee))
                print ("\nLa liste est triée: {0}".format(est_triee(listeNonTriee)))

            # listeTrieeParSelection, dureeSelection = tri_selection(listeNonTriee.copy())
            # tempsTotalSelection += dureeSelection
            # if (DEBUG):
            #     print ("\nListe triée par selection : {0}".format(listeTrieeParSelection))
            #     print ("\t* Tri par selection effectuée en : {0:.5g} s.\n".format(dureeSelection))

            # listeTrieeParInsertion, dureeInsertion = tri_insertion(listeNonTriee.copy())
            # tempsTotalInsertion += dureeInsertion
            # if (DEBUG):
            #     print ("Liste triée par insertion : " +  str(listeTrieeParInsertion))
            #     print ("\t* Tri par insertion effectuée en : {0:.5g} s.\n".format(dureeInsertion))

            listeTrieeParFusion, dureeFusion = tri_fusion(listeNonTriee.copy(),0, tailleListe-1)
            tempsTotalFusion += dureeFusion
            if (DEBUG):
                print ("Liste triée par fusion : " +  str(listeTrieeParFusion))
                print ("\t* Tri par fusion effectuée en : {0:.5g} s.\n".format(dureeFusion))
        
        print("\nN: " + str(tailleListe))

        # print ("--> Temps selection Moyen={0:.5g} s.".format(tempsTotalSelection/nombreTests))
        # print ("--> Temps insertion Moyen={0:.5g} s.".format(tempsTotalInsertion/nombreTests))
        print ("--> Temps fusion Moyen={0:.5g} s.".format(tempsTotalFusion/nombreTests))

        # tempsSelection.append(tempsTotalSelection/nombreTests)
        # tempsInsertion.append(tempsTotalInsertion/nombreTests)
        tempsFusion.append(tempsTotalFusion/nombreTests)

    plt.title('Tri de listes par differents algorithmes') 

    plt.xlabel('Taille Tableau') 
    plt.ylabel('Temps de Tri (secondes)') 
    
    # plt.plot(tailles, tempsSelection, label = "Tri par Selection") 
    # plt.plot(tailles, tempsInsertion, label = "Tri par Insertion") 
    plt.plot(tailles, tempsFusion, label = "Tri par Fusion") 
    
    # complexite=[]
    # coef = tempsSelection[0] / tailles[0]**2
    
    # for x in tailles:
    #     valeur = coef*x*x
    #     complexite.append(valeur)
    
    # plt.plot(tailles, complexite, label = "Complexite N^2") 

    plt.legend() 
    plt.show() 

if __name__ == "__main__":
    main()