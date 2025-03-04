# a is an array of integers
def count_swaps(a):
    swaps = 0
    # bubble sort
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                # when a swap is made 1 is added to the counter
                swaps += 1
    # prints the number of swaps and the elements in the first and last positions
    print("Array is sorted in " + str(swaps) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[len(a) - 1]))
    return
