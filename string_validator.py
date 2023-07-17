# String Validator

def check(string):
    ans1 = True in [char.isalnum() for char in string]
    print(ans1)
    
    ans2 = True in [char.isalpha() for char in string]
    print(ans2)
    
    ans3 = True in [char.isdigit() for char in string]
    print(ans3)
    
    ans4 = True in [char.islower() for char in string]
    print(ans4)
    
    ans5 = True in [char.isupper() for char in string]
    print(ans5)

if __name__ == '__main__':
    s = input()
    check(s)
