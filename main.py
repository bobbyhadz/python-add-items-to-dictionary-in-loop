# Adding items to a Dictionary in a Loop in Python

my_list = [
  ('first', 'bobby'),
  ('last', 'hadz'),
  ('site', 'bobbyhadz.com')
]

my_dict = {}

for item in my_list:
    my_dict[item[0]] = item[1]

# 👇️ {'first': 'bobby', 'last': 'hadz',
#     'site': 'bobbyhadz.com'}
print(my_dict)