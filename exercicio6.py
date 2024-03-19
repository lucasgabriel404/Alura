numeros = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
nomes = ['Lucas','Gabriel','Santos','Quimera']
anos = [1997,2024]

for i in numeros:
    print(i)

for i in nomes:
    print(i)

for i in anos:
    print(i)

x=0
for i in numeros:
    if i%2 != 0:
        x=x+i
print(x)

y=len(numeros)
while y>0:
    print(numeros[y-1])
    y=y-1



