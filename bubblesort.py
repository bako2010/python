import random as rd

zufall = []
rd.seed()
for i in range(10):
    zufall.append(rd.randint(1, 20))
print(zufall)

for a in range(9):
  for i in range(9):
       if zufall[i] > zufall[i+1]:
            a = zufall[i]
            zufall[i] = zufall[i+1]
            zufall[i+1] = a
print(zufall)
