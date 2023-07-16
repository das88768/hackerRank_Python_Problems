# String Split and Join

def split_and_join(line):
    str_list = line.split(" ")
    
    final_str = "-".join(str_list)
    return final_str

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
