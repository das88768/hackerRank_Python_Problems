# Designer Door Mat

N, M = input().split()

N = int(N)
M = int(M)

# Top Design
for i in range(1, int(N/2)+1):
    print(('.|.'*(i*2-1)).center(M, '-'))
    
# Middle Greating
print(("WELCOME").center(M, '-'))

# Bottom Design
for i in range(int(N/2), 0, -1):
    print(('.|.'*(i*2-1)).center(M, '-'))