# this is a class
class Player:
    # this initialises any variables
    def __init__(self, name, score):
        self.name = name
        self.score = score
    # the repr function represents the classes objects as a string
    def __repr__(self):
        return self.name + " " + self.score
    # this function mimics the java comparator method to order scores in descending order
    # in ascending order:
    # a > b returns 1
    # a == b returns 0
    # a < b returns -1
    # therefore descending reverses these values
    def comparator(a, b):
        if a.score > b.score:
            return -1
        if a.score == b.score:
            arr = [a.name, b.name]
            arr.sort()
            if arr[0] == a.name:
                return -1
            else:
                return 1
        if a.score < b.score:
            return 1
