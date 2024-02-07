import timeit

# Provided list elements
my_list = [
    836, 279, 580, 520, 923, 185, 129, 167, 954, 959,
    84, 144, 136, 837, 156, 727, 327, 823, 682, 784,
    595, 512, 990, 180, 981, 737, 195, 6, 60, 186, 936,
    240, 710, 449, 224, 999, 501, 755, 483, 384, 994,
    673, 217, 125, 534, 460, 436, 93, 825, 924, 654,
    566, 312, 657, 807, 294, 834, 761, 168, 174, 948,
    796, 984, 600, 291, 846, 859, 41, 527, 950, 853,
    181, 462, 121, 539, 522, 916, 594, 764, 621, 819,
    285, 153, 96, 444, 545, 873, 879, 73, 416, 904,
    540, 889, 626, 435, 676, 500, 478, 417, 956
]

# Function to print the result
def print_result(sort_name, unsorted_list, sorted_list, execution_time):
    print("\n"+"\033[93m=" * 80, "\n")
    print("\033[92m{} - Unsorted List \033[97m\n{}".format(sort_name, unsorted_list))
    print("\n"+"\033[93m=" * 80, "\n")
    print("\033[92m{} - Sorted List \033[97m\n{}".format(sort_name, sorted_list))
    print("\n"+"\033[93m=" * 80, "\n")
    print("\033[92m{} - Execution Time \033[97m\n{}".format(sort_name, execution_time))
    print("\n"+"\033[93m=" * 80, "\n")

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr  # Corrected: Return the sorted list

# Displaying the results
print_result("Selection Sort", my_list, selection_sort(my_list.copy()), timeit.timeit(lambda: selection_sort(my_list.copy()), number=1000))