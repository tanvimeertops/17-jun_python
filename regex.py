import re
# text = 'Title: Mrs. Lacy'

# # Capturing group
# pattern1=r'(Mr|Mrs|Ms)\.?\s[A-Z][a-z]+'
# match1=re.search(pattern1,text)
# print(match1)
# print(match1.group(1))

# # Non capturing group
# pattern2=r'(?:Mr|Mrs|Ms)\.?\s[A-Z][a-z]+'
# match2=re.search(pattern2,text)

# print(match2)




data = """Dave Martin 615-555-7164
173 Main St., Springfield RI 55924 davemartin@bogusemail.com

Charles Harris 800-555-5669
969 High St., Atlantis VA 34075 charlesharris@bogusemail.com

Eric Williams 560-555-5153
806 1st St., Faketown AK 86847 laurawilliams@bogusemail.com

Corey Jefferson 900-555-9340
826 Elm St., Epicburg NE 10671 coreyjefferson@bogusemail.com

Jennifer Martin-White 714-555-7405
212 Cedar St., Sunnydale CT 74983 jenniferwhite@bogusemail.com

Erick Davis 800-555-6771
519 Washington St."""

pattern="\d{3}-\d{3}-\d{4}"

print(re.match(pattern,data))
print(re.search(pattern,data))
print(re.findall(pattern,data))

numbers=re.finditer(pattern,data)
for i, num in enumerate(numbers):
    print(i,num)
    if i==3:
        break

text = '123' 
pattern1="\d{3}"
match1=re.fullmatch(pattern1,text)
print(match1)

def validate_phone(num):
    pattern=r'\d{10}'
    return bool(re.fullmatch(pattern,num))

print(validate_phone('7854696582'))
print(validate_phone('78546%6582'))
print(validate_phone('785469'))

pattern=r'\b[A-Z][a-z]*\b'
text = 'A Tops Tech is in Surat'
print(re.findall(pattern,text)) 


text="Started at 09:30, ended 13:45:10"
pattern2=r'\d{2}:\d{2}(?::\d{2})?'
print(re.findall(pattern2,text))

#*	Extract Words Ending in 'ing'
text="Running, testing, and logging complete." 
pattern=r'\b\w+ing\b'
print(re.findall(pattern,text))

#*	Extract Error Codes (ERR, WARN, FAIL)
text = 'ERR123 occurred after WARN456 and FAIL789' 
pattern=r'\b(?:ERR|WARN|FAIL)\d+\b'
print(re.findall(pattern,text))

text = 'Accessed 192.168.1.1 and 10.0.0.4' 
pattern=r'\d{1,3}(?:\.\d{1,3}){3}'
print(re.findall(pattern,text))
match1=re.sub(pattern, '[IP]', text)
print(match1)

#*	Regex for Email
pattern = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$' 