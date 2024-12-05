with open('/Users/dimitricaputo/Downloads/input5.txt') as f:
    order_pages = {}
    to_print = []
    for line in f.readlines():
        stripped = line.strip('\n')
        if '|' in stripped:
            order_pages[stripped.split('|')[0]] = stripped.split('|')[1]
        else: 
            to_print.append(stripped.split(','))

to_print.remove([''])
okay = []
sum_middle = 0

def check_updates(lst_lst, dico):
    for line in lst_lst:
        lst_temp = line.copy()
        for item in line[::-1]:
            if item not in dico.keys():
                lst_temp.remove(item)
            elif item in dico.keys() and dico[item] not in lst_temp:
                lst_temp.remove(item)
        if lst_temp == []:
            okay.append(line)

check_updates(to_print, order_pages)

for lst in okay:
    if len(lst)%2 != 0:
        mid = int(len(lst)/2)+1
        sum_middle += int(lst[mid])

print(sum_middle)


        
        


