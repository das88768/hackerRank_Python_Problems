# Mutations

def mutate_string(string, position, character):
    
    txt = list(string)
    
    txt[position] = character
    
    modify_str = "".join(txt)
    return modify_str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)