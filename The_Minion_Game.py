# The Minion Game

def minion_game(string):
    temp = enumerate(string)
    vovels = ['A', 'E', 'I', 'O', 'U']
    
    kevin, stuart = 0, 0
    for i, ch in temp:
        point = len(string) - i
        
        if ch in vovels:
            kevin += point
        else:
            stuart += point
            
    if kevin == stuart:
        print("Draw")
    elif(stuart > kevin):
        print(f"Stuart {stuart}")
    else:
        print(f"Kevin {kevin}")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)