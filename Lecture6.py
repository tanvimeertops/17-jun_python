# N=235
# print(N%10)

# N=123
# print(N//10)

# Question 2

# Print the Digits of Number '459' in reverse order 
# print : 9 5 4

#take input from user
#To extract last digit
#To remove the last from N 
# N=int(input("Enter a value in positive integer :"))
# while N>0:
#     print(N%10,end="")
#     N=N//10

#Print sum of digits of N. N > 0
# N = 6531
# 6+5+3+1 = 15.	print(15)

#input from user
#while N>0
#N%10 
#ans=ans+N
#N//10

# N=int(input("Enter the number in positive integer"))
# ans=0
# while N>0:
#     ans+=N%10
#     N//=10


# print(ans)

# Add a given digit to the back of a given number N
#   N > 0
#   0 <= D <= 9

# N=int(input("Enter positive integer"))
# D=int(input("enter value greater than 0 less than 10"))

# N=N*10+D
# print(N)

# N=-256
# if N<0:
#     copy=N*-1
# else: 
#     copy=N 
# rev=0 
# while copy>0:
#     d=copy%10
#     rev=rev*10+d
#     copy=copy//10

# if N<0:
#     rev=rev*-1
# print(rev)
    
# T=int(input("enter a single digit :"))
# while T>0:
#     N=int(input("Enter a digit :"))
#     if N<0:
#         copy=N*-1
#     else:
#         copy=N
#     rev=0
#     while copy>0:
#         d=copy%10 #last digit
#         rev=rev*10+d # 
#         copy//=10 #
#     if N<0:
#         rev=rev*-1
    
#     print(rev)

#     T-=1    

for _ in range(5):
    print('*'*5)

for i in range(1,6):
    print('*'*i)

