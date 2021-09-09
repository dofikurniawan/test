# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 13:48:21 2021

@author: Dofi
"""

name1=input("masukan nama1:")
name2=input("masukan nama2:")
A=[]
C=[]
name=name1+name2
for i in 'truelove':
    A.append(name.count(i))
for i in range (len(A)):
    B=[]
    for j in range((len(A))-1-i):
        if i==0:
            if (A[j]+A[j+1]>=10):  
                B.append(A[j]+A[j+1]-10)
            else:
                B.append(A[j]+A[j+1])
        else:
            if (C[i-1][j]+C[i-1][j+1]>=10):
                B.append(C[i-1][j]+C[i-1][j+1]-10)
            else:
                B.append(C[i-1][j]+C[i-1][j+1])
    C.append(B)
print('Tingkat Kecocokan',C[5][0]*10+C[5][1],'%')

    


