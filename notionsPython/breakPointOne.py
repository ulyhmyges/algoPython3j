# Exercice 1
import math

temps = 6.892
distance = 19.7
vitesse = distance / temps

print("la vitesse = {:.1f}".format(vitesse))

# Exercice 2
name = input("Entrez le nom: ")
age = int(input("Entrez l'âge: "))
print("{}, vous avez {} ans.".format(name, age))

# Exercice 3
number = float(input("Saisissez un flottant: "))
if number >= 0:
    racine = math.sqrt(number)
    print("{} a pour racine carré {:.1f}".format(number, racine))
else:
    print("un message d'erreur.")

# Exercice 4
mot1 = input("Saisir le premier mot: ")
mot2 = input("Saisir le second mot: ")

if mot1 < mot2:
    print("Le mot {} est plus petit que le mot {}.".format(mot1, mot2))

elif mot2 < mot1:
    print("Le mot {} est plus petit que le mot {}.".format(mot2, mot1))

else:
    print("Les mots {} e† {} sont identiques.".format(mot1, mot2))

# Exercice 5
pSeuil = 2.3
vSeuil = 7.41
pression = float(input("Saisir la pression de l'enceinte: "))
volume = float(input("Saisir le volume de l'enceinte: "))
if pression > pSeuil and volume > vSeuil:
    print("Arrêt immédiat")

elif pression > pSeuil:
    print("Augmentez le volume de l'enceinte")

elif volume > vSeuil:
    print("Diminuez le volume de l'enceinte")

else:
    print("RAS. Tout va bien")