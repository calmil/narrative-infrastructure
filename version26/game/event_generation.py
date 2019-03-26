import random
from termcolor import colored, cprint
# New event begins
            # Event is passed agent vals:
                # Titles
                # Natures
                # Speeds
                # Avg. Distance?
        # It is "evaluated"
            # How long?
            # Anyone else involved?
            # Natures are compared, and a "difference" is generated (based on diff in internal vals?)
            # How did it end?
        # Type is generated (from event_gen):
            # How strong/long?
            # What kind of a relationship? Formal? Militaristic? Diplomatic? Educational?
            # Will they be changed?
            # Was a "site" made?
            # How will this event be referenced in the future?

# NEED A CHECK FOR VOWEL NAMES LOL

# Physical event (triggered by proximity)

def physical_event(obj_1, obj_2):
    obj_1_tag = colored(obj_1.title, color=None, on_color=obj_1.color_str)
    obj_2_tag = colored(obj_2.title, color=None, on_color=obj_2.color_str)

    phrase = ""

    if random.choice([True, False]):
        phrase += (random.choice(phrase_beginnings) + ', a ')
    else:
        phrase += 'A '

    phrase += obj_1_tag
    if random.choice([True, False, False, False, False, False]):
        phrase += (" " + random.choice(physical_interaction_adverbs))
    phrase += ' ' +  random.choice(physical_interaction_verbs)
    phrase += ' a '
    phrase += obj_2_tag
    if random.choice([True, False, False, False]):
        phrase += (", " + random.choice(phrase_endings))

    print(phrase)

    # Response Phrase
    if random.choice([True, False, False]):
        response_phrase = ""
    # Beginning check
        if random.choice([True, False, False, False]):
            response_phrase += (random.choice(response_beginnings)).capitalize()
            if random.choice([True, False, False]):
                response_phrase += random.choice(response_beginnings_addition)
            response_phrase += ', the '
    # No beginning
        else:
            response_phrase += 'The '
        response_phrase += obj_2_tag
        if random.choice([True, False]):
    # Physical Reaction
            response_phrase += (
                ' ' + random.choice(response_actions) +
                ' ' + random.choice(response_directions) + ' the '
                )
            response_phrase += obj_1_tag
        else:
    # Thought
            response_phrase += ' ' + random.choice(response_thoughts)

        print(response_phrase)



duration_natures =[
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

# - - - - Physical Interaction - - - - - - - -

physical_interaction_adverbs = [
    'playfully',
    'gently',
    'eagerly',
    'aggressively',
    'curiously',
    'meditatively',
    'rapturously',
    'tenderly',
    ', without thought,',
    ', considerately,',
    'unenthusiastically',
    'audibly',
    'weakly',
    'impishly',
    'slowly',
]

physical_interaction_verbs = [
    'pushes',
    'shoves',
    'pulls',
    'guides',
    'tickles',
    'punches',
    'sidles up to',
    'kisses',
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

# reaction_verbs = [
#     'surprises',
#     'upsets',
#     'pleases',
#     'distracts',
#     'serves as punishment for',
# ]

phrase_beginnings = [
    'It seems',
    'From what you can tell',
    'To your surprise',
    'Beyond reasonable expectations',
    'Surprisingly',
    'To the surprise of many',
    'To no one\'s surprise',
    'Sadly',
]

phrase_endings = [
    'for unknown reasons',
    'due to unforseen circumstances',
    'though unbeknownst to many',
    'for furtive reasons',
    'through sheer circumstance',
    'driven by unknown motives',
    'bringing closure',
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
    'interested',
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

# Mapped
response_actions = [
    'howls',
    'screams',
    'hollers',
    'glares',
    'stares aggressively',
    'flares their nostrils',
    'simply nods',
    'breathes heavily',
]

response_directions = [
    'at',
    'toward',
    'towards',
    'in the direction of',
    'directly at',
    'near',
    'because of'
]

# Mapped
response_thoughts = [
    'laments',
    'curses',
    'ignores',
    'does not understand',
    'takes note',
    'aknowledges',
    'understands',
    'comes to terms',
]


physical_response_endings = [
    'immediately',
    'privately',
    'deliberately',
    'with ease',
    'automatically',
]