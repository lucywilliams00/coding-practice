# a is an array, d is the number of times to shift the elements to the left
def rotate_left(a, d):
    # this takes all of the elements up to the index d and puts them in a list
    shift = a[:d]
    # this takes all of the elements after the index d and puts them in a list
    keep = a[d:]
    # this concatenates two lists
    shifted = keep + shift
    # return the shifted array
    return shifted
