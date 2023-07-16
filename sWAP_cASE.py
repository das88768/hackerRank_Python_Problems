# sWAP cASE

def swap_case(s):
    new_str = "" 
    for i in s:
        if(i == i.upper()):
            char = i.lower()
            new_str = new_str + char
        else:
            char = i.upper()
            new_str = new_str + char
    
    modified_str = new_str
    return new_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)