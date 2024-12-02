from math import *

# First part
lst1 = []
lst2 = []
with open('/Users/dimitricaputo/Downloads/input') as f:
    lines = f.readlines()
    for line in lines:
        lst1.append(int(line.strip('\n').split('   ')[0]))
        lst2.append(int(line.strip('\n').split('   ')[1]))

sorted_lst1 = list(sorted(lst1))
sorted_lst2 = list(sorted(lst2))

sum_diffs = 0
for item1,item2 in zip(sorted_lst1,sorted_lst2):
    sum_diffs += abs(item1-item2)

print(sum_diffs)

# Second part

similarity_score = 0
for item in lst1:
    similarity_score += item * lst2.count(item)

print(similarity_score)

