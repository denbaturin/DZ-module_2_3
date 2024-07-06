my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
zero = 0
while zero < len(my_list):
    new_list = my_list[zero]
    zero += 1
    if new_list == 0:
        continue
    elif new_list < 0:
        break
    else:
        print(new_list)