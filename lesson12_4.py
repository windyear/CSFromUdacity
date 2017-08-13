# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    if not len(list_of_numbers):
        return 0
    max = 0
    for number in list_of_numbers:
        if number > max:
            max = number
    return max


print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

    
