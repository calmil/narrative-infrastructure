import random
import math

# Strength of alignment to others. (12)
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

# Strength of allure toward others. (14)
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

# Strength of repulsion from others. (12)
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

# Incentive for others to align with (8)
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

# Incentive to come towards (12)
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

# Incentive to be repelled (10)
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


def round_nearest(x, a):
    return round(round(x / a) * a, -int(math.floor(math.log10(a))))


def get_nature():
    # Inner Nature

    ia_index = random.randint(0, len(inner_alignment_nature) - 1)
    ic_index = random.randint(0, len(inner_cohesion_nature) - 1)
    is_index = random.randint(0, len(inner_separation_nature) - 1)

    # Outer Nature
    oa_index = random.randint(0, len(outer_alignment_nature) - 1)
    oc_index = random.randint(0, len(outer_cohesion_nature) - 1)
    os_index = random.randint(0, len(outer_separation_nature) - 1)

    natures = [inner_alignment_nature[ia_index],
               inner_cohesion_nature[ic_index],
               inner_separation_nature[is_index],
               outer_alignment_nature[oa_index],
               outer_cohesion_nature[oc_index],
               outer_separation_nature[os_index]]

    natures_str = str(
                 inner_alignment_nature[ia_index]
                 + ", "
                 + inner_cohesion_nature[ic_index]
                 + ", "
                 + inner_separation_nature[is_index]
                 + ", "
                 + outer_alignment_nature[oa_index]
                 + ", "
                 + outer_cohesion_nature[oc_index]
                 + ", & "
                 + outer_separation_nature[os_index]
                )

    return (
            natures,
            natures_str,
            ia_index,
            oa_index,
            ic_index,
            oc_index,
            is_index,
            os_index
           )


print(get_nature())
