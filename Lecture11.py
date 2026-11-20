planets = ["Mercury", "Venus", "Earth", "Mars",
            "Jupiter", "Saturn", "Uranus", "Neptune"]
planets.append('sun')
print(planets)

# tuples of number 
num=(1,2,3)
print(type(num))
print(num)
# num[0]=5
# print(num)
# *** Create tuple of single digit 
b=(1,)
print(type(b))
c=('a',)
print(type(c))
a=()
print(type(a))

# tuple of range 0- 10 
nums=tuple(range(11))
print(nums)

a=[]
for i in range(11):
    a.append(i)
a=tuple(a) #list to tuple
print(a)

# Tuples in functions 
def swap(a,b):
    return(b,a)

print(type(swap(12,34)))

a,b=swap(5,6)
print(a)
print(b)

def name():
    first_name=input("enter first name : ")
    last_name=input("enter last name :")
    return (first_name,last_name)

# first_name,last_name=name()
# print(first_name,last_name)

# Partially mutable tuples 

a=(1,2,3,[4,5,6])
print(a)
print(a[0])

print(a[-3])
print(a[3])
a[3].append(20)
print(a)

# t = (1, 2, 3)
# t[0]=4
# print(t)

a = 23
t = (a) 
print(type(t))

a = (1,2,3,4,5)
for n in a: # 2
    print(n)

for i in range(len(a)):
    print(a[i]) # a[0]=1 a[1]=2


#String
a= 'Piyush' 
b = "singh"
print(type(a))
# string is also immutable 
# a[0]="S"
# print(a)

print(ord('a')) #97
print(ord('m'))
print(ord('z'))
print(ord('9'))
print(ord("&"))

print(chr(97))
print(chr(109))

#Properties of String
#string are immutable 
# a = 'Piyush'
# a[0]='a'

# we are replacing and not modifying 
# Homogeneity 
a = ["Naveen", "kumar"] 
a[0]="Naveenkumar"
print(a)
# a=a+42
# print(a)
a="piyush"
a = a + 'd'

print(a)

# Iterability 
a = 'Piyush' 
for each_chr in a:
    print(each_chr)


# for i in range(len(a)):
#     a[i] = 'c'
#     print(a[i])

# Case Sensitive 
a= 'Piyush'
b = 'piyush' 
print(a==b)
s = 'Tops Tech' 
print(s[0:5])

text = "TopsTechnologies"
print(text[0:6])
print(text[-3:])
print(text[6:11])
print(text[::-1])
print(text[::2])
print(text[3:])

#Functions in strings
print("tops tech".capitalize())
print("tops tech".title())
print("tops tech".count('t'))
print('pooja makhija'.count('ja'))
deltr = 'ae'
print('piyush singh'.replace('iy',deltr))

a = 'piyush'
b = a.replace('i','e') 
print(a)
print(b)

# split(seperator) 
print('abc_bncd_def'.split('_'))
print('abc_+bncd_+def'.split('_+'))

# join()
a = ['abc', 'bncd', 'def'] 
print('_+'.join(a))


# upper and lower 
print('tops'.upper())
print('TOPS'.lower())

#Formatted String
name = 'Piyush' 
gender= 'Male' 
age = '30'
print('Name:-',name,"Gender:-",gender,"Age:-",age)
print(f'Name:-{name} Gender:-{gender} Age:-{age}')
temp = 'Name:- {}, Gender:- {}, Age:- {}' 
print(temp.format("tops","UnSpecified",13))
print([1,2,3,4,5] < [1, 3])
print([1,3,0]>[1,3])
print([1,3] ==[1, 3])
print([1,4,5] > [1,6])

#String comparision
print('a' > 'A')
print('Aakar' > 'Sudip') #65
# You are given a list of strings, where each string represents
#  a log entry from a system. 
# # Your task is to find and print all log entries 
# that contain the word "ERROR".

# logs = [
#	"2024-07-18 10:00:01 INFO Server started",
#	"2024-07-18 10:01:17 ERROR Failed to connect to database",
#   "2024-07-18 10:02:45 WARNING High memory usage",
#	"2024-07-18 10:04:10 ERROR Disk full",
#	"2024-07-18 10:06:30 INFO Backup complete" # ]


logs = [
    "2024-07-18 10:00:01 INFO Server started",
    "2024-07-18 10:01:17 ERROR Failed to connect to database",
    "2024-07-18 10:02:45 WARNING High memory usage",
	"2024-07-18 10:04:10 ERROR Disk full",
	"2024-07-18 10:06:30 INFO Backup complete,error"  ]

for lines in logs:
    if "ERROR" in lines.upper():
         print(lines)

# Question 2 -> Print the longest line lines = [
#   "DevOps is awesome.",
#   "Error: Disk not found.",
#   "Server started successfully at 10:05 AM.",
#   "OK"
# ]
longest_line = ""
lines = [
  "DevOps is awesome.",
  "Error: Disk not found.",
  "Server started successfully at 10:05 AM.",
  "OK"
]
for line in lines:
    if len(line)>len(longest_line):
        longest_line=line
print(longest_line)

print(max(lines))
