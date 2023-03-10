######### Troisième Break Point #########
### Exercice 15
print("##### Exercice {} #####".format(15))

sac = [17, 38, 10, 25, 72]
new = []
sac.sort()
print(sac)
sac.append(12)
print(sac)
sac.sort(reverse=True)
print(sac)
print("indice de 17: ", sac.index(17))
sac.remove(38)
print(sac)
print(sac[1:3])
print(sac[:2])
print(sac[2:])
print(sac[:])

### Exercice 16
print("##### Exercice {} #####".format(16))

chaine = input("saisir une string: ")
l = list(chaine)
l.reverse()
chaineReversed = "".join(l)
print(chaineReversed)

### Exercice 17: Palindrome
print("##### Exercice {} #####".format(17))

chaine = input("Guessing palindrome: ")
pile = list(chaine)
pile.reverse()
face = "".join(pile)
pile = chaine
if pile == face:
    print("palindrome found!")

### Exercice 18
print("##### Exercice {} #####".format(18))

chaine = input("Saisir une chaîne de caractères de votre choix: ")
arobase = 0
for char in chaine:
    if char == "@":
        arobase += 1


if len(chaine) > 4 and chaine[len(chaine) - 4] == "."  and arobase == 1:
    l = list(chaine)
    l.reverse()
    for i, letter in enumerate(l):
        if i < 3 and (letter == "." or letter == "@"):
            print("not a email address valid")
            break
    print("Valid email address")
else:
    print("not email address")

### Exercice 19
print("##### Exercice {} #####".format(19))

truc = []
machin = []
for i in range(5):
    machin.append(0.)
print("machin: ", machin, "truc: ", truc)

for i in range(4):
    print(i)
print("---")
for i in range(4,8):
    print(i)

for i in range(2,9,2):
    print("pas", i)

### Exercice 20
print("##### Exercice {} #####".format(20))

chose = [i for i in range(6)]
if chose.__contains__(3):
    print("test élément 3 : succès")

if not chose.__contains__(6):
    print("test élément 6 non présent : succès")


