# Selection sort
def printing_speed_sort(printers_list):
    print_speed_list = []
    for i in printers_list:
        print_speed_list.append(i.print_speed)
    print(print_speed_list)
    for i in range(0, len(print_speed_list) - 1):
        minimum = i
        for j in range(minimum + 1, len(print_speed_list)):
            if print_speed_list[j] < print_speed_list[minimum]:
                minimum = j
        if minimum != i:
            print_speed_list[i], print_speed_list[minimum] = print_speed_list[minimum], print_speed_list[i]
    print(print_speed_list)


# Quick sort
def price_sort(price_list):
    for i in range(len(price_list)):
        price_list[i] = int(price_list[i].price)

    print(price_list)

    def partition(left_limit, right_limit):
        if right_limit - left_limit < 1:
            return

        left_index = left_limit + 1
        right_index = right_limit
        pivot = price_list[left_limit]

        while True:
            while price_list[left_index] < pivot and left_index < right_limit:
                left_index = left_index + 1
            while price_list[right_index] > pivot and right_index > left_limit:
                right_index = right_index - 1
            if left_index >= right_index:
                break
            temp = price_list[right_index]
            price_list[right_index] = price_list[left_index]
            price_list[left_index] = temp
        price_list[left_limit], price_list[right_index] = price_list[right_index], price_list[left_limit]

        partition(left_limit, right_index - 1)
        partition(right_index + 1, right_limit)

    left_limit = 0
    right_limit = len(price_list) - 1

    partition(left_limit, right_limit)
    return price_list
