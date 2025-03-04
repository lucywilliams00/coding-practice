# create a function to check if a candidate is qualified in an imaginary interview of an imaginary startup
# the candidate should have completed all questions
# the maximum time given to complete the interview is 120 minutes
# the maximum time given for very easy questions is 5 minutes each
# the maximum time given for easy questions is 10 minutes each
# the maximum time given for medium questions is 15 minutes each
# the maximum time given for hard questions is 20 minutes each
# if all the above criteria is satisfied, return "qualified", else return "disqualified"
# the format of the list input is [very easy, very easy, easy, easy, medium, medium, hard, hard]
# the maximum time to complete the interview includes a buffer time of 20 minutes
# try to solve using only list methods

def interview(lst, tot):
    if len(lst) < 8:
        return 'disqualified'
    elif tot > 120:
        return 'disqualified'
    elif lst[0] > 5 or lst[1] > 5:
        return 'disqualified'
    elif lst[2] > 10 or lst[3] > 10:
        return 'disqualified'
    elif lst[4] > 15 or lst[5] > 15:
        return 'disqualified'
    elif lst[6] > 20 or lst[7] > 20:
        return 'disqualified'
    else:
        return 'qualified'