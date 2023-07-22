def insertion_sort(list):

    for step in range(1, len(list)):
        key = list[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<list[j] to key>list[j].        
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        list[j + 1] = key


data = [9, 5, 1, 4, 3]
insertion_sort(data)
print('Sorted list in Ascending Order:')
print(data)