# Itertools Product

from itertools import product

input_a = list(input().split(' '))
A = [int(i) for i in input_a]
        
input_b = list(input().split(' '))
B = [int(i) for i in input_b]

temp = [A, B]

ans = list(product(*temp))

for i in ans:
    print(i, end=' ')