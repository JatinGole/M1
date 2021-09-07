import random

roll=input("___Press y to roll the dice___")
print("\n")

while roll == "y":
    a=random.randint(1,6)

    if a== 1:
        print("-----------")
        print("|         |")
        print("|    *    |")
        print("|         |")
        print("___________")
        break
    if a == 2:
        print("-----------")
        print("|         |")
        print("|  *   *  |")
        print("|         |")
        print("___________")
        break
    if a == 3:
        print("-----------")
        print("|         |")
        print("| *  *  * |")
        print("|         |")
        print("___________")
        break
    if a == 4:
        print("-----------")
        print("|  *   *  |")
        print("|         |")
        print("|  *   *  |")
        print("___________")
        break
    if a == 5:
        print("-----------")
        print("|    *    |")
        print("| *  *  * |")
        print("|    *    |")
        print("___________")
        break
    if a == 6:
        print("-----------")
        print("|  *   *  |")
        print("|  *   *  |")
        print("|  *   *  |")
        print("___________")
        break

