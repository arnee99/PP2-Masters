import re

# login
# password
# email -> abc@organization.kz
# abc -> [a-zA-Z0-9_.]+@[a-zA-Z0-9_.]+.(ru|com|kz|edu|gov|net|ua|org)
# + -> [1;+infinity)
# * -> [0;+infinity)
# ? -> [0;1]
# {1,3} -> [1;3]
# arnee.99@gmail.com