# Find a String

def count_substring(string, sub_string):
    str_len = len(string)
    
    start_index = string.find(sub_string)
    
    count = 0
    start = 0
    
    for i in range(str_len):
        occur = string.find(sub_string, start)
        if occur != -1:
            count += 1
            start = occur+1
        else:
            break
    
    return count
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)