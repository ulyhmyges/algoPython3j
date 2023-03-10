import typing
from copy import deepcopy
from typing import Any
from typing_extensions import Self


class AB:
    def __init__(self, racine=None, gauche=None, droite=None):
        self.racine = racine  # liste
        self.gauche = gauche  # AB
        self.droite = droite  # AB

    def __str__(self):
        return "\n-----\nRacine: {}\nArbre gauche: {}\nArbre droite: {}\n-----".format(self.racine, self.gauche,
                                                                                       self.droite)

    def estVide(self) -> bool:
        """
        renvoie True si l'arbre est est un arbre vide
        :return: booléen
        """
        if self.racine == None:
            return True
        else:
            return False

    def taille(self) -> int:
        """
        Donna la taille de l'arbre, le nombre total de noeuds
        :return: int
        """
        if self.estVide():
            return 0
        else:
            return 1 + (self.gauche.taille() if self.gauche else 0) + (self.droite.taille() if self.droite else 0)

    def hauteur(self) -> int:
        """
        Donne la hauteur de l'arbre
        :return: int
        """
        if self.estVide():
            return -1
        else:
            return 1 + max((self.gauche.hauteur() if self.gauche else -1),
                           (self.droite.hauteur() if self.droite else -1))

    def estEquilibre(self) -> bool:
        """
        Détermine si l'arbre est équilibré
        :return: booléen
        """
        if self.estVide():
            return True
        elif self.gauche == None and self.droite == None:
            return self.bonDelta()
        elif self.gauche == None:
            if self.bonDelta():
                return self.droite.bonDelta()
            return False
        elif self.droite == None:
            if self.bonDelta():
                return self.gauche.bonDelta()
            return False
        else:
            if self.bonDelta():
                return self.gauche.bonDelta() and self.droite.bonDelta()
            return False

    def bonDelta(self) -> bool:
        if self.deltaHauteur() > 1 or self.deltaHauteur() < -1:
            return False
        else:
            return True

    def deltaHauteur(self) -> int:
        if self.estVide():
            return -1
        else:
            return (self.gauche.hauteur() if self.gauche else -1) - (self.droite.hauteur() if self.droite else -1)

    def ABR(self) -> bool:
        """
        Détermine si l'arbre est un arbre de recherche (ABR)
        :return: booléen
        """
        isABR = True
        infixe = self.infixe().split(" ")
        liste = [int(i) for i in infixe if i.isdigit()]
        for i in range(1, len(liste)):
            if liste[i] <= liste[i - 1]:
                isABR = False
        return isABR

    def fromFileGrowABR(self, pathFile: str) -> Self:
        """
        construit et retourne un arbre de type AB à partir d'un fichier
        :param pathFile: chemin du fichier contenant un parcours préfixe
        :return: AB (arbre)
        """
        try:
            file = open(pathFile, "r")
            self = self.growABR(file.read())
        finally:
            # the file will be closed even if an exception occurs
            file.close()
        return self

    def growABR(self, chaine: str) -> Self:
        """
        construit et retourne un arbre (AB) à partir d'un parcours préfixe sous forme de chaîne de caractères
        :param chaine: parcours préfixe d'une arbre de recherche
        :return: un arbre de recherche
        """
        prefixe = [int(i) for i in chaine.split(" ") if i.isdigit()]
        if len(prefixe) == 0:
            self = AB()
        else:
            self = AB(prefixe)
            self.growRoot()
        return self

    def growRoot(self) -> Any:
        racine = self.racine  # liste
        self.racine = [racine[0]]
        g = []
        d = []
        for i in range(1, len(racine)):
            if racine[i] < self.racine[0]:
                g.append(racine[i])
            else:
                d.append(racine[i])
        if d != []:
            self.set_droite(AB(d))
        if g != []:
            self.set_gauche(AB(g))

        if self.gauche == None and self.droite == None:
            return self
        elif self.gauche == None:
            return self.droite.growRoot()
        elif self.droite == None:
            return self.gauche.growRoot()
        else:
            return self.gauche.growRoot(), self.droite.growRoot()

    def rotD(self) -> Self:
        """
        rotation à droite de l'arbre
        :return: AB
        """
        rot = deepcopy(self.get_gauche())
        if rot != None and rot.get_droite() != None:
            self.set_gauche(rot.get_droite())
            rot.set_droite(self)
        return rot

    def prefixe(self) -> str:
        """
        Retourne le parcours préfixe de l'arbre
        :return: str
        """
        if self.estVide():
            return ""
        else:
            return "{} ".format(self.racine[0]) + (self.gauche.prefixe() if self.gauche else "") \
                + (self.droite.prefixe() if self.droite else "")

    def postfixe(self) -> str:
        """
        Retourne le parcours postfixe de l'arbre
        :return: str
        """
        if self.estVide():
            return ""
        else:
            return (self.gauche.postfixe() if self.gauche else "") + (self.droite.postfixe() if self.droite else "") \
                + "{} ".format(self.racine[0])

    def infixe(self) -> str:
        """
        Retourne le parcours intfixe de l'arbre
        :return: str
        """
        if self.estVide():
            return ""
        else:
            return (self.gauche.infixe() if self.gauche else "") + "{} ".format(self.racine[0]) \
                + (self.droite.infixe() if self.droite else "")

    def get_racine(self) -> list:
        return self.racine

    def get_gauche(self) -> Self:
        return self.gauche

    def get_droite(self) -> Self:
        return self.droite

    def set_racine(self, racine: list) -> None:
        self.racine = racine

    def set_gauche(self, gauche: Self) -> None:
        self.gauche = gauche

    def set_droite(self, droite: Self) -> None:
        self.droite = droite




    ################ brouillon : à ignorer après cette ligne
    def compterLettre(self, chaine):
        dico = {}
        for c in chaine:
            count = 0
            for i in range(len(chaine)):
                if chaine[i] == c:
                    count += 1
            dico[c] = count
        return dico

    def indexLettre(self, chaine):
        freq = self.compterLettre(chaine)
        dico = {}
        for key in freq.keys():
            dico[key] = chaine.find(key)
        return dico

    def autre(self, chaine):
        freq = self.compterLettre(chaine)
        count = 0
        l = []

        while len(freq) > 0:
            for key in freq.keys():
                if count == 0:
                    inf = freq[key]
                    k = key
                    count += 1
                    continue
                if freq[key] < inf:
                    inf = freq[key]
                    k = key
            l.append((k, freq[k]))
            del freq[k]

        return l

    def noeudExt(self):
        if self.estVide():
            return 0
        elif self.gauche == None and self.droite == None:
            return 1
        elif self.gauche == None:
            return self.droite.noeudExt()
        elif self.droite == None:
            return self.gauche.noeudExt()
        else:
            return self.gauche.noeudExt() + self.droite.noeudExt()
