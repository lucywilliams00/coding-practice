# create a function which returns the number of true values there are in an array
# e.g.
# countTrue([true, false, false, true, false]) --> 2
# countTrue([false, false, false, false]) --> 0
# countTrue([]) --> 0

# list = [True, False, False, True]
# count = 0

# for item in list:
#     if item == True:
#         count += 1

# print(count)

def count_true(lst):
    count = 0
    for item in lst:
        if item == True:
            count += 1
    return count

# when checking if this solution was correct, 
# originally return count was print(count)
# this failed the tests but was technically correct
# using print(count) allows you to see the answers in the console
# return count was required for the tests to pass