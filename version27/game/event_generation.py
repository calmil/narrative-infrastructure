import random
import math
from termcolor import colored

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


# NEED A CHECK FOR VOWEL NAMES LOL

# Physical event (triggered by proximity)
def physical_event(obj_1, obj_2):
    obj_1_tag = colored(obj_1.title, color=None, on_color=obj_1.color_str)
    obj_2_tag = colored(obj_2.title, color=None, on_color=obj_2.color_str)

    phrase = ""

    if random.choice([True, False, False, False, False]):
        phrase += map_string(obj_1, 'outer_separation', phrase_beginnings)
        phrase += ', a '
    else:
        phrase += 'A '

    phrase += obj_1_tag
    if random.choice([True, False, False, False, False, False]):
        phrase += ' '
        phrase += map_string(obj_1, 'inner_separation', physical_interaction_adverbs)

    phrase += ' '
    phrase += map_string(obj_1, 'outer_separation', physical_interaction_verbs)
    phrase += ' a '
    phrase += obj_2_tag

    if random.choice([True, False, False, False]):
        phrase += ', '
        phrase += (random.choice(phrase_endings))
    phrase += '.'

    obj_1.history.append(phrase)
    print(phrase)

    # - - - - - - Response Phrase - - - - - -

    if random.choice([True, False, False]):
        response_phrase = ""

        if random.choice([True, False, False, False]):
            response_phrase += map_string(obj_1, 'inner_separation', response_beginnings).capitalize()

            if random.choice([True, False, False]):
                response_phrase += ' '
                response_phrase += random.choice(response_beginnings_addition)

            response_phrase += ', the '

        else:
            response_phrase += 'The '
        response_phrase += obj_2_tag

        if random.choice([True, False]):

            if random.choice([True, False]):
                response_phrase += ' '
                response_phrase += random.choice(physical_response_natures)

            response_phrase += (
                ' ' + random.choice(response_actions) +
                ' ' + random.choice(response_directions) + ' the '
                )
            response_phrase += obj_1_tag
            response_phrase += '.'

        else:

            response_phrase += ' '
            response_phrase += random.choice(response_thoughts)
            response_phrase += '.'

        print(response_phrase)


duration_natures = [
    'brief',
    'short-lived',
    'quick',
    'unintentional',
]

distance_natures = [
    'loving',
    'intimate',
    'tender',
    'sincere',
    'interpersonal',
    'close-knit',
    'professional',
    'impersonal',
    'terse',
    'distant',
    'unenthusiastic',
    'tepid',
]

# - - - - - - - - - - - - - - - - -

# Mapped
symbolic_interaction_adverbs = [
    'audibly',
    'weakly',
    'impishly',
    'slowly',
    'unenthusiastically',
    'unenthusiastically',
    'enthusiastically',
    'half-heartedly',
]

# Mapped
symbolic_interaction_verbs = [
    'winks at',
    'grins at',
    'grimaces at',
    'smiles at',
    'remembers',
    'thinks about',
    'suppresses the thought of',
    'comes to a conclusion about',
    'wants to see',
    'curses'
]

phrase_beginnings = [
    'From what you can tell',
    'To your surprise',
    'Beyond reasonable expectations',
    'Surprisingly',
    'To the surprise of many',
    'Though it\'s difficult to see',
    'Though it would later be forgotten',
    'As though it were inevitable',
]

# - - - - Physical Interaction - - - - - - - -
physical_interaction_adverbs = [
    'tenderly',
    'gently',
    'eagerly',
    'curiously',
    'weakly',
    'unenthusiastically',
    'furtively',
    'playfully',
    'slowly',
    'meditatively',
    'rapturously',
    'audibly',
    'impishly',
    'aggressively',
]

physical_interaction_verbs = [
    'feigns an attack on',
    'pursues',
    'signs toward',
    'pushes',
    'shoves',
    'pulls themselves toward',
    'asks to dance with',
    'extends a hand toward',
    'expresses contempt for',
    'expresses desire for',
    'guides',
    'tickles',
    'punches',
    'sidles up to',
    'nearly tramples',
    'kisses the hand of',
]

phrase_endings = [
    'for unknown reasons',
    'though unbeknownst to many',
    'for mysterious reasons',
    'driven by unknown motives',
    'with hypnotic grace',
    'with surprising speed',
    'with deliberate determination',
    'with great difficulty',
    'in childish rage',
    'in simple kindness',
    'though poetically',
    'though it seems like a mistake',
    'seemingly on accident',
    'in such a way as to seem fated',
    'as though following a script',
    'without a shred of irony',
    'without hesitation',
    'bravely',
    'fully knowing the consequences',
]

# - - - Response - - - - - - - - - - - - - - - -

# Mapped
response_beginnings = [
    'astonished',
    'terrified',
    'angered',
    'bothered',
    # NEUTRAL
    'unsettled',
    'with interest piqued',
    # POSITIVE
    'intrigued',
    'excited',
    'enraptured',
    ]

response_beginnings_addition = [
    'by this',
    'by the idea that this could happen',
    'at even the mere possibility',
    'by the implications',
    'at the chance',
]

physical_response_natures = [
    'immediately',
    'privately',
    'deliberately',
    ', with ease,',
    'automatically',
    'simply',
]

# Mapped
response_actions = [
    'howls',
    'screams',
    'hollers',
    'glares',
    'stares aggressively',
    'flares their nostrils',
    'nods',
    'breathes heavily',
    'lurches',
    'rolls over',
]

# glares [...] the
response_directions = [
    'back at',
    'at',
    'toward',
    'towards',
    'in response to',
    'due to the actions of',
    'as recourse for the actions of',
    'in the direction of',
    'directly at',
    'straight back at',
    'near',
    'in the general vicinity of',
]


# Mapped
response_thoughts = [
    'laments',
    'curses',
    'ignores this',
    'does not understand',
    'takes note',
    'hardly aknowledges',
    'understands',
    'sees no reason for this',
    'finds coping difficult',
    'is pleased',
    'is oddly pleased',
    'comes to terms with this',
]


