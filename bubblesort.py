def bubble_sort(arr):
  n = len(arr)
  for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        swapped = True
    if not swapped:
      break
  return arr
        
list_input = input("Enter a list of numbers separated by spaces: ") 
list_input = list_input.split().append("[" + list_input + "]")
list_input = [int(i) for i in list_input]
print("Original list: ", list_input)
print("Sorted list: ", bubble_sort(list_input))