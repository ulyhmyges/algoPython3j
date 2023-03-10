def intInput(inf, sup):
    while True:
        try:
            entier = int(input("Saisir un entier compris entre {} et {}: ".format(inf, sup)))
            if entier > sup or entier < inf:
                raise Exception("The input value must be a integer in the range of {} to {}".format(inf, sup))
            print("your input value: ", entier)
            return entier
        except ValueError:
            print("Value error: input must be a integer")
        except Exception as ex:
            print(ex)

######### Deuxième Break Point #########
### Exercice 6
print("##### Exercice {} #####".format(6))

chaine = input("Saisir une chaîne de caractères de votre choix: ")
arobase = 0
for char in chaine:
    if char == "@":
        arobase += 1

chaineList = chaine.split(".com")
if chaineList[len(chaineList) - 1] == "" and arobase == 1 and chaine[len(chaine) - 5] != "@":
    print("Valid email address")
else:
    print("not email address")

### Exercice 7
print("##### Exercice {} #####".format(7))

for i in range(10):
    print("{:0>2} fois : un message à l'écran".format(i + 1))

### Exercice 8
print("##### Exercice {} #####".format(8))

word = input("Saisir un mot: ")
for letter in word:
    print("letter: ", letter)

### Exercice 9
print("##### Exercice {} #####".format(9))

a = 0
b = 10
while a < b:
    print("a = ", a)
    a += 1

### Exercice 10
print("##### Exercice {} #####".format(10))

# b = 10
while b > 0:
    if b % 2 == 1:
        print("b = ", b)
    b -= 1

### Exercice 11
print("##### Exercice {} #####".format(11))

while True:
    try:
        entier = int(input("Saisir un entier compris entre 1 et 10: "))
        if entier > 10 or entier < 1:
            raise Exception("The input value must be a integer in the range of 1 to 10")
        print("your input value: ", entier)
        break
    except ValueError:
        print("Value error: input must be a integer")
    except Exception as ex:
        print(ex)

### Exercice 12
print("##### Exercice {} #####".format(12))

for character in "hello world!":
    print(character)

for item in [3, 5, True, 2, "rr"]:
    print("item: ", item)

for i in range(15):
    if i % 3 == 0:
        print("entier: ", i)

n = 30
while n > 0:
    if n % 2 == 0:
        print("n est paire: ", n)
    n -= 1

n = intInput(0, 100)
for i in range(n + 1):
    if i % 2 == 0:
        print("(for loop) n est paire: ", i)
