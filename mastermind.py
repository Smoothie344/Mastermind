# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 14:43:21 2021

@author: Rebecca LAFONT, Paul CROIZET
"""

from outilsmm import *

print(18*"=" +" \n    Mastermind\n" + 18*"=")
print("Vous disposez de 10 essais pour deviner la combinaison de 4 pions")
print("Les pions peuvent être de 8 couleurs: A, B, C, D, E, F, G, H")

print(18*"=")
solution=tirage()
jeu=[]
nbr_essai = 0

while nbr_essai < 10 :
    combinaison=essai()
    ajout(combinaison,solution,jeu)
    affiche(jeu)
    nbr_essai=nbr_essai + 1
    if victoire(combinaison,solution) == True:
        break
if victoire(combinaison,solution)==False :
    print("Vous avez perdu, la solution était : ", end="")
else:
    print("Vous avez gagné en {} essais, la solution était : ".format(nbr_essai),end="")
print(solution)
