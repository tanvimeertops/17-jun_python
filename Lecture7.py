# def transaction_message():
#     print ('*' * 20) 
#     print('Transaction Complete') 
#     print('Thank you')
#     print ('*' * 20)

# transaction_message()

# #function Example
# # def area_of_circle():
# #     print(3.14*5*5)

# # area_of_circle()
# # print(area_of_circle()+10)


# # def abc():
# #     return 5

# # print(abc())
# # a=abc()
# # print(a)

# def area_of_circle():
#     return 3.14*5*5

# print(area_of_circle())
# print(area_of_circle()+10)

# def abc():
#     print('Hello')
#     return
#     print('World')
#     return 'Tops'

# print(abc())

# def even_odd():
#     a=20
#     if a%2==0:
#         return 'Even'
#     else:
#         return 'Odd'

# print(even_odd())

# #*	Parameter and Argument in Function
# def area_of_circle_5():
#     return 3.14*5*5
# print(area_of_circle_5())

# def area_of_circle_20():
#     return 3.14*20*20
# print(area_of_circle_20())


# def area_of_circle(radius):
#     return 3.14*radius*radius

# print(area_of_circle(6))

# def sum(a,b):
#     return a+b

# print(sum(10,20))

# def sum(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b

# def calculate_salary(base_mothly,bonus,equity):
#     yearly_base=mul(base_mothly,12)
#     yearly_base_bonus=sum(yearly_base,bonus)
#     total_salary=sum(yearly_base_bonus,equity)
#     return total_salary

# a=calculate_salary(10000,5000,10000)
# print(a+100000)

#Scope of Variable

# a = 1 # global scope
# def area_circle(radius):
#     area = 3.14 * (radius ** 2) # area is having a local scope of the function only 
#     return area
# b = area_circle(10) # global 
# print(a) # print 1
# print(b) # 314.0 
# print(area) # error

'''
a = 1 #global 
def abc():
    a = 2 #local scope 
    print(a) # 2
abc() #2
print(a) # print 1

a = 1 #global 
def abc():
    global a
    a = 2 #local scope 
    print(a) # 2
abc() #2
print(a) # print 2


def foo(a): #0
    if(a): #
        return 100
    a += 20 #0+20
    return a
print(foo(1)) #20


def solve(a, b): 
    print('Function Started') 
    return 0
    c = a + b 
    print('Function Ends')
c = solve(2, 3) #0
print(c)

# Simple interest
# take principal, rate and time as input from user 
# and create a function 
#to calculate simple interest # (p * r * t)/ 100
# p=float(input('Enter Principal: '))
# r=float(input('Enter Rate: '))
# t=float(input('Enter Time: '))

# def simple_interest(p, r, t):
#     return (p * r * t) / 100

# simple_interest_value = simple_interest(p, r, t)
# print('Simple Interest:', simple_interest_value)

def bio_data(name, age, gender): 
    print("Name: ", name)
    print("Age: ", age)
    print("Gender: ", gender)

bio_data(age=23,gender= "Male", name="aakar")

def bio_data(name, age=0, gender=None): 
    print("Name: ", name)
    print("Age: ", age)
    print("Gender: ", gender)

bio_data( name="aakar")
'''

print(round(3.6546546,4)) #3.6547
def abc(name, gender, age = 0): 
    print(name,gender,age)
abc(name = 'aakar', gender = 'Male')

def abc(a,b,c=10): 
    return a,b,c
print(abc(1,2))



