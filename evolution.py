import random
import datetime

maxLength = 100000

class Human(object):
    def __init__(self, velocidade, habilidade, forca, inteligencia):
        self.velocidade = velocidade
        self.habilidade = habilidade
        self.forca = forca
        self.inteligencia = inteligencia
    def adaptabilidade(self):
        return (self.velocidade + self.habilidade + self.forca + self.inteligencia)/4
    
def getParent():
    return Humano(random.randrange(maxLength), random.randrange(maxLength), random.randrange(maxLength), random.randrange(maxLength))

def mutate(parent):
    child = Humano(parent.velocidade, parent.habilidade, parent.forca, parent.inteligencia)
    r = random.randrange(4)
    if r == 0:
        child.velocidade = random.randrange(maxLength)
    if r == 1:
        child.habilidade = random.randrange(maxLength)
    if r == 2:
        child.forca = random.randrange(maxLength)
    if r == 3:
        child.inteligencia = random.randrange(maxLength)

    if child.adaptabilidade() <= parent.adaptabilidade():
        child = parent

    return child

def display(parent):
    print("Humano:\n velocidade: "+str(parent.velocidade)+"\n habilidade: "+str(parent.habilidade)+"\n força: "+str(parent.forca)+"\n inteligencia: "+str(parent.inteligencia)+"\n adaptabilidade: "+str(parent.adaptabilidade())+"\n")

bestParent = getParent()
bestParent = mutate(bestParent)
display(bestParent)
inicial = datetime.datetime.now()
print(inicial)

while True:
    bestParent = mutate(bestParent)
    display(bestParent)

input()
