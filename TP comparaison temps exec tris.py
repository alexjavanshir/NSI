# -*- coding: utf-8 -*-

def aleaT(n):
    """ int-->List[int]
    hypothèse : n>0
    retourne un tableau d'entiers tirés aléatoirement entre 1 et n"""
    from random import randint
    return [randint(1,n) for i in range(0,n)]
    
print("########################### A2. ex 2.b ###########################") 
def insere (T,i,temp):
    """List[int]*int*int-->None
    insere v dans T à l'index ? (T[0..i[ supposé trié)"""
    j=i
    while j>0 and T[j-1]>temp:
        T[j]=T[j-1]
        j=j-1
    T[j]=temp

def tri_ins(T):
    """List[int]-->None
    trie T par insertion"""
    for i in range(1,len(T)):
        insere(T,i,T[i])

print("########################### A2. ex 2.a ###########################") 
def echange(T,i,j):
    """List[int],int,int-->None
    i>=0 et j >=0
    échange les valeurs des cellules i et j"""
    temp=T[i]
    T[i]=T[j]
    T[j]=temp

def tri_sel(T):
    """List[int]-->None
    trie le tableau T par sélection"""
    for i in range(len(T)-1):
        m=i
        for j in range(i+1,len(T)):
            if T[j]<T[m]:
                m=j
        echange(T,i,m)

print("########################### compar. durée exec ###########################") 
def deepcopy(T):
    """List[int]-->List[int]
    crée une liste identique"""
    TT=[]
    for elt in T:
        TT.append(elt)
    return TT

# est-ce vrai en moyenne ? et pour des tableaux plus petits ?et plus grands ?
# modifier algo pour faire moyennes et varier la taille du tableau

#help("modules")
import time 
import math
#help(time)

x=[]
y1=[]
y2=[]
y3=[]
for i in range (1,8):
    moy1=0
    moy2=0
    moy3=0
    for j in range (5) : 
        print("pour un tableau de ",i*1000,"éléments, mesure n°",j+1,"/5")
        T=aleaT(1000*i)  # génère alétoirement un tableau de 500*i cellules
        TT = deepcopy(T) # copie le tableau pour comparaison
        TTT = T[:]       # autre méthode de copie profonde
        t1=time.perf_counter()
        tri_sel(T)
        t2=time.perf_counter()
        dt1=t2-t1  #selection
        moy1=moy1+dt1
        
        t1=time.perf_counter()
        tri_ins(TT)
        t2=time.perf_counter()
        dt2=t2-t1  #insertion
        moy2=moy2+dt2
        
#        t1=time.perf_counter()
#        TTT.sort()  
#        t2=time.perf_counter()
#        dt3=t2-t1 #sort
#        moy3=moy3+dt3
    
    x.append(1000*i*1000*i)    # ou 1000 * i * 1000 * i pour vérifier que la durée est pptionnelle à N²
    y1.append(moy1/5)
    y2.append(moy2/5)
#    y3.append(moy3/5)

import matplotlib.pyplot as plt
#help(plt)

plt.xlabel("x")
plt.ylabel("y1 et y2 (en s)")

#plt.xlim(0, 8500)
#plt.ylim(-0.5, 5)

plt.plot(x,y1,'r',marker="s",label="selection")  #mark : x
plt.plot(x,y2,'g',marker="v",label="insertion")  
#plt.plot(x,y3,'b',marker="o",label="sort")  

plt.legend()  # pour voir le label (à placer après plot)

plt.title("comparaisons tris")
plt.show()
   
# cf https://courspython.com/introduction-courbes.html




