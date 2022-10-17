def print_header(*msg):
    '''Returns the string of the header.'''
    help(print_header)
    print(msg)
    print(msg)
print(print_header("This is a header."))


def find_min(a,b):
    '''Finds the minimum between two values'''
    if (a > b):
        min = b
    else:
        min = a
    return min
print(find_min(7,2))


cube = lambda a : a ** 3
print(cube(7))