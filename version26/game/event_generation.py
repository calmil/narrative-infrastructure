import random

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

duration_natures =[
    'brief',
    'short-lived',
    'quick',
    'unintentional',
    'ac'
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

physical_interaction_adverbs = [
    'playfully',
    'gently',
    'eagerly',
    'aggressively',
    'curiously',
    'tenderly'
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

symbolic_interaction_adverbs = [
    'audibly',
    'weakly',
    'impishly',
    'slowly',
    'unenthusiastically',
    'unenthusiastically',
    'enthusiastically',
    'bravely',
]

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

reaction_verbs = [
    'surprises',
    'upsets',
    'pleases',
    'distracts',
    'serves as punishment for',
]

phrase_beginnings = [
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


# NEED A CHECK FOR VOWEL NAMES LOL

# Physical event (triggered by proximity)

def event_gen(obj_1, obj_2):
    phrase = ""
    if random.choice([True, False]):
        phrase += (random.choice(phrase_beginnings))
        phrase += (", a ")
    else:
        phrase += ("A ")
    phrase += (obj_1.title)
    if random.choice([True, False]):
        phrase += (" " + random.choice(physical_interaction_adverbs))
    phrase += (" " +  random.choice(physical_interaction_verbs) + " a " + obj_2.title)

    print(phrase)
