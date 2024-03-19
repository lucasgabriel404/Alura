numeros = [0,1,2,3,4,5,6,7,8,9,10,11,12,'nevertheless']

y=0
for i in numeros:
    try:
        y=y+int(numeros[i])
    except:
        pass

try:
    print(round(y/len(numeros),3))
except:
    print('zero')


