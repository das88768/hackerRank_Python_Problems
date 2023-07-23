# Collection Counters

from collections import Counter

num_of_shoe = int(input())
size_list = map(int, input().split())
num_of_customer = int(input())


avail_shoes = Counter(size_list)

total_income = 0

for i in range(num_of_customer):
    size, cost = map(int, input().split())
    
    if avail_shoes[size]:
        total_income += cost
        avail_shoes[size] -= 1
        
print(total_income)
      