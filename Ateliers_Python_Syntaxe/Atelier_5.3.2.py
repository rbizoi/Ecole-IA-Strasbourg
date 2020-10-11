# -*- coding:utf-8 -*-
# Atelier 5.3.2


A = [1,'A','Mot',20.3,20+3j,36,'B']
print(A)
B = [0]*len(A)
print(B)

c = 0
while c < len(A) :
    B[c] = A[c] 
    c = c+1
    
print(B)

B1 = []
for i in A: B.append(i)
print(B1)
    
B2 = A[0:len(A)]
print(B2)
