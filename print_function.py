# Print Function

if __name__ == '__main__':
    n = int(input())
    
    temp = []
    for i in range(1, n+1):
        temp.append(i)
    for i in temp:
        print(i, end='')