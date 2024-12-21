import os

with open(os.path.expanduser('~/Downloads/input10.txt')) as f:
    txt = [x.strip('\n') for x in f.readlines()]

pos_zeros = [(i,j) for i in range(len(txt)) for j in range(len(txt)) if txt[i][j] == '0']

lst_dico_numbers = [{} for x in range(0,9)]

directions = [(x,y) for x in [-1, 0, 1] for y in [-1, 0, 1] if (x,y) != (0,0)]

def get_next_number_pos(position, number):
    tour = 0
    for tup in directions:
        ind,col = position
        if 0 <= ind+tup[0] <= len(txt)-1:
            ind += tup[0]
        if 0 <= col+tup[1] <= len(txt)-1:
            col += tup[1]
        if txt[ind][col] == str(number + 1):
            if position in lst_dico_numbers[number].keys():
                lst_dico_numbers[number][position].append((ind, col))
            else:
                lst_dico_numbers[number][position] = [(ind,col)]

def build_dicos():
    for pos in pos_zeros:
        get_next_number_pos(pos, 0)
    for x in range(1,9):
        for lst in lst_dico_numbers[x-1].values():
            for (ind,col) in lst:
                get_next_number_pos((ind,col), x)

build_dicos()


# def remove_deadends():
#     for i in range(len(lst_dico_numbers)-1):
#         for k,v in lst_dico_numbers[i].items():
#             for item in v:
#                 if item not in lst_dico_numbers[i+1].keys():
#                     v.remove(item)
#             # if v == []:
#             #     lst_dico_numbers[i].pop(k)

# remove_deadends()


def run_through(list_of_dict):
    dico_zero_to_nine = {}
    for k,v in list_of_dict[0].items():
        for item in v:
            lst = one_step_r(item,0)
        if k not in dico_zero_to_nine.keys():
            dico_zero_to_nine[k] = lst
        else:
            dico_zero_to_nine[k].extend(lst)
    return dico_zero_to_nine

def one_step_r(tup, number):
    if number == 8:
        lst_9 = []
        for k,v in lst_dico_numbers[number].items():
            for item in v:
                lst_9.append(item)
                return lst_9
    else:
        lst_temp = []
        for k,v in lst_dico_numbers[number].items():
            for item in v:
                lst_temp.extend(one_step_r(item, number+1))

dict_results = run_through(lst_dico_numbers)


count = 0
for k,v in dict_results.items():
    count += len(v)

print(count)