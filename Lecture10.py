def sub_list(li, start, end):
    new_list=[]
    for i in range(start,end+1):
        new_list.append(li[i])
        #49 6 71
    return new_list

li = [2, 23, 49, 6, 71, 55]
print(sub_list(li,2,4))

new_slicing_list=li[2:]
print(new_slicing_list)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_string = "Hello Python"
print(my_list[2:7]) 
print(my_string[0:5]) 

# Omitting start or end 
print(my_list[:5])
print(my_string[7:]) 

# Slicing with a step 
print(my_list[0:10:2])
print(my_string[:: -1]) #reverse


# Creating a copy of a sequence 
new_list = my_list[:] 
print(new_list)

a = [1,2,3] # 123
b = a #123
a[2]=4 # 124
print(b) #124


#*	Introduction to 2d List (Nested List)
math = [100, 98, 90]
science = [90, 100, 89]
hindi = [96, 76, 100]

subjects=[math,science,hindi]
print(subjects)
#*	Indexing in 2d List
# Get the number of 2nd student for hindi 
# take out hindi number

print(subjects[2][1])
# Get the number of 3rd person for science subject 
print(subjects[1][2])
#*	Iterating a 2D list
subjects = [[100, 98, 90], [90, 89], [96, 76, 100]]
for i in range(len(subjects)):
    for j in range(len(subjects[i])):
        print(subjects[i][j],end=" ") # 100 98 90
    print()


#*	Input a 2d List
# user_inp_list = [] 
# row=4
# col=2

# for i in range(row):
#     temp=[]
#     for j in range(col):
#         n=int(input()) # 1 2
#         temp.append(n)
#     user_inp_list.append(temp)
#     print(user_inp_list)

# # Create a matrix of 5 (rows) * 4(column) 
# and enter only even numbers from 0 -> 40 # <!--
#	0	2	4	6
#	8	10	12	14
#	16	18	20	22
#	24	26	28	30
#	32	34	36	38
#	-->			

row=5
col=4
count=0
even_num=[]
for i in range(row):
    temp=[]
    for j in range(col):
        temp.append(count)
        count+=2
    even_num.append(temp)
print(even_num)

#*	Question 1

#Given a value and a list, 
# find the element and print 
# "Found at : index" else "Not found"

# a = [4 ,5 ,3,6, 10] 
# n = 6
# ans = Found at 3 
# n = 11
# ans = Not Found

a = [4 ,5 ,3,6, 10,6]
n = 11
for i in range(len(a)):
    if a[i]==n:
        print("Found at :"+str(i))
        break
else:
    print("Not Found")


