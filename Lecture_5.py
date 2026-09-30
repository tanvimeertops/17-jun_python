# #range(end)
# print(list(range(3)))
# #0 1 2
# print(list(range(10)))
# print(list(range(-5))) #jump 1
# #   0 1 2
# print(list(range(0)))
# # 0 to -1
# print(list(range(1)))
# # 0

# #range 1 (start,end)
# print(list(range(1,3)))
# #1 2 

# print(list(range(-5,-1)))
# # -5 -4 -3 -2

# print(list(range(-4,-10)))
# # -4 -3

# print(list(range(5,1)))
# # range variation 2
# print(list(range(1,6,2)))
# #1 3 5
# print(list(range(0,-5,-1)))
# # -4 -3 -2 -1 0

# print(list(range(-5,0,-1)))
# # -5 -4 -3 -2 -1 

# print(list(range(0,5,1)))
# #0 1 2 3 4
# print(list(range(-5,-10,-1)))
# #-9 -8 -7 -6 -5
# print(list(range(-4,-6)))
# # -5 -4 
# print(list(range(5)))
# #0 to 4

# #for is iterator
# #range is iterable

# for i in range(10):
#     print(i)

# # print number from 1 to 100 
# for i in range(1,101):
#     print(i)


# print(list(range(5)))
# print(list(range(5,15,2)))
# # 5 7 9 11 13 
# print(list(range(-5,0,1)))
# #-5 -4 -3 -2 -1

# print(list(range(0,1)))

# for i in (list(range(0,1))):
#     print("Hello")

# for i in range(10):
#     if i==5:
#         break
#     print(i)
# for i in range(10):
#     if i==5:
#         continue
#     print(i)

# Good programming practice: if you dont use 
# variable in for loop the replace it with _ 
for _ in range(3):
    print("piyush")

# *	Pass

 	# It is not to be used in competitive 
    # programming or interviews. 
    # It is usually used in testing.
 	# The pass does nothing. 
    # It signifies that the programmer 
    # will later add some code to it.
    # Right now ignore this block.

for i in range(5):
    if i%2==0: #2 4
       pass
    print("other statement")

for i in range(0,10):
    if i%3==0:
        continue
    print(i,end=" ")
print()
for i in range(1,10):
    if i%3==0:
        break
    print(i,end=" ")
print()

# Nested Loops 
# * * * *
# * * * *


for _ in range(2):
    for _ in range(4):
        print("*",end=" ")
    print()

N=int(input("Enter the number :"))#5
flag=False

if N==1:
    print("Not a prime number")
elif N==2:
    print("Prime Number")
else:
    for i in range(2,N): 
        if N%i==0:
            flag=True
            break
        else:
            flag=False
    if flag==False:
        print("Prime Number")
    else:
        print("Not a prime Number")

    



