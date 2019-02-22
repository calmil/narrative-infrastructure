import random
import math


def round_nearest(x, a):
    return round(round(x / a) * a, -int(math.floor(math.log10(a))))

def get_nature():
    # Inner Nature

    # Strength of alignment to others.
    inner_alignment_nature = [
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

    # Strength of allure toward others.
    inner_cohesion_nature = [
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

    # Strength of repulsion from others.
    inner_separation_nature = [
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

    ia_index = random.randint(0, len(inner_alignment_nature) - 1)
    ic_index = random.randint(0, len(inner_cohesion_nature) - 1)
    is_index = random.randint(0, len(inner_separation_nature) - 1)

    ia_weight = round_nearest(ia_index / len(inner_alignment_nature), 0.05) * 2
    ic_weight = round_nearest(ic_index / len(inner_cohesion_nature), 0.05) * 2
    is_weight = round_nearest(is_index / len(inner_separation_nature), 0.05) * 2

    # Outer Nature

    # Incentive for others to align with
    outer_alignment_nature = [
        'pessimistic',
        'unseen',
        'silent',
        'predictable',
        'uninspired',
        'unimaginative',
        'realistic',
        'optimistic',
        'utopian'
    ]

    # Incentive to come towards
    outer_cohesion_nature = [
        'drab',
        'boring',
        'pedestrian',
        'plain',
        'common',
        'ordinary',
        'nondescript',
        'intriguing',
        'attractive',
        'alluring',
        'cherubic',
        'beautiful',
        'resplendent',

    ]

    # Incentive to be repelled
    outer_separation_nature = [
        'amoral',
        'nescient',
        'dull',
        'honest',
        'spastic',
        'coarse',
        'uncouth',
        'vulgar',
        'repugnant',
        'vile',
        'repulsive',
    ]

    oa_index = random.randint(0, len(outer_alignment_nature) - 1)
    oc_index = random.randint(0, len(outer_cohesion_nature) - 1)
    os_index = random.randint(0, len(outer_separation_nature) - 1)

    oa_weight = round_nearest(oa_index / len(outer_alignment_nature), 0.05) * 2
    oc_weight = round_nearest(oc_index / len(outer_cohesion_nature), 0.05) * 2
    os_weight = round_nearest(os_index / len(outer_separation_nature), 0.05) * 2


    nature = str(
                 inner_alignment_nature[ia_index] +
                 ", " +
                 inner_cohesion_nature[ic_index] +
                 ", " +
                 inner_separation_nature[is_index] +
                 ", " +
                 outer_alignment_nature[oa_index] +
                 ", " +
                 outer_cohesion_nature[oc_index] +
                 ", & " +
                 outer_separation_nature[os_index]
                )

    return nature, ia_weight, oa_weight, ic_weight, oc_weight, is_weight, os_weight,


print(get_nature())