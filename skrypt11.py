import os
import time
from math import pi

print("Witajcie \n")
liczba = 6
liczba1 = 6 * 1.5
print(liczba," ",liczba1)
A = "pythonhonhon"
print(len(A))
print(A[0]," ",A[3])
print(A[-1])
print(A+" warsztaty")
print(A[3:5])
print(A*3)
A = A.replace("hon", "bu")
print(A)
A = A.upper()
print(A)
#--------------------------
L = [3, "warsztaty", 2.13, "python", 42, 512]
print(len(L))
print(L[1])
print(L[1][1])
L = L+[1,2,3]
print(L)
L.append("IKN")
print(L)
L.pop(2)
print(L)
L.reverse()
print(L)
inty = [2,[3,6],[12,67,3],56,9]
print(inty[1][1])
#-------------------------------
B = {"sala": 1018, "temat": "Python", "uniwersytet": "UwB"}
print(B["sala"])
#--------------------------------------------------------
T = (1,2,3,2,5,2)
print(T.count(2))
T = T+(1,2,6,6)
print(T)
#--------------------------------------------------------
f = open('data.txt',"w")
f.write("Witaj, \n")
f.close()
g = open('data.txt',"r")
text = g.read()
print(text)

#----------------------------------------------
#d = input("wpisz liczbe \n")
#print(d)
x = 5
y = 5
if x>y:
    print("X wiekszy od Y")
elif x<y:
    print("X mniejszy od Y")
else:
    print("Nie wiem")
#---------------------------------
for i in range(20,40):
    print(i)
S = {'sala': 1018, 'nazwa': "warszaty", 'temat': "python"}
for x in S:
    print(x, "->", S[x])

Y = pi
print(Y)



