# M1
# projects
# Dice Simulator 


import random
from locale import k

def roll(k):

        a = random.randint(1, 6)

        if a == 1:
            print("|-----------|")
            print("|           |")
            print("|     *     |")
            print("|           |")
            print("|___________|")

        if a == 2:
            print("|-----------|")
            print("|           |")
            print("|  *     *  |")
            print("|           |")
            print("|___________|")

        if a == 3:
            print("|-----------|")
            print("|           |")
            print("| *   *   * |")
            print("|           |")
            print("|___________|")

        if a == 4:
            print("|-----------|")
            print("|   *   *   |")
            print("|           |")
            print("|   *   *   |")
            print("|___________|")

        if a == 5:
            print("|-----------|")
            print("|     *     |")
            print("| *   *   * |")
            print("|     *     |")
            print("|___________|")

        if a == 6:
            print("|-----------|")
            print("|   *   *   |")
            print("|   *   *   |")
            print("|   *   *   |")
            print("|___________|")




roll(k)
print("\n")
