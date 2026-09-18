print(3 * 10 / 2)
print((3 * 10) / 2)
print(45 % 10 / 2)
print(True and not False)

a=5
if a>10:
    print(a)
    if a%5==2:
        print("Bla")
else:   
    print(a)
    print('1234')

print("Five")
print("Five")
print("Five")
'''
variable initialization 
while (condition)
{
action
update variable
}

'''
# # while
# # Print Numbers from 1 to 15 
# count=1
# while(count<=15):
#     print(count)
#     count+=1


# #break
# count=1
# while(count<=15):
#     if count==10:
#         break
#     print(count)
#     count+=1

#continue
count=0
while(count<=15):
    count+=1
    if count==10:
        continue
    print(count)

count = 0  
while count <= 5: #5<=5
    count += 1 #6
    if count == 3: #6==3
        continue
    print(count) #5

#while else
count=0 #initialization
while count<=15: #condition
    count+=1 # 16
    print(count) #1
    if count==10: #
        break
else:
    print("completed")
    print("yay")