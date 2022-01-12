# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:06:48 2021

@author: Rebecca LAFONT, Paul CROIZET
"""

from random import randint
pion = ["A","B","C","D","E","F","G","H"]


def tirage():
    return "".join([pion[randint(0,7)],pion[randint(0,7)],pion[randint(0,7)],pion[randint(0,7)]])

def essai():
    combinaison = input("Essai : ")
    if valide(combinaison) == True:
        return combinaison
    else:
        print("Combinaison incorrecte, vous avez perdu un essai !")
        return '****'
    
    
def affiche(jeu):
    print("---------------------")
    for i in range(len(jeu)):
        print(" {0:2} : {1}  ={2}  *{3}".format(i+1," ".join(jeu[i][0]),jeu[i][1],jeu[i][2]))
    print("---------------------")
    

def bienplace(combinaison,solution):
    L1=combinaison.upper()
    L2=solution
    a=0
    for i in range (len(L1)):
        if L1[i]==L2[i]:
            a=a+1
    return a

def malplace(combinaison,solution):
    L1=list(combinaison.upper())
    L2=list(solution)
    b=0
    for i in range(len(L1)):
        if L1[i]==L2[i]:
            L1[i]='*'
            L2[i]='!'
        else:
            None
    for i in range(len(L1)):
        if L1[i] in L2:
            b = b+1
            L2[L2.index(L1[i])]='!'
        else:
            None        
    return b


def victoire(combinaison,solution):
    if solution == combinaison.upper():
        return True
    else:
        return False
    
def valide(combinaison):
    L1=combinaison
    if len(L1)==4:
        L1up=L1.upper()
        for i in range(len(L1up)):
                if pion.count(L1up[i])==0:
                    return False
                else:
                    None
        return True
    else:
        return False
    
def ajout(combinaison,solution,jeu):
    jeu.append([combinaison.upper(),bienplace(combinaison,solution),malplace(combinaison,solution)])

#Section test :

if __name__ == "__main__":
    print("Test de la fonction bienplace avec :\nsolution = 'ABCD'\ncombinaison = 'aBdC'")
    print("Résultat attendu : 2")
    valeur = bienplace('aBdC','ABCD')
    if valeur==2:
        print("OK")
    else:
        print("NOK")
        
    print("\n\n")
    
    print("Test de la fonction malplace avec :\nsolution = 'ABCD'\ncombinaison = 'aBdC'")
    print("Résultat attendu : 2")
    valeur = malplace('aBdC','ABCD')
    if valeur==2:
        print("OK")
    else:
        print("NOK")
        
    print("\n\n")
    
    print("Test de la fonction victoire avec :\nsolution = 'ABCD'\ncombinaison = 'aBCd'\net combinasion = 'efgH'")
    print("Résultat attendu : True pour le premier test et False pour le second")
    valeur = victoire('aBCd','ABCD')
    if valeur==True:
        print("OK")
    else:
        print("NOK")
    valeur = victoire('efgH','ABCD')
    if valeur==False:
        print("OK")
    else:
        print("NOK")
        
    print("\n\n")
    
    print("Test de la fonction valide avec : 'abcde', 'abgM', 'aBdC'")
    print("Résultat attendu : False, False et True")
    if valide("abcde")==False and valide("abgM")==False and valide("aBdC")==True:
        print("OK")
    else:
        print("NOK")
        
    print("\n\n")
    
    