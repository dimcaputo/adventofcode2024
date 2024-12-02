

with open('/Users/dimitricaputo/Downloads/input2.txt') as f:
    lines = f.readlines()
    lst_of_str_lst = [line.strip('\n').split() for line in lines]

lst_of_int_lst = []
for lst in lst_of_str_lst:
    lst_of_int_lst.append([int(x) for x in lst]) 

count = 0

for lst in lst_of_int_lst:
    for i in range(len(lst)-2):
        cond1 = lst[i] > lst[i+1] and lst[i+1] < lst[i+2]
        cond2 = lst[i] < lst[i+1] and lst[i+1] > lst[i+2]
        cond3 = lst[i] == lst[i+1] or lst[i+1] == lst[i+2]
        cond4 = abs(lst[i]-lst[i+1]) > 3 or abs(lst[i+1]-lst[i+2]) > 3
        if cond1 or cond2 or cond3 or cond4:
            count += 1
            break

print(len(lst_of_int_lst)-count)

#Part Two

count2 = 0

# for lst in lst_of_int_lst:
#     count_inter = 0
#     for i in range(len(lst)-2):
#         cond1 = lst[i] > lst[i+1] and lst[i+1] < lst[i+2]
#         cond2 = lst[i] < lst[i+1] and lst[i+1] > lst[i+2]
#         cond3 = lst[i] == lst[i+1]
#         cond4 = lst[i+1] == lst[i+2]
#         cond5 = abs(lst[i]-lst[i+1]) > 3
#         cond6 = abs(lst[i+1]-lst[i+2]) > 3
#         lst_bool = [cond1,cond2,cond3,cond4]
#         if cond5 == True or cond6 == True:
#             count2 += 1
#             break
#         if lst_bool.count(True) > 0:
#             count_inter += 1
#         if count_inter > 1:
#             count2 += 1
#             break

is_increasing = [lst[i] < lst[i+1] for i in range(len(lst)-1)]
is_decreasing = [lst[i] > lst[i+1] for i in range(len(lst)-1)]
is_different = [lst[i] != lst[i+1] for i in range(len(lst)-1)]
is_less_than_3 = [abs(lst[i]-lst[i+1]) for i in range(len(lst)-1)]

def is_safe(lstcondup, lstconddown, lstconddiff, lstcondless3):
    if all(lstcondup) and all(lstconddiff) and all(lstcondless3):
        return True
    elif all(lstconddown) and all(lstconddiff) and all(lstcondless3):
        return True
    else:
        return False
    
def can_be_made_safe():
    
    


