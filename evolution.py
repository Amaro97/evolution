import random
import datetime

maxLength = 1000000

class Human(object):
    def __init__(self, speed, abiliity, strength, intelligence):
        self.speed = speed
        self.abiliity = abiliity
        self.strength = strength
        self.intelligence = intelligence
    def adaptability(self):
        return (self.speed + self.abiliity + self.strength + self.intelligence)/4
    
def getParent():
    return Human(random.randrange(maxLength), random.randrange(maxLength), random.randrange(maxLength), random.randrange(maxLength))

def mutate(parent):
    child = Human(parent.speed, parent.abiliity, parent.strength, parent.intelligence)
    r = random.randrange(4)
    if r == 0:
        child.speed = random.randrange(maxLength)
    if r == 1:
        child.abiliity = random.randrange(maxLength)
    if r == 2:
        child.strength = random.randrange(maxLength)
    if r == 3:
        child.intelligence = random.randrange(maxLength)

    if child.adaptability() <= parent.adaptability():
        child = parent

    return child

def display(parent):
    print("Human:\n speed: "+str(parent.speed)+"\n abiliity: "+str(parent.abiliity)+"\n strength: "+str(parent.strength)+"\n intelligence: "+str(parent.intelligence)+"\n adaptability: "+str(parent.adaptability())+"\n")

bestParent = getParent()
bestParent = mutate(bestParent)
display(bestParent)
initial = datetime.datetime.now()
print(initial)

while True:
    bestParent = mutate(bestParent)
    display(bestParent)
    if bestParent.adaptability() >= maxLength - 1:
        print(datetime.datetime.now() - initial)
        break

input()
