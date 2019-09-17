# Selection sort
def printing_speed_sort(printers_list):
    print_speed_list = []
    for i in printers_list:
        print_speed_list.append(i.print_speed)
    print(print_speed_list)

    for i in range(0, len(print_speed_list) - 1):
        minumum = i
        for j in range(minumum + 1, len(print_speed_list)):
            if print_speed_list[j] < print_speed_list[minumum]:
                minumum = j
        if minumum != i:
            print_speed_list[i], print_speed_list[minumum] = print_speed_list[minumum], print_speed_list[i]
    print(print_speed_list)


