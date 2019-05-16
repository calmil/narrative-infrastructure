import random
import math
from termcolor import colored

# Inner Alignment: Strength of alignment to others.
# Inner Cohesion: Strength of allure toward others.
# Inner Separation: Strength of repulsion from others.
# Outer Alignment: Incentive for others to align with
# Outer Cohesion: Incentive to come towards
# Outer Separation: Incentive to be repelled


def round_nearest(x, a):
    return round(round(x / a) * a, -int(math.floor(math.log10(a))))


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


def vowel_check(string):
    if string[0] in {"a", "e", "i", "o", "u"}:
        return 'an'
    else:
        return 'a'


def physical_event(obj_1, obj_2):
    obj_1_tag = colored(obj_1.title, color=None, on_color=obj_1.color_str)
    obj_2_tag = colored(obj_2.title, color=None, on_color=obj_2.color_str)

    phrase = " "

    if random.choice([True, False, False, False, False, False, False]):
        phrase += (
                map_string(obj_1, phrase_beginnings)
                + ', '
                + vowel_check(obj_1.title)
            )
    else:
        phrase += vowel_check(obj_1.title).capitalize()

    phrase += ' ' + obj_1_tag

    if random.choice([True, False, False, False, False, False]):
        phrase += ' ' + map_string(obj_1, adverbs)

    phrase += (
            ' '
            + map_string(obj_1, physical_interaction_verbs)
            + ' '
            + vowel_check(obj_2.title)
            + ' '
            + obj_2_tag
        )

    # if random.choice([True, False, False, False, False, False, False]):
    #     phrase += ', ' + map_string(obj_1, phrase_endings)

    phrase += '.'

    # ------------ Response Phrase ------------
    if random.choice([True, False, False, False]):
        response_phrase = " "

        if random.choice([True, False, False, False]):
            response_phrase += map_string(
                    obj_1,
                    response_beginnings
                ).capitalize()

            if random.choice([True, False, False, False, False, False, False]):
                response_phrase += ' ' + map_string(
                        obj_2, 
                        response_beginnings_addition
                    )

            response_phrase += ', the '

        else:
            response_phrase += 'The '

        response_phrase += obj_2_tag

        if random.choice([True, False]):
        #     if random.choice([True, False]):
        #         response_phrase += ' ' + map_string(
        #                 obj_2, 
        #                 physical_response_natures
        #             )
            
        #     response_phrase += (
        #         ' ' + map_string(obj_2, response_actions) +
        #         ' ' + map_string(obj_2, response_directions) + ' the '
        #         )

        #     response_phrase += obj_1_tag + '.'

        # else:
            response_phrase += ' ' + map_string(obj_2, response_thoughts) + '.'

        return phrase + '\n' + response_phrase

    if random.choice([True, False, False, False]):
        phrase += '\n'
        phrase += " " + random.choice(post_commentary)

    return phrase


def symbolic_interaction(obj_1, obj_2):
    obj_1_tag = colored(obj_1.title, color=None, on_color=obj_1.color_str)
    obj_2_tag = colored(obj_2.title, color=None, on_color=obj_2.color_str)

    phrase = ' '

    phrase += (
            vowel_check(obj_1.title).capitalize()
            + ' '
            + obj_1_tag
            + ' '
            + map_string(obj_1, symbolic_interaction_verbs)
            + ' '
            + map_string(obj_1, symbolic_interaction_subjects)
            + ' of '
            )
    
    if random.choice([True, False]):
        phrase += (
                vowel_check(obj_2.title)
                + ' '
                + obj_2_tag
                )
    else:
        phrase += map_string(obj_1, symbolic_interaction_nouns)

    phrase += '.'

    print(phrase)


def retire(obj):
    print(
        (
            ' '
            + vowel_check(obj.title).capitalize()
            + ' '
            + colored(obj.title, color=None, on_color=obj.color_str) 
            + ' '
            + 'passes away.'
        )
    )


# ---------------------------------------------
# ------------- WORD LISTS --------------------
# ---------------------------------------------

# ------------- Misc Lists --------------------
objects = [
        'meaningless trinket',
        'powerful trinket',
        'foreign trinket',
        'child\'s blanket',
        'torn blanket',
        'old blanket',
        'ripped quilt',
        'broken bowl',
        'blanket',
        'ill-fitting suit and tie',
        'fragile mask',
        'profane mask',
        'innapropriate mask',
        'pocket knife',
        'bug suspended in amber',
        'scorpion suspended in amber',
        'spider suspended in amber',
        'pocket dictionary',
        'small atlas',
        'wooden figurine',
        'wet mop',
    ]

# ----------- Symbolic Interaction ------------
symbolic_interaction_verbs = [
        'ic',
        [
            'suppresses',
            'curses',
            'struggles with',
            'cannot cope with',
            'is haunted by',
            'mourns',
            'seeks relief from',
            'critiques',
            'mocks'
        ],
        [
            'thinks about',
            'recalls',
            'wonders about',
            'comes to a conclusion about',
            'ponders',
            'relives',
            'articulates a description of',
            'pantomimes the shape of',
            'observes',
            'misremembers',
        ],
        [
            'grows to understand',
            'is illuminated by',
            'is motivated by',
            'misses',
            'sees new meaning in',
            'relishes',
            'adores',
            'expresses fondness for',
            'desires',
            'ascribes meaning to',
            'finds inspiration in',
            'sees purpose in',
            'paints',
            'shares',
        ]
    ]

