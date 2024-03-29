import random
import math
from termcolor import colored


def round_nearest(x, a):
    return round(round(x / a) * a, -int(math.floor(math.log10(a))))


# Make it so it picks a random string from a relevant list
# def map_string(obj, quality, target_list):
#     """Maps the relevant quality to a list of strings
#        (whether verbs, adverbs, or adjectives), describing a situation."""

#     nature_list_sizes = {
#         'inner_alignment': 12,
#         'inner_cohesion': 14,
#         'inner_separation': 12,
#         'outer_alignment': 8,
#         'outer_cohesion': 12,
#         'outer_separation': 10
#         }

#     quality_index = {
#         'inner_alignment': obj.ia_index,
#         'inner_cohesion': obj.ic_index,
#         'inner_separation': obj.is_index,
#         'outer_alignment': obj.oa_index,
#         'outer_cohesion': obj.oa_index,
#         'outer_separation': obj.oa_index
#         }

#     scalar = len(target_list)/nature_list_sizes[quality]
#     mapped_index = math.floor(quality_index[quality] * scalar) - 1
#     # if mapped_index > 1 or mapped_index < (len(target_list)-2):
#     #     mapped_index += random.choice([-1,1])
#     mapped_string = target_list[mapped_index]

#     return mapped_string


def map_string(obj, target_list):
    if target_list[0] == 'random':
        return random.choice(target_list[1])
    elif target_list[0] == 'oa':
        quality = obj.oa_weight
    elif target_list[0] == 'oc':
        quality = obj.oc_weight
    elif target_list[0] == 'os':
        quality = obj.os_weight
    elif target_list[0] == 'ia':
        quality = obj.ia_weight
    elif target_list[0] == 'ic':
        quality = obj.ic_weight
    elif target_list[0] == 'is':
        quality = obj.is_weight

    if quality >= 0 and quality <= 0.6:
        index = 1
    elif quality >= 0.7 and quality <= 1.3:
        index = 2
    elif quality >= 1.4:
        index = 3
    
    return random.choice(target_list[index])

# NEED A CHECK FOR VOWEL NAMES LOL
def vowel_check(obj):
    if obj.title[0] in {"a", "e", "i", "o", "u"}:
        return 'an'
    else:
        return 'a'


# Physical event (triggered by proximity)
def physical_event(obj_1, obj_2):
    obj_1_tag = colored(obj_1.title, color=None, on_color=obj_1.color_str)
    obj_2_tag = colored(obj_2.title, color=None, on_color=obj_2.color_str)

    phrase = ""

    if random.choice([True, False, False, False, False]):
        phrase += map_string(obj_1, phrase_beginnings)
        phrase += ', '
        phrase += vowel_check(obj_1)
    else:
        phrase += vowel_check(obj_1).capitalize()

    phrase += ' '
    phrase += obj_1_tag
    if random.choice([True, False, False, False, False, False]):
        phrase += ' '
        phrase += map_string(obj_1, physical_interaction_adverbs)

    phrase += ' '
    phrase += map_string(obj_1, physical_interaction_verbs)
    phrase += ' '
    phrase += vowel_check(obj_2)
    phrase += ' '
    phrase += obj_2_tag

    if random.choice([True, False, False, False]):
        phrase += ', '
        phrase += map_string(obj_1, phrase_endings)
    phrase += '.'



    # - - - - - - Response Phrase - - - - - -

    if random.choice([True, False, False]):
        response_phrase = ""

        if random.choice([True, False, False, False]):
            response_phrase += map_string(obj_1, response_beginnings).capitalize()

            if random.choice([True, False, False]):
                response_phrase += ' '
                response_phrase += map_string(obj_2, response_beginnings_addition)

            response_phrase += ', the '

        else:
            response_phrase += 'The '
        response_phrase += obj_2_tag

        if random.choice([True, False]):

            if random.choice([True, False]):
                response_phrase += ' '
                response_phrase += map_string(obj_2, physical_response_natures)

            response_phrase += (
                ' ' + map_string(obj_2, response_actions) +
                ' ' + map_string(obj_2, response_directions) + ' the '
                )   
            response_phrase += obj_1_tag
            response_phrase += '.'

        else:

            response_phrase += ' '
            response_phrase += map_string(obj_2, response_thoughts)
            response_phrase += '.'

        return phrase + '\n' + response_phrase

    return phrase

# Inner_Alignment: Strength of alignment to others.
# Inner_Cohesion: Strength of allure toward others.
# Inner_Separation: Strength of repulsion from others.
# Outer_Alignment: Incentive for others to align with
# Outer_Cohesion: Incentive to come towards
# Outer_Separation: Incentive to be repelled

# - - - - - - - - - - - - - - - - -

# Inner Alignment
symbolic_interaction_adverbs = [
    'ia',
    [
        'weakly',
        'unenthusiastically',
        'impishly',
    ],
    [
        'weakly',
        'unenthusiastically',
        'impishly',
    ],
    [
        'slowly',
        'agonizingly',
        'audibly',
        'enthusiastically',
        'half-heartedly',
    ]
]

