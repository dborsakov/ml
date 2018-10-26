import numpy as np
import random
import math

def print_arr(a):
    global n
    for i in range(n):
        for j in range(n):
            print(a[i][j],end=' ')
        print()

def middle(a):
    global n
    s=0
    for i in range(n):
        for j in range(n):
            s+=a[i][j]
    return(s/n**2)

def dis(a):
    global n
    global S
    D = 0
    for i in range(n):
        for j in range(n):
            D+=(a[i][j]-S)**2
    return(math.sqrt(D/(n*n-1)))

def obr(a):
    global n
    global S
    global D
    for i in range(n):
        for j in range(n):
            if (math.fabs(a[i][j])>D):
                a[i][j]=S

a = []
print('Ведите размер:')
n = int(input())
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(random.randint(-100,100))

print_arr(a)
S = middle(a)
D = dis(a)

print('Среднее ',S)
print('Среднее квадратическое отклонение ',D)
print('Новый массив')
obr(a)
print_arr(a)
