import re

file = open('row.txt', 'r', encoding='utf-8')
# print(file.read())

s = 'The Abba in Alps, and Abba in Singapore'
s = 'a+b abbs abbbs abbbbs'
s = 'I have defined a variable with the name hello_world'
s = 'jack.john.son.help@myspace.some_domain'
s = 'https://www.kbtu.kz/auth?id=23B123123'

# reg = re.compile('[a-zA-Z0-9_.]+@[a-zA-Z0-9_]+[.][a-zA-Z0-9_]+')

try:
    reg = re.compile(r'(http(s)?://)?(www.)?[a-zA-Z0-9_-]+[.](kz|com|ru|edu)([/][a-z_.-]+[?]id=[a-zA-Z0-9]+)?')
    result = reg.search(s)
    print(result.group())
except AttributeError:
    print("Sorry!")

# login
# password
# email -> abc@organization.kz
# jack.johnson@myspace.com
# abc -> [a-zA-Z0-9_.]+@[a-zA-Z0-9_]+.(ru|com|kz|edu|gov|net|ua|org)
# + -> [1;+infinity)
# * -> [0;+infinity)
# ? -> [0;1]
# {1,4} -> [1]

#helloDearWorld -> hello_dear_world
#hello_dear_world -> helloDearWorld
#['hello', 'dear', 'world']
# camel_case_string = helloDearWorld
# helloDearWorld