# Inner Cohesion
symbolic_interaction_verbs = [
    'ic',
    [
        'suppresses the thought of',
        'curses'
    ],
    [
        'thinks about',
        'remembers',
        'comes to a conclusion about',
    ],
    [
        'wants to see',
    ]
]

# Random
phrase_beginnings = [
    'random',
    [
        'From what you can tell',
        'To your surprise',
        'Beyond reasonable expectations',
        'Surprisingly',
        'To the surprise of many',
        'Though it\'s difficult to see',
        'Though it would later be forgotten',
        'As though it were inevitable',
        'Steeped in irony,'
    ]
]

# - - - - Physical Interaction - - - - - - - -
physical_interaction_adverbs = [
        'random',
    [
        'abnormally',
        'absentmindedly',
        'accidentally',
        'actually',
        'adventurously',
        'afterwards',
        'almost',
        'always',
        'annually',
        'anxiously',
        'arrogantly',
        'awkwardly',
        'bashfully',
        'beautifully',
        'bitterly',
        'bleakly',
        'blindly',
        'blissfully',
        'boastfully',
        'boldly',
        'bravely',
        'briefly',
        'brightly',
        'briskly',
        'broadly',
        'busily',
        'calmly',
        'carefully',
        'carelessly',
        'cautiously',
        'cheerfully',
        'clearly',
        'cleverly',
        'closely',
        'coaxingly',
        'colorfully',
        'commonly',
        'continually',
        'coolly',
        'correctly',
        'courageously',
        'crossly',
        'cruelly',
        'curiously',
        'daintily',
        'dearly',
        'deceivingly',
        'defiantly',
        'deliberately',
        'delightfully',
        'diligently',
        'dimly',
        'doubtfully',
        'dreamily',
        'easily',
        'elegantly',
        'energetically',
        'enthusiastically',
        'equally',
        'especially',
        'eventually',
        'exactly',
        'excitedly',
        'extremely',
        'fairly',
        'faithfully',
        'ferociously',
        'fervently',
        'fiercely',
        'fondly',
        'foolishly',
        'frankly',
        'frantically',
        'freely',
        'frenetically',
        'frightfully',
        'fully',
        'furiously',
        'generally',
        'generously',
        'gently',
        'gladly',
        'gleefully',
        'gracefully',
        'gratefully',
        'greedily',
        'happily',
        'hastily',
        'helpfully',
        'helplessly',
        'highly',
        'honestly',
        'hopelessly',
        'hourly',
        'hungrily',
        'immediately',
        'innocently',
        'inquisitively',
        'instantly',
        'intensely',
        'intently',
        'interestingly',
        'inwardly',
        'irritably',
        'jaggedly',
        'jealously',
        'jovially',
        'joyfully',
        'joyously',
        'jubilantly',
        'judgmentally',
        'justly',
        'keenly',
        'kiddingly',
        'kindheartedly',
        'kindly',
        'knavishly',
        'knowingly',
        'knowledgeably',
        'lazily',
        'lightly',
        'likely',
        'limply',
        'loftily',
        'longingly',
        'loosely',
        'loudly',
        'lovingly',
        'loyally',
        'madly',
        'majestically',
        'meaningfully',
        'mechanically',
        'merrily',
        'mockingly',
        'mortally',
        'mysteriously',
        'naturally',
        'hopelessly',
        'hungrily',
        'immediately',
        'innocently',
        'inquisitively',
        'instantly',
        'intensely',
        'intently',
        'interestingly',
        'inwardly',
        'irritably',
        'jaggedly',
        'jealously',
        'jovially',
        'joyfully',
        'joyously',
        'jubilantly',
        'judgmentally',
        'justly',
        'keenly',
        'kiddingly',
        'kindheartedly',
        'kindly',
        'knavishly',
        'knowingly',
        'knowledgeably',
        'lazily',
        'less',
        'lightly',
        'likely',
        'limply',
        'lively',
        'loftily',
        'longingly',
        'loosely',
        'loudly',
        'lovingly',
        'loyally',
        'madly',
        'majestically',
        'meaningfully',
        'mechanically',
        'merrily',
        'miserably',
        'mockingly',
        'mortally',
        'mostly',
        'mysteriously',
        'naturally',
        'nearly',
        'neatly',
        'nervously',
        'nicely',
        'noisily',
        'obediently',
        'obnoxiously',
        'oddly',
        'offensively',
        'officially',
        'only',
        'openly',
        'optimistically',
        'overconfidently',
        'painfully',
        'partially',
        'patiently',
        'perfectly',
        'physically',
        'playfully',
        'politely',
        'poorly',
        'positively',
        'potentially',
        'powerfully',
        'promptly',
        'properly',
        'punctually',
        'quaintly',
        'queasily',
        'questionably',
        'quickly',
        'quietly',
        'quirkily',
        'quizzically',
        'rapidly',
        'rarely',
        'readily',
        'reassuringly',
        'recklessly',
        'regularly',
        'reluctantly',
        'repeatedly',
        'reproachfully',
        'restfully',
        'righteously',
        'rightfully',
        'rigidly',
        'roughly',
        'rudely',
        'safely',
        'scarcely',
        'scarily',
        'searchingly',
        'sedately',
        'seemingly',
        'seldom',
        'selfishly',
        'separately',
        'seriously',
        'shakily',
        'sharply',
        'sheepishly',
        'shrilly',
        'shyly',
        'silently',
        'sleepily',
        'slowly',
        'smoothly',
        'softly',
        'solemnly',
        'solidly',
        'speedily',
        'stealthily',
        'sternly',
        'strictly',
        'successfully',
        'suddenly',
        'supposedly',
        'surprisingly',
        'suspiciously',
        'sweetly',
        'swiftly',
        'sympathetically',
        'tenderly',
        'tensely',
        'terribly',
        'thankfully',
        'thoroughly',
        'thoughtfully',
        'tightly',
        'tremendously',
        'triumphantly',
        'truly',
        'truthfully',
        'rightfully',
        'scarcely',
        'searchingly',
        'sedately',
        'seemingly',
        'selfishly',
        'separately',
        'seriously',
        'sheepishly',
        'smoothly',
        'solemnly',
        'sometimes',
        'speedily',
        'stealthily',
        'successfully',
        'suddenly',
        'supposedly',
        'surprisingly',
        'suspiciously',
        'sympathetically',
        'tenderly',
        'thankfully',
        'thoroughly',
        'thoughtfully',
        'tomorrow',
        'tremendously',
        'triumphantly',
        'truthfully',
        'ultimately',
        'unabashedly',
        'unaccountably',
        'unbearably',
        'unethically',
        'unexpectedly',
        'unfortunately',
        'unimpressively',
        'unnaturally',
        'unnecessarily',
        'urgently',
        'usefully',
        'uselessly',
        'usually',
        'utterly',
        'vacantly',
        'vaguely',
        'vainly',
        'valiantly',
        'vastly',
        'verbally',
        'very',
        'viciously',
        'victoriously',
        'violently',
        'vivaciously',
        'voluntarily',
        'warmly',
        'weakly',
        'wearily',
        'wetly',
        'wholly',
        'wildly',
        'willfully',
        'wisely',
        'woefully',
        'wonderfully',
        'worriedly',
        'wrongly',
        'yawningly',
        'yearningly',
        'yesterday',
        'yieldingly',
        'youthfully',
        'zealously',
        'zestfully',
    ]
]

