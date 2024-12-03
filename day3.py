import regex as re

with open('/Users/dimitricaputo/Downloads/input3.txt') as f:
    txt = f.read()

search_for_mul = re.findall(r'mul\(\d{1,3}\,\d{1,3}\)', txt)

change_to_tup = []

for item in search_for_mul:
    change_to_tup.append(eval(item[3:]))

count = 0
for item in change_to_tup:
    count += item[0]*item[1]




# Part 2

remove_portions = re.sub(r'don\'t\(\).*do\(\)','',txt)
search_for_mul2 = re.findall(r'mul\(\d{1,3}\,\d{1,3}\)', remove_portions)

print(len(txt))
print(len(remove_portions))

change_to_tup2 = []

for item in search_for_mul2:
    change_to_tup2.append(eval(item[3:]))

count2 = 0
for item in change_to_tup2:
    count2 += item[0]*item[1]

print(count2)