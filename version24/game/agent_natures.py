import random
import math


def round_nearest(x, a):
    return round(round(x / a) * a, -int(math.floor(math.log10(a))))

def get_nature():
    # weights and words that describe them.
    # how do these affect their neighbors?

    # are these how they affect? or are affected! !

    # same dir. as neighbors
    alignment_nature = [
        'passive',
        'agnostic',
        'listless',
        'uninspired',
        'questionable',
        'agreeable',
        'cooperative',
        'harmonious',
        'active',
        'obsessive',
        'dogmatic',
        'vehement',
        'fanatical',
    ]

    # drawn toward neighbors.
    cohesion_nature = [
        'uninterested',
        'lonesome',
        'solitary',
        'wandering',
        'easygoing',
        'amicable',
        'sociable',
        'social',
        'hospitable',
        'attentive',
        'convivial',
        'vigilant',
        'absorbed',
        'inescapable',
        'isolophobial',
    ]

    # repulsed
    separation_nature = [
        'patient',
        'monastic',
        'tolerant',
        'liberal',
        'unbiased',
        'dispassionate',
        'neutral',
        'distant',
        'disdainful',
        'impatient',
        'scornful',
        'isolated',
        'agoraphobic',
    ]

    a_index = random.randint(0, len(alignment_nature) - 1)
    c_index = random.randint(0, len(cohesion_nature) - 1)
    s_index = random.randint(0, len(separation_nature) - 1)

    a_weight = round_nearest(a_index / len(alignment_nature), 0.05) * 2
    c_weight = round_nearest(c_index / len(cohesion_nature), 0.05) * 2
    s_weight = round_nearest(s_index / len(separation_nature), 0.05) * 2

    nature = str(
                 alignment_nature[a_index] +
                 ", " +
                 cohesion_nature[c_index] +
                 ", & " +
                 separation_nature[s_index]
                )

    return nature, a_weight, c_weight, s_weight

    # take count of possible natures
    # get values equally scaled across a reasonable range, set for each
    # return a value normalized.


my_nature, a_val, c_val, s_val = get_nature()
print(my_nature, a_val, c_val, s_val)