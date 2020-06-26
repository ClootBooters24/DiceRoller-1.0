from random import randint


print("Welcome to Clay's Dice Roller!")
while True:
    print("What dice would you like me to roll?")
    x = input()

#Stop The Game
    if x == "None":
        y = input("Are you ready to quit?: ")
        if y == "Yes":
            break
        else:
            exit

#Four Sided Dice
    if x == 'd4':
        print("You rolled", randint(1, 4))
        y = input("Would you like to roll again?: ")
        if y == "Yes":
            exit
        else:
            break

#Six Sided Dice
    if x == 'd6':
        print("You rolled", randint(1, 6))
        y = input("Would you like to roll again?: ")
        if y == "Yes":
            exit
        else:
            break

#Eight Sided Dice
    if x == 'd8':
        print("You rolled", randint(1, 8))
        y = input("Would you like to roll again?: ")
        if y == "Yes":
            exit
        else:
            break

#Ten Sided Dice
    if x == 'd10':
       print("You rolled", randint(1, 10))
       y = input("Would you like to roll again?: ")
       if y == "Yes":
            exit
       else:
            break

#Twelve Sided Dice
    if x == 'd12':
        print("You rolled", randint(1, 12))
        y = input("Would you like to roll again?: ")
        if y == "Yes":
            exit
        else:
            break

#Twenty Sided Dice
    if x == 'd20':
        print("You rolled", randint(1, 20))
        y = input("Would you like to roll again?: ")
        if y == "Yes":
            exit
        else:
            break

#Hundred Sided Dice
    if x == 'd100':
        print("You rolled", randint(1, 100))
        y = input("Would you like to roll again?: ")
        if y == "Yes":
            exit
        else:
            break
