# *	Assignment Operator
# = is an assignment operator, 
# it will assign value to the variable
a = 25
print(a)
a=a+25
print(a)

# Shorthand
a+=25
print(a)

a/=2
print(a)

a*=2
print(a)

# *	Logical Operators
# AND
# True and True -> True
# True and False -> False 
# False and True -> False 
# False and False -> False

age=30
print((age>20)and(age<40))

print(('Aakar' == 'Aakar') and (-2 < -3))

# OR
# True or True -> True 
# True or False -> true 
# False or True -> true
# False or False -> False

print((2 < 3) or (2 < 4))
print(('Aakar' == 'aakar') or (-2 < -3))
# Not or !=
# not True -> False # not False -> True
print(not('piyush'=='Piyush'))
# *	Conditional Statement
# m_comp = 120 
# m_culture = 'positive' 
# m_distace = 300

# g_comp = 110 
# m_culture = 'positive' 
# m_distace = 30

# if m_comp>80:
#     print("Microsoft Criteria filled!!!")
# elif g_comp>80:
#     print("Google Criteria filled!!!")
# else:
#     print("sad life!!!")


# Nested 
m_comp = 110
m_culture = 'positive' 
m_distace = 300

g_comp = 110
g_culture = 'positive' 
g_distace = 3000

if m_comp>80 and g_comp>80:
    if m_distace>g_distace:
        print('Go to Google') 
    else:
        print('Go to Microsoft') 


# Problem Statement: Traffic Lights
# You have to ask about the color of 
# the traffic light from the user, if:
# it is green, then print go,
# it is yellow, then print wait, 
# it is red, then print stop
# green -> go
# yellow -> wait # red -> stop

light=input("Enter the color of light :")
if light=='green':
    print("go")
elif light=='yellow':
    print("wait")
elif light=='red':
    print("stop")
else:
    print("invalid input...")