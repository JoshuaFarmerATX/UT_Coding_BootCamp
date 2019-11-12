import random as r
atkRoll = r.randint(1,20)
gameOn = True
atkSum = 0
spellsAvailable = False

def atk_Roll(fDie, fDieCount):
    atkSum = 0
    for i in range(int(fDieCount)):
        roll = r.randint(1, int(fDie))
        atkSum = atkSum + roll
    print("Your attack damage is:")
    print(atkSum + int(atkDmgMod))

atkMod = input("What is your attack mod?")
atkDie = input("What is your attack die?")
atkDieCount = input("How many attack die?")
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
        atk_Roll(atkDie, atkDieCount)
    elif int(actionCall) is 2 and spellsAvailable in {'y', 'Y', 'yes', 'Yes', 'YES'}:
        print("You cast " + spellName + "!")
        atkRoll = r.randint(1,20)
        print("Your attack roll is:")
        print(atkRoll + int(spellAtk))
        atk_Roll(spellAtk, spellDieCount)
    elif int(actionCall) is 2 and spellsAvailable in {'n', 'N', 'No', 'no', 'NO'}:
        print("You don't have a spell normie! try again!")
    elif int(actionCall) is 5:
        gameOn = False
    else:
        print("Invalid selection, try again.")

print("Oh how sad! The game is over!!!")

