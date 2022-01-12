# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:06:48 2021

@author: Rebecca Lafont Paul Croizet
"""

from random import randint
pion = ["A","B","C","D","E","F","G","H","I","J","K","L","*"]


def tirage(n):
    return "".join([pion[randint(0,n-1)],pion[randint(0,n-1)],pion[randint(0,n-1)],pion[randint(0,n-1)]])

def essai(n):
    combinaison = input("Essai : ")
    if valide(combinaison,n) == True:
        return combinaison
    else:
        print("Combinaison incorrecte, vous avez perdu un essai !")
        return '****'
    
    
def affiche(jeu):
    print("---------------------")
    for i in range(len(jeu)):
        print(" {0:2} : ".format(i+1), end="")
        for k in range(4):
            print(transcription_couleur(jeu[i][0][k]),end=" ")
        print(" ={0}  *{1}".format(jeu[i][1],jeu[i][2]))
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
    
def valide(combinaison,n): 
    L1=combinaison
    if len(L1)==4:
        L1up=L1.upper()
        pionN=[]
        for i in range(n):
            pionN.append(pion[i])
        for i in range(len(L1up)):
                if pionN.count(L1up[i])==0:
                    return False
                else:
                    None
        return True
    else:
        return False
    
def ajout(combinaison,solution,jeu):
    jeu.append([combinaison.upper(),bienplace(combinaison,solution),malplace(combinaison,solution)])
    
def transcription_couleur(caract): # on rentre un caractère et il ressort le code pour coder la couleur du caractère
    x = 30 + pion.index(caract)
    if x == 42 :                 # on a voulu optimiser au maximum les couleurs, mais pour certaines on les a chosies à la main 
        return caract            # car les couleurs ne se voyaient pas
    elif x==41:
        x=37
        return '\x1b[1;'+str(x)+';44m' + caract + '\x1b[0m'
    elif x>= 38:
        x = x + 2
        return '\x1b[1;'+str(x)+';1m' + caract + '\x1b[0m'
    else :
        return '\x1b[1;'+str(x)+';1m' + caract + '\x1b[0m'
    

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
    
    print("Test de la fonction malplace avec :\nsolution = 'ABCD'\ncombinaison = 'aDdC'")
    print("Résultat attendu : 2")
    valeur = malplace('aDdC','ABCD')
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
    
    print("Test de la fonction valide avec : 'IjKl', 'ghiJ', aBdH")
    print("En prenant les caractères valide jusqu'à J (soit n = 10) ")
    print("Résultat attendu : False, True et True")
    if valide("iJkL")==False and valide("ghiJ",10)==True and valide("aBdH",10)==True:
        print("OK")
    else:
        print("NOK")
        
    print("\n\n")
    
    print("Test de la fonction tirage pour un n donné, on chosit n : 8,10,12")
    print("On regarde avec la fonction valide si le tirage est valide")
    print("Résultat attendu : True, True et True")
    if valide(tirage(8),8)==True and valide(tirage(10),10)==True and valide(tirage(12),12)==True:
        print("OK")
    else:
        print("NOK")

    print("\n\n")
    
    print("Test de la fonction transcription_couleur pour les caractères : *,A,J,H")
    print("On regarde ici si la fonction renvoie bien le code qui est associé à la lettre")
    if transcription_couleur('*') == '*':
        print("OK")
    else:
        print("NOK")
    if transcription_couleur('A') == '\x1b[1;30;1mA\x1b[0m':
        print("OK")
    else:
        print("NOK")
    if transcription_couleur('J') == '\x1b[1;41;1mJ\x1b[0m':
        print("OK")
    else:
        print("NOK")
    if transcription_couleur('H') == '\x1b[1;37;1mH\x1b[0m':
        print("OK")
    else:
        print("NOK")
    
    