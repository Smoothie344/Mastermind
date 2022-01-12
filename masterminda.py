# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 14:43:21 2021

@author: Rebecca Lafont Paul Croizet
"""

from outilsmma import *
pion = ["A","B","C","D","E","F","G","H","I","J","K","L","*"]
print(18*"=" +"\n    Mastermind\n" + 18*"=")

while True :
    n = int(input("Avec combien de pions voulez vous jouer (4 à 12) : "))
    print(n)
    if n>=4 and n<=12:
        break
    else:
        print("Il doit y avoir une erreur.....")

while True :
    nbr_essai_joueur = int(input("Avec combien d'essais voulez vous jouer (5 à 30) : "))
    if nbr_essai_joueur>=5 and nbr_essai_joueur<=30:
        break
    else:
        print("Il doit y avoir une erreur.....")

print("\n" + 18*"=")        
print("Vous disposez de {} essais pour deviner la combinaison de 4 pions".format(nbr_essai_joueur))
print("Les pions peuvent être de {} couleurs : ".format(n), end="")
for i in range(n-1):
    print(transcription_couleur(pion[i]), end=", ")
print(transcription_couleur(pion[n-1]))
print(18*"=")  

solution=tirage(n)
jeu=[]
nbr_essai = 0
while nbr_essai < nbr_essai_joueur :
    combinaison=essai(n)
    ajout(combinaison,solution,jeu)
    affiche(jeu)
    nbr_essai=nbr_essai + 1
    if victoire(combinaison,solution) == True:
        break
if victoire(combinaison,solution)==False :
    print("Vous avez perdu, la solution été : ",end="")
else:
    print("Vous avez gagné en {} essais, la solution était bien : ".format(nbr_essai),end="")
for k in range(4):
    print(transcription_couleur(solution[k]),end=" ")
