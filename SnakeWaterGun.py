import random


def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == "s":
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == "w":
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == "g":
        if you == 's':
            return False
        elif you == 'w':
            return True


print('Comp Turn: Snake (s) Water(w) and Gun(g)?')
randomNo = random.randint(1, 3)
if randomNo == 1:
    comp = "s"
elif randomNo == 2:
    comp = "w"
elif randomNo == 3:
    comp = "g"

you = input('Your Turn: Snake (s) Water(w) and Gun(g)?')

a = gameWin(comp, you)

print(f"Comp Choose {comp}")
print(f"You Choose {you}")

if a == None:
    print("Game is Equle")
elif a:
    print("Your Win")
else:
    print("Your Lose")
