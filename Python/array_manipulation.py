# ***WARNING*** this did not pass all of its tests

# n is the length of the array, queries is a 2d array in the following format:
# each query in queries is an array of length 3
# for example: {(4, 8, 100), (2, 6, 50)...}
# this function adds a number to the values in an array between two positions
# for example:
# the first query adds 100 to the values at position 4, 5, 6, 7 and 8
# the second query adds 50 to the values at position 2, 3, 4, 5 and 6
def manipulate_array(n, queries):
    # this initialises an array of size n with all 0s
    a = [0] * n
    # loop through the queries
    for x in range(len(queries)):
        # this is the position in a to start from
        start = queries[x][0]
        # this is the position in a to end at
        end = queries[x][1]
        # this is the value to add the the values between start and end
        value = queries[x][2]
        # loops through the values between and including start and end
        # remember however start and end are positions NOT INDICES
        for y in range(start - 1, end):
            a[y] = a[y] + value
    # set the largest number as the first index in a
    largest = a[0]
    # loop through a comparing the numbers to find the largest number
    for z in range(n - 1):
        if a[z + 1] > largest:
            largest = a[z + 1]
    # return the largest number in a
    return largest
