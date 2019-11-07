import random as r
atkMod = input("What is your attack mod?")
atkDie = input("What is your attack die?")
atkDieCount = input("How many attack die?")
while int(atkDieCount) >= 9:
    print("You cheater! You don't have that many attack die! Try again!")
    atkDieCount = input("How many attack die?")
atkDmgMod = input("What is your attack damage mod?")

atkRoll = r.randint(1,20)
gameOn = True
while gameOn:
    print("""
    What would you like to do?
    1. ATTACK!!!
    5. End Game
    """)
    actionCall = input()
    if int(actionCall) is 1:
        atkRoll = r.randint(1,20)
        print("Your attack roll is:")
        print(atkRoll + int(atkMod))
        if int(atkDieCount) is 1:
            atkDmgRoll = r.randint(1,int(atkDie))
            print("Your attack damage is:")
            print(int(atkDmgRoll) + int(atkDmgMod))
        elif int(atkDieCount) is 2:
            atkDmgRoll1 = r.randint(1,int(atkDie))
            atkDmgRoll2 = r.randint(1,int(atkDie))
            print("Your attack damage is:")
            print(int(atkDmgRoll1) + int(atkDmgRoll2) + int(atkDmgMod))
        elif int(atkDieCount) is 3:
            atkDmgRoll1 = r.randint(1,int(atkDie))
            atkDmgRoll2 = r.randint(1,int(atkDie))
            atkDmgRoll3 = r.randint(1,int(atkDie))
            print("Your attack damage is:")
            print(int(atkDmgRoll1) + int(atkDmgRoll2) + int(atkDmgRoll3) + int(atkDmgMod))
        elif int(atkDieCount) is 4:
            atkDmgRoll1 = r.randint(1,int(atkDie))
            atkDmgRoll2 = r.randint(1,int(atkDie))
            atkDmgRoll3 = r.randint(1,int(atkDie))
            atkDmgRoll4 = r.randint(1,int(atkDie))
            print("Your attack damage is:")
            print(int(atkDmgRoll1) + int(atkDmgRoll2) + int(atkDmgRoll3) + int(atkDmgRoll4) + int(atkDmgMod))
        elif int(atkDieCount) is 5:
            atkDmgRoll1 = r.randint(1,int(atkDie))
            atkDmgRoll2 = r.randint(1,int(atkDie))
            atkDmgRoll3 = r.randint(1,int(atkDie))
            atkDmgRoll4 = r.randint(1,int(atkDie))
            atkDmgRoll5 = r.randint(1,int(atkDie))
            print("Your attack damage is:")
            print(int(atkDmgRoll1) + int(atkDmgRoll2) + int(atkDmgRoll3) + int(atkDmgRoll4) + int(atkDmgRoll5) + int(atkDmgMod))
        elif int(atkDieCount) is 6:
            atkDmgRoll1 = r.randint(1,int(atkDie))
            atkDmgRoll2 = r.randint(1,int(atkDie))
            atkDmgRoll3 = r.randint(1,int(atkDie))
            atkDmgRoll4 = r.randint(1,int(atkDie))
            atkDmgRoll5 = r.randint(1,int(atkDie))
            atkDmgRoll6 = r.randint(1,int(atkDie))
            print("Your attack damage is:")
            print(int(atkDmgRoll1) + int(atkDmgRoll2) + int(atkDmgRoll3) + int(atkDmgRoll4) + int(atkDmgRoll5) + int(atkDmgRoll6) + int(atkDmgMod))
        elif int(atkDieCount) is 7:
            atkDmgRoll1 = r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie))
            print("Your attack damage is:")
            print(int(atkDmgRoll1) + int(atkDmgMod))
        elif int(atkDieCount) is 8:
            atkDmgRoll1 = r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie))
            print("Your attack damage is:")
            print(int(atkDmgRoll1) + int(atkDmgMod))

    elif int(actionCall) is 5:
        gameOn = False
    else:
        print("Invalid selection, try again.")

print("Oh how sad! The game is over!!!")

