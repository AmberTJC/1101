def bubble_sort (master_list):
    length = len(master_list)
    for i in range (length):
        for j in range (0, length - i - 1):
            if master_list [j] > master_list [j + 1]:
                master_list[j], master_list [j + 1] = master_list [j + 1], master_list [j]


with open ("one_hundred.txt") as data:
    master_list = []
    for line in data:
        if len(line) >1:
            list_nums = line.split()
            list_nums = [int (i) for i in list_nums]
            master_list.extend(list_nums)
#print (master_list)
    for r in range (100):
        if r not in master_list:
            print (f"{r} is not present")

bubble_sort (master_list)
with open ("one_hundred_sorted.txt", "w") as f:
    f.write (str(master_list))