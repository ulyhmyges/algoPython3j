import math
import re

def verifMail(chaine):
    arobase = 0
    for char in chaine:
        if char == "@":
            arobase += 1
    if len(chaine) > 4 and chaine[len(chaine) - 4] == "." and arobase == 1:
        l = list(chaine)
        l.reverse()
        for i, letter in enumerate(l):
            if i < 3 and (letter == "." or letter == "@"):
                #print("not a email address valid at line {} of the file {}".format(line, nameFile))
                return False
        #print("Valid email address")
        return True
    else:
        #print("not email address at line {} of the file {}".format(line, nameFile))
        return False


### Exercice 21
print("##### Exercice {} #####".format(21))
"""
x = int(input("Saisir un nombre : "))
fichier = open("data.txt", "w")

for i in range(x):
    chaine = input("Saisir une chaîne de caractères :")
    fichier.write(chaine)
    fichier.write("\n")

fichier.close()
"""

### Exercice 22
print("##### Exercice {} #####".format(22))

try:
    nameFile = "data.txt"
    fichier = open(nameFile, "r")
    myfile = fichier.read().split("\n")
    mailLine = []
    line = 0
    for chaine in myfile:
        if verifMail(chaine):
            mailLine.append(line)
        elif len(chaine) != 0 and not verifMail(chaine):
            print("Not a email address valid at line {} of the file {} => {}".format(line, nameFile, chaine))
        line += 1
    print("Fin de lecture des {} lignes du fichier {}.".format(line, nameFile))
    print("{} email address found, youpi!".format(len(mailLine)))

finally:
    # the file will be closed even if an exception occurs
    fichier.close()

### Exercice 23
print("##### Exercice {} #####".format(23))

chaine = "la vue est belle et belle est la vue comme sur cette vue dans la ville mais en montagne la vue est-elle la même."
def compterMots(chaine):
    """
    renvoie un dictionnaire de fréquence des mots de chaine
    :param chaine: str
    :return: dict
    """
    dico = {}
    wordsList = re.split(r"\s|\.|\-", chaine)
    if len(wordsList[len(wordsList) - 1]) == 0: # enlève le dernier élément de la liste si vide
        wordsList.pop()
    for word in wordsList:
        count = 0
        for index in range(len(wordsList)):
            if wordsList[index] == word:
                count += 1
        dico[word] = count
    return dico

print(compterMots(chaine))

### Exercice 24
print("##### Exercice {} #####".format(24))

def volumeSphere(rayon):
    return 4 * math.pi * math.pow(rayon, 3) / 3

rayon = float(input("Saisir un rayon pour une sphère: "))
print("Pour R = {}, le volume de la sphère = {:.1f}".format(rayon, volumeSphere(rayon)))

### Exercice 25
print("##### Exercice {} #####".format(25))

tutu = (5, 10, 12)
def somme(s, t):
    if len(t) > 0:
        s += t[0]
        return somme(s, t[1:])
    return s

print(somme(0, tutu))

