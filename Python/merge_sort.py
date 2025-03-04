# ***WARNING*** this did not pass all of its tests

# arr is an array of integers
def count_inversions(arr):
    inversions = 0
    is_sorted = False
    # loops until the array has been sorted
    # this is the same as 'while is_sorted == False'
    while not is_sorted:
        is_sorted = True
        # iterates through and sorts the array
        for x in range(len(arr) - 1):
            if arr[x] > arr[x + 1]:
                temp = arr[x]
                arr[x] = arr[x + 1]
                arr[x + 1] = temp
                # counts the number of inversions
                # an inversion is when i < j but arr[i] > arr[j]
                inversions += 1
                is_sorted = False
    return inversions
