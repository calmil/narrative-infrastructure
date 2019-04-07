import math


def cycle_list(list, index):
    """Cycles through a list and returns the other end"""
    if index != (len(list)-1):
        index += 1
        print('index now ', index)
    elif index == (len(list)-1):
        index = 0
        print('index now ', index)

    return index


def round_nearest(x, a):
    """Round to nearest whole number"""
    return round(round(x / a) * a, -int(math.floor(math.log10(a))))


def distance(point_1=(0, 0), point_2=(0, 0)):
    """Return the distance between two points"""
    return math.sqrt(
            (point_1[0] - point_2[0])**2 +
            (point_1[1] - point_2[1])**2)