symbolic_interaction_subjects = [
        'random',
        [
            'the idea',
            'the memory',
            'the history',
            'what they remember',
            'a distant memory',
            'the appearance',
            'the movements',
            'the nature',
            'the writings',
            'the songs',
            'the music',
            'their love',
            'the attire',
            'the language',
            'the vaguest idea',
            'an image',
            'a memory',
            'what is known',
            'what is left'
        ]
    ]

symbolic_interaction_nouns = [
        'random',
        [
            'someone they cannot name',
            'a long-lost figure',
            'an apparent friend',
            'an unknowable figure',
            'someone unfamiliar',
            'something shrouded in great distance',
            'their neighbor',
            'the others',
            'a past friend',
            'a past enemy',
            'someone they love',
            'someone they loved',
            'someone important',
            'someone great',
            'a foreign body',
            'a lover',
        ]
    ]

# ------------- Physical Interaction ----------- 

phrase_beginnings = [
        'random',
        [
            'To the surprise of many',
            'As though it were inevitable',
            'Steeped in irony',
        ]
    ]

adverbs = [
        'random',
        [
            'absentmindedly',
            'accidentally',
            'actually',
            'adventurously',
            'almost',
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
            'briskly',
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
            'courageously',
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
            'generously',
            'gently',
            'gleefully',
            'gracefully',
            'gratefully',
            'greedily',
            'happily',
            'hastily',
            'helpfully',
            'helplessly',
            'honestly',
            'hopelessly',
            'hungrily',
            'immediately',
            'innocently',
            'inquisitively',
            'intensely',
            'intently',
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
            'loftily',
            'longingly',
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

physical_interaction_verbs = [
        'oc',
        [
            'ignores',
            'expresses contempt for',
            'nearly tramples',
            'pursues',
            'pushes',
            'pickpockets a meaningless trinket from',
            'punches',
            'shoves',
            'tickles',
            'wounds',
            'bruises',
            'itemizes the tresspasses of',
            'grabs a ' + random.choice(objects) + ' from',
            'grabs a ' + random.choice(objects) + ' from the hands of',
        ],
        [
            'signs toward',
            'passes by',
            'moves themselves toward',
            'guides',
            'says something unintelligible to',
            'asks a favor of',
            'shares a secret with',
            'enjoys a small pleasure with',
            'nods at',
            'tries to strike up a conversation with',
            'feigns interest in',
            'itemizes the tresspasses of',
        ],
        [
            'grows familiar with',
            'tries to hug',
            'compliments',
            'tries to entertain',
            'dances for',
            'prepares a meal for',
            'points out a ' + random.choice(objects) + ' to',
            'mumbles a blessing for',
            'fumbles for a complement for',
            'offers a small gift to',
            'expresses desire for',
            'asks to dance with',
            'extends a hand toward',
            'kisses the hand of',
            'offers a ' + random.choice(objects) + ' to',
            'shares a dream with',
            'offers a picture of a ' + random.choice(objects) + ' to',
            'mentions a ' + random.choice(objects) + ' to',
            'tries to reminisce with',
            'expresses a fondness for',
        ]
    ]

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

# ------------- Physical Interaction Resp. ----

response_beginnings = [
        'os',
        [
            'astonished',
            'terrified',
            'angered',
            'bothered',
            'enraged',
            'now corrupted',
        ],
        # NEUTRAL
        [
            'unsettled',
            'motivated',
            'with interest piqued',
            'appropriately',
            'uncertain',
            'with little self-confidence',
        ],
        # POSITIVE
        [
            'intrigued',
            'excited',
            'enraptured',
        ]
    ]

response_beginnings_addition = [
        'random',
        [
            'by this',
            'by the idea that this could happen',
            'at even the mere possibility',
            'by the implications',
            'at the chance',
            'because of this',
        ]
    ]

physical_response_natures = [
        'random',
        [
            'immediately',
            'privately',
            'deliberately',
            ', with ease,',
            'automatically',
            'simply',
            'plainly',
        ]
    ]

response_actions = [
        'is',
        [
            'rolls over',
            'smiles',
            'laughs',
            'extends a hand',
            'gives thanks'
        ],
        [
            'exhales',
            'glances',
            'stares',
            'disregards',
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

response_thoughts = [
        'is',
        [
            'comes to terms with this',
            'is pleased',
            'is oddly pleased',
            'enjoys a private laugh',
            'finds peace',
            'grows to understand',
        ],
        [
            'finds no reason to change', 
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
            'privately rages',
            'loses faith',
            'cannot stand it'
        ]
    ]

# ------------- Commentary --------------------

post_commentary = [
        "It is an accident.",
        "It would not have happened any other way.",
        "It is a generous act, in the grand scheme of things.",
        "All things considered, it is a miracle.",
        "It is not news to anyone.",
        "It is electryifying to see.",
        "It is meant to be a gesture of care.",
        "It is intended as a kindness.",
        "And then...",
        "But...",
        "And the cast continues...",
        "A new movement begins.",
        "The pattern seems more complete.",
        "It is important to remember this.",
        "There is a brief moment of struggle, before the connection is made.",
        "They are interlinked.",
        "It is commemorated on a " + random.choice(objects) + ".",
        "It is miraculous.",
        "No explanation is given.",
        "The others avert their gaze.",
        "It is unforgettable.",
        "They will be buried near one another.",
        "The odds of such an exchange were slim.",
        "[expressions of disgust sweep across an unseen crowd]",
        "[a crowd cheers]",
        "[a crowd demands more]",
        "[a bird chirps]",
        "[a baby begins to cry]",
        "[laughter]"

    ]
