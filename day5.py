try:
    with open('/Users/dimitricaputo/Downloads/input5.txt') as f:
        order_pages = []
        to_print = []
        for line in f.readlines():
            stripped = line.strip('\n')
            if '|' in stripped:
                order_pages.append((stripped.split('|')[0],stripped.split('|')[1]))
            else: 
                to_print.append(stripped.split(','))
except:
    with open('/home/dimitri.caputo@Digital-Grenoble.local/Downloads/input5.txt') as f:
        order_pages = []
        to_print = []
        for line in f.readlines():
            stripped = line.strip('\n')
            if '|' in stripped:
                order_pages.append((stripped.split('|')[0],stripped.split('|')[1]))
            else: 
                to_print.append(stripped.split(','))

to_print.remove([''])
okay = []
sum_middle = 0

def check_updates(lst_lst, lst_tup):
    for lst in lst_lst:
        is_okay = True
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                if (lst[j], lst[i]) in lst_tup:
                    is_okay = False
        if is_okay == True:
            okay.append(lst)

check_updates(to_print, order_pages)            

for lst in okay:
    mid = int(len(lst)/2)
    sum_middle += int(lst[mid])

print(sum_middle)

# Part 2

left_to_print = [lst for lst in to_print if lst not in okay]

sum_middle_2 = 0
modified = []

def modify_updates(lst_lst, lst_tup):
    for lst in lst_lst:
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                if (lst[j], lst[i]) in lst_tup:
                    (lst[j], lst[i]) = (lst[i], lst[j])
        modified.append(lst)

modify_updates(left_to_print, order_pages)

for lst in modified:
    mid = int(len(lst)/2)
    sum_middle_2 += int(lst[mid])

print(sum_middle_2)


        
        


