# a and b are strings
def make_anagram(a, b):
    s1 = []
    s2 = []
    # creates an array for each string
    for achar in a:
        s1.append(achar)
    for bchar in b:
        s2.append(bchar)
    matching = []
    # finds the characters that match
    # you can't remove the character from s1 because it won't be able to iterate
    # by removing the character in s2 you prevent duplicates being counted
    # breaking moves onto the next letter preventing duplicates
    for char1 in s1:
        for char2 in s2:
            if char1 == char2:
                matching.append(char1)
                s2.remove(char2)
                break
    # the deleted characters is equal to the length of a - the letters that matched
    # therefore leaving the letters that were deleted
    # plus the letters remaining in s2 because these will be deleted
    deletions = len(a) - len(matching) + len(s2)
    return deletions
