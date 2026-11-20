import sys
encoding = sys.getdefaultencoding() 
print(encoding)

# file = open("sample2.txt", "r")

file = open('sample2.txt','w') 
file.write('This is\n multiple\n line') 
file.close()
# file = open('sample.txt', 'w+') 
# file.writelines(["1.\n", "2.\n", "3."]) 
# file.close()

# file = open("sample.txt", "r+") 
# content = file.read() 
# print(content)
# file.close()

# file = open("sample.txt", "r+") 
# content = file.readline() 
# print(content)
# file.close()

# file = open("sample.txt", "r+") 
# content = file.readlines() 
# print(content)
# file.close()

file = open("sample2.txt", "r+")
while True:
    chunk = file.read(5)
    if not chunk:
        break
    print(chunk)
file.close()

#*	Exceptions Handling

try:
    file = open('sfsfdsdfs.txt','r') 
except FileNotFoundError:
    print('OOps the file is not present')

print('This is the end of the program')

try:
    file = open('notes344.txt', 'r') 
    content = file.read() 
    print(content)
    file.close()
except FileNotFoundError:
    print('OOps the file is not present')
except PermissionError:
    print('You do not have permission to access this file')
except Exception as e:
    print('An error occurred:', str(e))
except:
    print("Unknown error occurred")
finally:
    print('This is the end of the program')

try:
    file = open('notes.txt', 'w') 
    file.write('This is the file') 
    file.close()
    print('Write operation successful') 
except PermissionError:
    print('You do not have permission to write to this file')
except:
    print('An error occurred while writing to the file')

file = open('demo.txt','w')
file.write('This is a demo file')
file.close()

# file = open('demo.txt','r')
# print(file.read()) 
# file.close()

with open('demo.txt','r') as file1:
    print(file1.read())

# file1.write('This is a new line in the demo file')

with open('input.txt','w') as file1:
    file1.write('This is line 1.\n') 
    file1.write('Room 202 has 4 ACs.\n') 
    file1.write('There are 3 dogs and 4 cats.\n') 
    file1.write('ID: 007, Code: 123456')
max_digit = -1 
result = ''
with open('input.txt', 'r') as file: 
    for line in file:
        digit_count = 0
        for char in line:
            if char.isdigit():
                digit_count+=1
                if digit_count > max_digit:
                    max_digit = digit_count
                    result = line
    print(result)