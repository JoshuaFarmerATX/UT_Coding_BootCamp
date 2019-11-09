import random as r

atkDie = 6
atkNum = 4
atkSum = 0

for i in range(atkNum):
    roll = r.randint(1,atkDie + 1)
    atkSum = atkSum + roll

print(atkSum)

