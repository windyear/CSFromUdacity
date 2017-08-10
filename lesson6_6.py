# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(search_string, target_string):
    '''
    这里其实可以将next_index初始化为-1，如果一次都没发现就直接返回
    使过程更加简单
    '''
    first_index = search_string.find(target_string)
    if first_index == -1:
        return -1
    #last_index = first_index
    next_index = first_index
    while True:
        temp_index = search_string.find(target_string, next_index + 1)
        if temp_index == -1:
            break
        next_index = temp_index
    return next_index    





print find_last('aaaa', 'a')
#>>> 3

print find_last('aaaaa', 'aa')
#>>> 3

print find_last('aaaa', 'b')
#>>> -1

print find_last("111111111", "1")
#>>> 8

print find_last("222222222", "")
#>>> 9

print find_last("", "3")
#>>> -1

print find_last("", "")
#>>> 0




