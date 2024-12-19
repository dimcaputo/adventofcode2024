import matplotlib.pyplot as plt

input = '0 89741 316108 7641 756 9 7832357 91'
lst_input = [int(x) for x in input.split()]
len_for_count ={}

def modif_stones(lst, number, count):
    if count < number:
        new_lst = []
        for item in lst:
            if item == 0:
                new_lst.append(1)
            elif len(str(item))%2 == 0:
                item = str(item)
                mid = int(len(item) / 2)
                new_lst.append(int(item[:mid]))
                new_lst.append(int(item[mid:]))
            elif len(str(item))%2 != 0:
                new_lst.append(item*2024)
        count += 1
        len_for_count[count] = len(new_lst)
        return modif_stones(new_lst, number, count)
    else:
        return lst

first = modif_stones(lst_input, 25, 0)
print(len_for_count)

plt.scatter(len_for_count.keys(), len_for_count.values())
plt.show