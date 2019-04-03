import math

reference_list = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '11',
    '12',
]

target_list = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
]

class Test_obj():

    def __init__(self):
        self.ia_index = 12
        self.ic_index = 8
        self.is_index = 2
        self.oa_index = 6
        self.oc_index = 4
        self.os_index = 6

egg = Test_obj()

def round_nearest(x, a):
    return round(round(x / a) * a, -int(math.floor(math.log10(a))))

def map_string(obj, quality, target_list):
    """Maps the relevant quality to a list of strings
       (whether verbs, adverbs, or adjectives), describing a situation."""

    nature_list_sizes = {'inner_alignment':12,
                       'inner_cohesion':14,
                       'inner_separation':12,
                       'outer_alignment':8,
                       'outer_cohesion':12,
                       'outer_separation':10}

    quality_index = {'inner_alignment':obj.ia_index,
                     'inner_cohesion':obj.ic_index,
                     'inner_separation':obj.is_index,
                     'outer_alignment':obj.oa_index,
                     'outer_cohesion':obj.oa_index,
                     'outer_separation':obj.oa_index}

    scalar = len(target_list)/nature_list_sizes[quality]

    mapped_index = math.floor(quality_index[quality] * scalar) - 1
    mapped_string = target_list[mapped_index]

    return mapped_string
