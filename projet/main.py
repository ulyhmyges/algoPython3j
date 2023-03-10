from collections import OrderedDict

from projet.ab import AB
from array import array

if __name__ == '__main__':
    A1 = AB()
    assert A1.estVide() == True
    print(A1.estVide())
    A2 = AB([5])
    assert A2.estVide() == False
    print(A2.estVide())
    A3 = AB([3])

    ####A3.set_droite(AB([4]))
    assert A3.estVide() == False
    print(A3.estVide())
    A2.set_gauche(A3)
    A8 = AB([8])
    A2.set_droite(A8)
    # Q7
    Atest = AB([10])
    A12 = AB([12])
    Atest.set_droite(A12)
    Atest.set_gauche(A2)
    assert Atest.estVide() == False
    print(Atest.estVide())
    #print(Atest)
    print(Atest.taille())
    # Q8
    #assert Atest.taille() == 5
    # Q11
    print("préfixe: ", Atest.prefixe())
    assert Atest.prefixe() == "10 5 3 8 12 "

    #Q13 : parcours postfixe
    print("postfixe: ", Atest.postfixe())
    assert Atest.postfixe() == "3 8 5 12 10 "

    # parcours infixe
    print("infixe: ", Atest.infixe())
    assert Atest.infixe() == "3 5 8 10 12 "

    # Q14: hauteur

    print("Atest hauteur: ", Atest.hauteur())

    # Q15
    print(Atest.ABR())
    assert Atest.ABR() == True

    # Q16 : Equilibré ?

    a51 = AB([51])
    a93 = AB([93])
    a77 = AB([77])
    a77.set_droite(a93)
    a77.set_gauche(a51)
    a3 = AB([3])
    a40 = AB([40])
    a40.set_gauche(a3)
    a40.set_droite(a77)
    a197 = AB([197])
    a237 = AB([237])
    a203 = AB([203])
    a203.set_droite(a237)
    a203.set_gauche(a197)
    a191 = AB([191])
    a191.set_droite(a203)
    a112 = AB([112])
    a112.set_droite(a191)
    a112.set_gauche(a40)
    print("hauteur a112: ", a112.hauteur())
    print("equilibré: ", Atest.estEquilibre())
    print("equilibré: ", a112.estEquilibre())
    a = AB([5])
    b = AB([12])
    c = AB([7])
    b.set_gauche(c)
    a.set_droite(b)
    f = AB([3])
    e = AB([1])
    d = AB([4])
    d.set_droite(AB(4))
    e.set_droite(f)
    d.set_gauche(e)
    a.set_gauche(d)
    print(a.estEquilibre())

    # grow tree
    p = AB().growABR(Atest.prefixe())
    print(a)
    assert p.__str__() == Atest.__str__()
    m = AB()
    m = m.growABR(a112.prefixe())
    assert m.__str__() == a112.__str__()
    arbre = AB().fromFileGrowABR("prefixe.txt")
    assert  arbre.__str__() == Atest.__str__()
    #x = x.growABR("10 5 3 8 12")

    ## ROTATION DROITE
    """
    print(Atest.rotD())
    print(a112.rotD())

    freq = Atest.compterLettre("BARBAPAPA")
    print("d", freq)
    dico = Atest.autre("BARBAPAPA")
    print("index: ", dico)
    """
