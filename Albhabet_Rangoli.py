# Albhabet Rangoli

import string
def print_rangoli(size):
    
    char = string.ascii_lowercase
    
    # upper cone and middle
    for i in range(size-1, -1, -1):
        row = char[i]
        for j in range(i+1, size):
            nxt = char[j] + '-'
            row = nxt + row + nxt[::-1]
        pad = i*2
        print('-'*pad + row + '-'*pad)
        
    # lower cone
    for i in range(i+1, size):
        row = char[i]
        for j in range(i+1, size):
            nxt = char[j] + '-'
            row = nxt + row + nxt[::-1]
        pad = i * 2
        print('-'*pad + row + '-'*pad)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)