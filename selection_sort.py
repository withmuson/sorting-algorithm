def selection_sort(list):
    size = len(list)
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if list[i] < list[min_idx]:
                min_idx = i

        # put min at the correct position
        (list[step], list[min_idx]) = (list[min_idx], list[step])


data = [-2, 45, 0, 11, -9]

selection_sort(data)

print('Sorted list in Ascending Order:')
print(data)