# Outer Cohesion
physical_interaction_verbs = [
    'oc',
    [
        'signs toward',
        'ignores',
        'expresses contempt for',
        'feigns an attack on',
        'nearly tramples',
        'pursues',
        'pushes',
        'punches',
        'shoves',
    ],
    [
        'passes by',
        'pulls themselves toward',
        'guides',
        'tickles',
        'sidles up to',
        'feigns interest in',
    ],
    [
        'expresses desire for',
        'asks to dance with',
        'extends a hand toward',
        'kisses the hand of',
    ]
]

# Random
phrase_endings = [
        'random',
    [
        'though unbeknownst to many',
        'for unknown reasons',
        'for mysterious reasons',
        'driven by unknown motives',
        'with hypnotic grace',
        'with surprising speed',
        'in simple kindness',
        'with deliberate determination',
        'with great difficulty',
        'though poetically',
        'though it seems like a mistake',
        'seemingly on accident',
        'in such a way as to seem fated',
        'fully knowing the consequences',
        'as though following a script',
        'without a shred of irony',
        'without hesitation',
        'bravely',
        'in childish rage',
    ]
]

# - - - Response - - - - - - - - - - - - - - - -

# Outer Separation
response_beginnings = [
        'os',
        [
            'astonished',
            'terrified',
            'angered',
            'bothered'
        ],
        # NEUTRAL
        [
            'unsettled',
            'with interest piqued'
        ],
        # POSITIVE
        [
            'intrigued',
            'excited',
            'enraptured',
        ]
    ]

# Random
response_beginnings_addition = [
        'random',
    [
        'by this',
        'by the idea that this could happen',
        'at even the mere possibility',
        'by the implications',
        'at the chance',
    ]
]

# Random
physical_response_natures = [
        'random',
    [
        'immediately',
        'privately',
        'deliberately',
        ', with ease,',
        'automatically',
        'simply'
    ]
]

# Inner Separation
response_actions = [
    'is',
    [
        'rolls over',
    ],
    [
        'nods',
        'breathes heavily',
    ],
    [
        'howls',
        'screams',
        'hollers',
        'glares',
        'rages',
        'stomps',
        'audibly complains',
        'lurches',
        'stares aggressively',
        'flares their nostrils',
    ]
]

# Random
response_directions = [
        'random',
    [
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
]

# Inner Separation
response_thoughts = [
    'is',
    [
        'comes to terms with this',
        'is pleased',
        'is oddly pleased',
    ],
    [
        'does not understand',
        'takes note',
        'hardly aknowledges',
        'ignores this',
        'understands',
        'sees no reason for this',
    ],
    [
        'laments',
        'finds coping difficult',
        'curses',
    ]

]

