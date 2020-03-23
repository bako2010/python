import random as rd
liste = []


def generate():
    rd.seed()
    return(rd.randrange(1,20))


for i in range(10):
    liste.append(generate())


    

print(liste)