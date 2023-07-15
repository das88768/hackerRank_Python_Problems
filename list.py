# List

if __name__ == '__main__':
    N = int(input())
    
    my_list = []
    
    for i in range(N):
        txt = input()
        temp = txt.split(" ")
        query = temp[0]
        
        if query == "insert":
            my_list.insert(int(temp[1]), int(temp[2]))
            
        if query == "append":
            my_list.append(int(temp[1]))
            
        if query == "remove":
            my_list.remove(int(temp[1]))
            
        if query == "sort":
            my_list.sort()
            
        if query == "pop":
            my_list.pop()
            
        if query == "reverse":
            my_list.reverse()
            
        if query == "print":
            print(my_list)