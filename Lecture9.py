#List
a=[1,2,3]
print(a)
print(type(a))

a=([1,2,3])
print(a)

a=['a','b','c']
print(a)

a=[1,True,3.5,'piyush',None]
print(a)

#*	Indexing in a List
students = ['Kusum', 'Shubham', 'Pooja']
print(students) # Kusum
#indexing
print(students[1])
print(len(students))

#*	Reverse Indexing
print(students[-1])

print(len(students))
print(students[len(students)-2])

#*	Updating an Index in a List
students = ['Kusum', 'Shubham', 'Pooja']
print(students)

students[1]="Naveen"
print(students)

# students[10]="piyush"
# print(students)

students[-1]="Devanshi"
print(students)


students = ['Kusum', 'Shubham', 'Pooja', 'Ruben', 'Aarushi', 
            'Vinoth', 'Veerendra'] 

for i in range(len(students)):
    print(students[i],end=" ")

for student in students:
    print(student,end=" ") #kusum shubham pooja ruben aarushi vinoth veerendra

# square all the elements inside the array [method 2] 
a = [1,2,3,4]
for index in a:
    print(index**2) 

# print(a)
# square all the elements inside the array [method 1]
a = [1,2,3,4]
for i in range(len(a)):
    a[i]=a[i]**2 # 1^2=1, 2^2=4,3^2=9,4^2=16
print(a)

#*	Functions in a List
#len()
a = [1, 5,6,10,15,20]
print(len(a)) #6

#*	append()
a=[]
print(a)
a.append(10)
print(a)
a.append(True)
print(a)
a.append("piyush")
print(a)
a.append("piyush")
print(a)
a.append([1,2,3])
print(a)
#insert()
a=[1,2,3,4]
a.insert(1,"piyush")
print(a) 

a.insert(0, 'Singh') 
print(a)

#['Singh', 1, 'piyush', 2, 3, 4]
a.insert(-1,"abc")
print(a)
#['Singh', 1, 'piyush', 2, 3, 'abc', 4]
a.insert(8, 'shdv')
print(a)
# Need to confirm 
a.insert(110, 'last') 
print(a)
#['Singh', 1, 'piyush', 2, 3, 'abc', 4, 'shdv', 'last']
print(len(a))

#pop
a = [1,2,3,4,5,6]
print(a.pop())
#1,2,3,4,5
print(a.pop(0))
#2,3,4,5
print(a.pop(2))
#2,3,5
#print(a.pop(10))

#remove
students = ['Kusum', 'Shubham', 'Pooja', 'Ruben', 'Aarushi', 'Vinoth', 'Veerendra']
students.remove("Shubham")
print(students)
a = [1, 2, 3, 2,4]
a.remove(2)
print(a)

a = [1,2,'a']
b = [4,5,6]
c=a+b
print(c)
a = [2,3,4,7]
a.extend([12,13, 15, 20])
a.extend(range(5))
print(a)

a = ['a', 'c', 'd', 'g']
print('x' in a) 

if 'd' in a:
    a.remove('d')

print(a)

# n=int(input("How many colors :"))
# colors=[]
# for _ in range(n):
#     color=input("Enter color :")
#     colors.append(color)

# print(colors)

a = ['Piyush', 'Shekhar'] 
for i in range(len(a)):
    if a[i]=="Shekhar":
        print(i)

a = ['a', 'b', 'c']
for i in range(len(a)):
    print(i, '  ',a[i])

#2D list
students=[
    [1,"nikhil"],
    [2,"jamshed"],
    [3,"dev"]
]
print(students)

a=[
    [10,20,30], #0
    [40,50,60], #1 
    [70,80,90]
]
print(a[0][0])
print(a[1][1])

#Iteration in list
numbers=[

    [1,2],
    [3,4]
]

for row in numbers:#row[0]
    for item in row:
        print(item*2,end=" ")                      
    print()
#         # 1 4 
#         # 

