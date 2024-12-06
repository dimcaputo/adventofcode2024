try:
    with open('/Users/dimitricaputo/Downloads/input5.txt') as f:
        order_pages = []
        to_print = []
        for line in f.readlines():
            stripped = line.strip('\n')
            if '|' in stripped:
                order_pages.append([stripped.split('|')[0]],stripped.split('|')[1])
            else: 
                to_print.append(stripped.split(','))
except:
    with open('/home/dimitri.caputo@Digital-Grenoble.local/Downloads/input5.txt') as f:
        order_pages = []
        to_print = []
        for line in f.readlines():
            stripped = line.strip('\n')
            if '|' in stripped:
                order_pages.append(([stripped.split('|')[0]],stripped.split('|')[1]))
            else: 
                to_print.append(stripped.split(','))

to_print.remove([''])
okay = []
sum_middle = 0

def in_tuple_left(page):
    verif = False
    for tup in order_pages:
        if page == tup[0]:
            verif = True
    return verif

def in_tuple_right(page):
    verif = False
    for tup in order_pages:
        if page == tup[1]:
            verif = True
    return verif

def get_left(page):
    lst = []
    for tup in order_pages:
        if page == tup[1]:
            lst.append(tup[0])
    return lst

def check_updates(lst_lst, dico):
    for line in lst_lst:
        lst_temp = line.copy()
        for item in line[::-1]:
            if not in_tuple_left(item) and not in_tuple_right(item):
                lst_temp.remove(item)
            elif in_tuple_right(item) and all([x not in lst_temp for x in get_left(item)]):   #Not good here
                lst_temp.remove(item)
        if lst_temp == []:
            okay.append(line)

check_updates(to_print, order_pages)

for lst in okay:
    if len(lst)%2 != 0:
        mid = int(len(lst)/2)+1
        sum_middle += int(lst[mid])

print(sum_middle)


        
        


