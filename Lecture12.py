d={}
print(type(d))

d=dict()
print(type(d))   

a = 'a'
d={a: 1, 'b': 2}
print(d)

# d={[1,2,3,4]:'1'}
# print(d)

d={(1,2,3,4):'1'}
print(d)

d={2:'1'}
print(d)

nicknames = { "Madhuri": "Sweety",
"Vinoth": "Appu",
"Shubham": "Zoo Zoo",
"Kusum": "ku ku",
"Aakar": "Golu"
}
# print(nicknames[0])
print(nicknames["Madhuri"])
print(nicknames["Aakar"])

# print(nicknames['avd'])

print(nicknames.get("Kusum"))

print(nicknames.get('abv','Not Present')) 
#*	Inserting values in Dictionary
a = {True: 'a', 'a': 1, 2: False, 3.14: 'pi'}
a[True] = 'b'
print(a) 

a[False] = 12 
print(a) 

# *	Updating value from the dictionary using a key
nicknames['Kusum'] = 'New Value' 
print(nicknames)

#*	Length of a Dictionary
print(len(nicknames))

#*	Delete a key from a Dictionary
del nicknames['Aakar']
print(nicknames)
print(len(nicknames))

## pop function 
print(nicknames.pop('Vinoth'))
print(nicknames)
print(len(nicknames))

print(nicknames.pop('Vinoth','Default value'))
#*	Get keys and values of Dictionary
nicknames = { "Madhuri": "Sweety",
"Vinoth": "Appu",
"Shubham": "Zoo Zoo",
"Kusum": "ku ku",
"Aakar": "Golu"
}
print(nicknames.keys())
print(nicknames.values())

#*	Iterating a Dictionary
for key in nicknames:
    print(f'keys:{key},value:{nicknames[key]}')

for key,value in nicknames.items():
    print(f'keys:{key},value:{value}')

# Modifying multiple keys 
d = {'a':1,'b':2, 'c':3}
for key in d.keys():
    d[key] = d[key]**2
print(d)

print("Aakar" in nicknames)
print('Golu' in nicknames)

#*	Count frequency of characters

input = 'Aakar Sharma'
freq={}
for ci in input: #A
    if ci not in freq:
        freq[ci] = 0 #  A:0
    freq[ci] += 1
print(freq)

#*	Sets
s=set()
print(type(s))

# set with default elements 
s={1,2,3,45,12,78,12,3,4,5,6,7,8,9}
print(s)

# print(s[1])

s= {1,True, (1,2),'a'} 
print(s)

# s = {True, [1,2,3]}
# print(s)

s= {1,True, (1,2),'a'}
s.add(False)
s.add(False)
print(s)

# update an element 
s = {'a','b', 'c'}
s.update(['d','e','f'])
print(s)

# delete an element inside the set 
s.remove('a')
print(s)
print(len(s))

for e in s:
    print(e)

print('a' in s)
print('d' in s)

food_that_you_like_to_eat = {'Pizza', 'Noodles', 'Pasta', 'Chocolates', 'Burger'} 
food_that_are_expensive = {'Pizza', 'Croissant', 'Avocado'}
print(food_that_you_like_to_eat.intersection(food_that_are_expensive))
print(food_that_you_like_to_eat.union(food_that_are_expensive))
print(food_that_you_like_to_eat.difference(food_that_are_expensive))
print(food_that_are_expensive-food_that_you_like_to_eat)

#*	Given a sentence count the number of unique words.
sentence = 'This is a sentence. This is not a paragraph.' 
words=sentence.split(' ')
print(words)
print(len(words))

unique=set(words)
print(unique)
print(len(unique))

# Ports in PC
free_ports = list(range(8000,9999))
used_ports=set()

if 8001 in free_ports:
    print('Port is free')
    free_ports.remove(8001)
    used_ports.add(8001)
else :
    print('Port is already in use')


#lambda function
#lambda arguments:expression

# def add(x,y):
#     return x+y

# print(add(2,3))

add=lambda x,y:x+y
print(add(2,3))

logs = { 'server1_logs' : 
        [ 
            {'timestamp': '2024-07-18 10:04:10', 'level': 'ERROR', 
             'message': 'Disk full'},
            {'timestamp': '2024-07-18 10:00:01', 'level': 'INFO', 
             'message': 'Server started'}, 
            ],
        'server2_logs' :
        [ 
            {'timestamp': '2024-07-18 10:01:17', 'level': 'ERROR', 
             'message': 'Database connection failed'}, 
            {'timestamp': '2024-07-18 10:02:45', 'level': 'WARNING', 
            'message': 'High memory usage'}, 
            ] 
        }

merged_logs=[]
for key,value in logs.items():
    merged_logs.extend(value)
# print(merged_logs)

# sort on the timestamp


all_logs=sorted(merged_logs,key=lambda x:x['timestamp'],reverse=True)

print(all_logs)