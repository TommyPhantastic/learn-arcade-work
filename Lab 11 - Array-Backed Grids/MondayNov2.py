my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]

print(my_list)

# Swaps values 15 and 14
# temp = my_list[0]
# my_list[0] = my_list[2]
# my_list[2] = temp

# Alternatively:

# my_list[0], my_list[2] = my_list[2], my_list[0]
#
# print(my_list)


# 15, 57, 14, 33, 72, 79, 26, 56, 42, 40
# 14, 57, 15, 33, 72, 79, 26, 56, 42, 40
# 14, 15, 57, 33, 72, 79, 26, 56, 42, 40
# 14, 15, 26, 33, 72, 79, 57, 56, 42, 40
# 14, 15, 26, 33, 72, 79, 57, 56, 42, 40
# 14, 15, 26, 33, 40, 79, 57, 56, 42, 72
# 14, 15, 26, 33, 40, 42, 57, 56, 79, 72
# 14, 15, 26, 33, 40, 42, 56, 57, 79, 72
# 14, 15, 26, 33, 40, 42, 56, 57, 79, 72
# 14, 15, 26, 33, 40, 42, 56, 57, 72, 79

def selection_sort(my_list):

    for cur_pos in range(len(my_list)):
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos

        # Swap
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp

my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
selection_sort(my_list)
print(my_list)