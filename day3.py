import regex as re

with open('/home/dimitri.caputo@Digital-Grenoble.local/Downloads/input3') as f:
    txt = f.read()

search_for_mul = re.findall(r'mul\(\d{1,3}\,\d{1,3}\)', txt)

change_to_tup = []

for item in search_for_mul:
    change_to_tup.append(eval(item[3:]))

count = 0
for item in change_to_tup:
    count += item[0]*item[1]




# Part 2
txt_copy = txt

lstsepdo = txt_copy.split('do()')
lst_sepsep = [item.split("don't")[0] for item in lstsepdo]
new_txt = ''.join(lst_sepsep)

search_for_mul2 = re.findall(r'mul\(\d{1,3}\,\d{1,3}\)', new_txt)

change_to_tup2 = []

for item in search_for_mul2:
    change_to_tup2.append(eval(item[3:]))

count2 = 0
for item in change_to_tup2:
    count2 += item[0]*item[1]

print(count2)