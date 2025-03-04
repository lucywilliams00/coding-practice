# s is a string
def alternating_characters(s):
    a = []
    # this copies s into an array a
    for char in s:
        a.append(char)
    x = 0
    y = 0
    # initialise alternating with the first letter of the string
    # even if a string is AAAA the alternating string will be A on its own
    alternating = [a[0]]
    # this iterates through each letter in the string
    # it checks each letter for duplicates
    # when it finds a different letter it adds it to the alternating array
    # e.g. AAABAB would add B to the array at index 3
    # then x becomes index 3
    while x < len(a):
        while y < len(a):
            if y - x > 0:
                if a[x] != a[y]:
                    alternating.append(a[y])
                    x = y
            y += 1
        x += 1
    # the number of deletions is the difference
    deletions = len(a) - len(alternating)
    return deletions
