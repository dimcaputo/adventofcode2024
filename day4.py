with open('/home/dimitri.caputo@Digital-Grenoble.local/Downloads/input4') as f:
    txt = f.readlines()

#Horizontal reading
count_hor = 0

for line in txt:
    for i in range(len(txt)-3):
        if (line[i], line[i+1], line[i+2], line[i+3]) == ('X', 'M', 'A', 'S') or (line[i], line[i+1], line[i+2], line[i+3]) == ('S', 'A', 'M', 'X'):
            count_hor += 1

#Vertical reading
count_ver = 0

lst_lst_col = [[] for x in range(len(txt[0]))]

for lst_row in txt:
    for i in range(len(lst_row)):
        lst_lst_col[i].append(lst_row[i])

for lst_col in lst_lst_col:
    for i in range(len(lst_col)-3):
        if (lst_col[i], lst_col[i+1], lst_col[i+2], lst_col[i+3]) == ('X', 'M', 'A', 'S') or (lst_col[i], lst_col[i+1], lst_col[i+2], lst_col[i+3]) == ('S', 'A', 'M', 'X'):
            count_ver += 1

#Diagonal rising
count_diag_rise = 0


for i in range(len(lst_lst_col)-3):
    for j in range(len(lst_lst_col[0])-3):
        if (lst_lst_col[i][j+3], lst_lst_col[i+1][j+2], lst_lst_col[i+2][j+1], lst_lst_col[i+3][j])  == ('X', 'M', 'A', 'S') or (lst_lst_col[i][j+3], lst_lst_col[i+1][j+2], lst_lst_col[i+2][j+1], lst_lst_col[i+3][j])  == ('S', 'A', 'M', 'X'):
            count_diag_rise += 1

#Diagonal decreasing
count_diag_dec = 0


for i in range(len(lst_lst_col)-3):
    for j in range(len(lst_lst_col[0])-3):
        if (lst_lst_col[i][j], lst_lst_col[i+1][j+1], lst_lst_col[i+2][j+2], lst_lst_col[i+3][j+3])  == ('X', 'M', 'A', 'S') or (lst_lst_col[i][j], lst_lst_col[i+1][j+1], lst_lst_col[i+2][j+2], lst_lst_col[i+3][j+3])  == ('S', 'A', 'M', 'X'):
            count_diag_dec += 1

final = count_hor + count_ver + count_diag_rise + count_diag_dec

print(count_hor, count_ver, count_diag_rise, count_diag_dec, final)


# Part 2
count_x = 0
for i in range(1, len(lst_lst_col)-1):
    for j in range(1, len(lst_lst_col[0])-1):
        if lst_lst_col[i][j] == 'A':
            if lst_lst_col[i-1][j-1] == 'M' and lst_lst_col[i+1][j-1] == 'S' and lst_lst_col[i-1][j+1] == 'M' and lst_lst_col[i+1][j+1] == 'S':
                count_x += 1
            elif lst_lst_col[i-1][j-1] == 'M' and lst_lst_col[i+1][j-1] == 'M' and lst_lst_col[i-1][j+1] == 'S' and lst_lst_col[i+1][j+1] == 'S':
                count_x += 1
            elif lst_lst_col[i-1][j-1] == 'S' and lst_lst_col[i+1][j-1] == 'M' and lst_lst_col[i-1][j+1] == 'S' and lst_lst_col[i+1][j+1] == 'M':
                count_x += 1
            elif lst_lst_col[i-1][j-1] == 'S' and lst_lst_col[i+1][j-1] == 'S' and lst_lst_col[i-1][j+1] == 'M' and lst_lst_col[i+1][j+1] == 'M':
                count_x += 1

print(count_x)



