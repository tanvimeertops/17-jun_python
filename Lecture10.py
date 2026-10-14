def sub_list(li, start, end):
    new_list=[]
    for i in range(start,end+1):
        new_list.append(li[i])
        #49 6 71
    return new_list

li = [2, 23, 49, 6, 71, 55]
print(sub_list(li,2,4))