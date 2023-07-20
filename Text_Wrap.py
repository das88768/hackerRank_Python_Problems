# Text Wrap

import textwrap

def wrap(string, max_width):
    word_list = list(string)
    
    for i in range(1, len(word_list)):
        if(i*max_width+i-1 < len(word_list)):
            word_list.insert(i*max_width+i-1, '\n')
            
    return "".join(word_list)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)