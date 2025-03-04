# ***WARNING*** this did not pass all of its tests

# expenditure is an array of numbers, d is the number of trailing days
def activity_notifications(expenditure, d):
    # notices is the number of notices that are sent if fraudulent activity is suspected
    notices = 0
    # iterate through expenditures
    # expenditure - 1 iterates through the indexes properly
    # expenditure - 1 - d iterates through and prevents indexing errors
    for x in range(len(expenditure) - d - 1):
        # this is the subarray containing the trailing days
        trailing = expenditure[x:x + d]
        trailing.sort()
        # this finds the median of the array
        # the first if statement checks for an even length
        if len(trailing) & 2 == 0:
            # this is the upper middle value e.g. [2, 4, 6, 8] would be 6
            upper = trailing[len(trailing)//2]
            # this is the lower middle value e.g. [2, 4, 6, 8] would be 4
            lower = trailing[len(trailing)//2 - 1]
            median = (upper + lower) / 2
        # the second if statement defaults for odd lengths
        else:
            median = trailing[len(trailing)//2]
        # if the expenditure following the trailing days exceeds the median * 2
        # a notice is sent out
        if median * 2 >= expenditure[d]:
            notices += 1
    return notices
