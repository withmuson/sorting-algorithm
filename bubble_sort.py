def bubble_sort(list):
    
  # loop through each element of list
  for i in range(len(list)):
        
    # keep track of swapping
    swapped = False
    
    # loop to compare list elements
    for j in range(0, len(list) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if list[j] > list[j + 1]:

        # swapping occurs if elements
        # are not in the intended order
        temp = list[j]
        list[j] = list[j+1]
        list[j+1] = temp

        swapped = True
          
    # no swapping means the list is already sorted
    # so no need for further comparison
    if not swapped:
      break

data = [-2, 45, 0, 11, -9]

bubble_sort(data)

print('Sorted list in Ascending Order:')
print(data)