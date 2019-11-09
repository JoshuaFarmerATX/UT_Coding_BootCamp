import random as r
atkRoll = r.randint(1,20)
gameOn = True
atkSum = 0
spellsAvailable = False


atkMod = input("What is your attack mod?")
atkDie = input("What is your attack die?")
atkDieCount = input("How many attack die?")
#while int(atkDieCount) >= 9:
#    print("You cheater! You don't have that many attack die! Try again!")
#    atkDieCount = input("How many attack die?")
atkDmgMod = input("What is your attack damage mod?")
while spellsAvailable is False:
    spellsAvailable = input("Would you like to add a spell? yes/no")
    if spellsAvailable in {'y', 'Y', 'yes', 'YES'}:
        spellName = input("What is your spell's name?")
        spellAtk = input("What is your spell's attack bonus?")
        spellDmg = input("What is your spell's damage die?")
        spellDieCount = input("How many die?")
        spellDmgMod = input("What is your spell's damage modifier?")
    elif spellsAvailable in {'n', 'N', 'no', 'No'}:
        break
    else:
        spellsAvailable = False
        print("Invalid input. Type yes/no")

while gameOn:
    print("""
    What would you like to do?
    1. ATTACK!!!
    2. Cast my spell!!!
    5. End Game
    """)
    actionCall = input()
    if int(actionCall) is 1:
        atkRoll = r.randint(1,20)
        print("Your attack roll is:")
        print(atkRoll + int(atkMod))
        for i in range(int(atkDieCount)):
            roll = r.randint(1, int(atkDie))
            atkSum = atkSum + roll
#            print(roll)
        print("Your attack damage is:")
        print(atkSum + int(atkDmgMod))
        atkSum = 0
    elif int(actionCall) is 2 and spellsAvailable in {'y', 'Y', 'yes', 'Yes', 'YES'}:
        print("You cast " + spellName + "!")
        atkRoll = r.randint(1,20)
        print("Your attack roll is:")
        print(atkRoll + int(spellAtk))
        for i in range(int(spellDieCount)):
            roll = r.randint(1, int(spellDmg))
            atkSum = atkSum + roll
#            print(roll)
        print("Your attack damage is:")
        print(atkSum + int(spellDmgMod))
        atkSum = 0
    elif int(actionCall) is 2 and spellsAvailable in {'n', 'N', 'No', 'no', 'NO'}:
        print("You don't have a spell normie! try again!")
#        if int(atkDieCount) is 1:
#            atkDmgRoll = r.randint(1,int(atkDie))
#            print("Your attack damage is:")
#            print(int(atkDmgRoll) + int(atkDmgMod))
#        elif int(atkDieCount) is 2:
#            atkDmgRoll1 = r.randint(1,int(atkDie))
#            atkDmgRoll2 = r.randint(1,int(atkDie))
#            print("Your attack damage is:")
#            print(int(atkDmgRoll1) + int(atkDmgRoll2) + int(atkDmgMod))
#        elif int(atkDieCount) is 3:
#            atkDmgRoll1 = r.randint(1,int(atkDie))
#            atkDmgRoll2 = r.randint(1,int(atkDie))
#            atkDmgRoll3 = r.randint(1,int(atkDie))
#            print("Your attack damage is:")
#            print(int(atkDmgRoll1) + int(atkDmgRoll2) + int(atkDmgRoll3) + int(atkDmgMod))
#        elif int(atkDieCount) is 4:
#            atkDmgRoll1 = r.randint(1,int(atkDie))
#            atkDmgRoll2 = r.randint(1,int(atkDie))
#            atkDmgRoll3 = r.randint(1,int(atkDie))
#            atkDmgRoll4 = r.randint(1,int(atkDie))
#            print("Your attack damage is:")
#            print(int(atkDmgRoll1) + int(atkDmgRoll2) + int(atkDmgRoll3) + int(atkDmgRoll4) + int(atkDmgMod))
#        elif int(atkDieCount) is 5:
#            atkDmgRoll1 = r.randint(1,int(atkDie))
#            atkDmgRoll2 = r.randint(1,int(atkDie))
#            atkDmgRoll3 = r.randint(1,int(atkDie))
#            atkDmgRoll4 = r.randint(1,int(atkDie))
#            atkDmgRoll5 = r.randint(1,int(atkDie))
#           print("Your attack damage is:")
#            print(int(atkDmgRoll1) + int(atkDmgRoll2) + int(atkDmgRoll3) + int(atkDmgRoll4) + int(atkDmgRoll5) + int(atkDmgMod))
#        elif int(atkDieCount) is 6:
#            atkDmgRoll1 = r.randint(1,int(atkDie))
#            atkDmgRoll2 = r.randint(1,int(atkDie))
#            atkDmgRoll3 = r.randint(1,int(atkDie))
#            atkDmgRoll4 = r.randint(1,int(atkDie))
#            atkDmgRoll5 = r.randint(1,int(atkDie))
#            atkDmgRoll6 = r.randint(1,int(atkDie))
#            print("Your attack damage is:")
#            print(int(atkDmgRoll1) + int(atkDmgRoll2) + int(atkDmgRoll3) + int(atkDmgRoll4) + int(atkDmgRoll5) + int(atkDmgRoll6) + int(atkDmgMod))
#        elif int(atkDieCount) is 7:
#            atkDmgRoll1 = r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie))
#            print("Your attack damage is:")
#            print(int(atkDmgRoll1) + int(atkDmgMod))
#        elif int(atkDieCount) is 8:
#            atkDmgRoll1 = r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie)) + r.randint(1,int(atkDie))
#            print("Your attack damage is:")
#            print(int(atkDmgRoll1) + int(atkDmgMod))

    elif int(actionCall) is 5:
        gameOn = False
    else:
        print("Invalid selection, try again.")

print("Oh how sad! The game is over!!!")

