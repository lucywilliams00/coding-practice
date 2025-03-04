# ***WARNING*** this did not pass all of its tests

# s1 and s2 are two strings
def twoStrings(s1, s2):
    # gets the length of s1
    length1 = len(s1)
    # iterates through the different substrings possible
    # for example: if s1 was elephant
    # you would have e, el, ele, elep, eleph, elepha, elephan and elephant
    # you would also have l, le, lep... etc.
    for x in range(length1 - 1):
        for y in range(length1 - 1):
            # y - x must be greater than 0
            # a substring can not have length 0
            # and all values before x have been tested
            if y - x > 0:
                # this gets the substring between x and y
                substring = s1[x: y]
                # if the second string s2 contains the substring, return "YES"
                if substring in s2:
                    return "YES"

    return "NO"