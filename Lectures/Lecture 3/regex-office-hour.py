import re
# Abby said that Debby is a good friend!
# [ove]
# str = 'Some_good_result_string_sequence'
# _abc
# obj = re.compile('[a-z]+_[a-z]+')
# ab [0; +infinity) -> a, ab, abb, abbb, abbbb
# (ove)

# str = 'Some good. Result string, which is good'
# _abc
# obj = re.compile(r'[ .,]')

str1 = "some_random_snake_case" #someRandomSnakeCase
obj = re.compile(r'([a-zA-Z0-9]+)_([a-zA-Z0-9]+)')
# \w -> [a-zA-Z0-9_]
p = obj.findall(str1)
res = ''
for tup in p:
    for word in tup:
        res += word.capitalize()
        
res = res[0].lower() + res[1:]
print(res)

# str = obj.sub(':', str)
# print(str)