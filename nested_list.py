# Nested List

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l = [name, score]
        records.append(l)
    
    marks = []
    for i in records:
        if i[1] not in marks:
            marks.append(i[1])
            
    marks.sort()

    res_name = []
    for i in records:
        if(i[1] == marks[1]):
            res_name.append(i[0])
    
    res_name.sort()       
    
    for i in res_name:
        print(i)