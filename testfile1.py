import random as r
atkMod = input("What is your attack mod?")
atkDie = input("What is your attack die?")
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
        atkDmgRoll = r.randint(1,int(atkDie))
        print("Your attack damage is:")
        print(int(atkDmgRoll) + int(atkDmgMod))
    elif int(actionCall) is 5:
        gameOn = False
    else:
        print("Invalid selection, try again.")

print("Oh how sad! The game is over!!!")

