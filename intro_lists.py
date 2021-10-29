def swap(list_one):
    """
    Function that swaps the first and last elements of the list, regardless of length
    :param list_one: a list of at least two elements
    :return: the same list with the first and last elements swapped
    """
    x = list_one[0]
    y = list_one[-1]
    list_one[-1] = x
    list_one[0] = y
    return list_one



def rotate_left(list_one):
    """
    Given a list of ints length 3, return a list with the elements "rotated left" so [1, 2, 3] yields [2, 3, 1].
    :param list_one: A list consisting of exactly three integers
    :return: a list where all the elements have been shifted 1 place to the left
    """
    I = list_one[0]
    c = list_one[1]
    u = list_one[2]
    list_one[2] = I
    list_one[1] = u
    list_one[0] = c
    return list_one


def max_end(list_one):
    """
    This function will find if the first or last element of an list is larger, then set all the elements
    of that list to that value.
    :param list_one: A list consisting of three elements - all integers
    :return: A list where all the elements are the larger of the first or last element of the original list
    """
    o = list_one[0]
    m = list_one[1]
    g = list_one[2]
    if o > g:
        list_one[0] = o
        list_one[1] = o
        list_one[2] = o
        return list_one
    else:
        list_one[0] = g
        list_one[1] = g
        list_one[2] = g
        return list_one
