import datetime
import math
import random
from termcolor import colored

console_width = 110
console_indent = (" " * math.floor(console_width/8))


def speak(text, style):
    phrase = (("-" * console_width) + '\n')

    if style == 'title':
        bold_text = colored(text, color=None, on_color=None, attrs=['bold']) 
        left_margin = '>' + (' ' * math.floor((console_width - len(text))/2))
        right_margin = (' ' * (console_width - len(bold_text) - len(left_margin)) + (' ' * 7) + '<')
        phrase += (
            left_margin
            + bold_text
            + right_margin
            + '\n' )

    if style == 'body':
        split_text = text.split('\n')

        for i in range(len(split_text)):
            right_margin = ((' ' * (console_width - len(split_text[i]) - len(console_indent) - 2)) + '<')
            
            phrase += (
                '>' 
                + console_indent 
                + split_text[i]
                + right_margin
                + '\n'
            )
    
    phrase += ("-" * console_width)

    print(phrase)

def intro():
    '''Commemorate the beginning of a Spiral'''
    date = datetime.datetime.now()

    speak("We gather here as witness to the matter spiral of" + '\n'
        + str(date) + '\n'
        + "May it bear meaning, joy, or humor. God willing.", 'body')

def counter(cycle, age):
    speak('Period ' + str(cycle) + ' begins.', 'title')
    index = random.randint(0,len(age_descriptors)-1)
    speak(
        age_descriptors[index]
        + ' '
        + age
        + ' '
        + age_descriptor_suffixes[index]
        ,'body')

    # Somehow also must get what is fed back to affect the system?


# # After x cycles
x = """
Life is abundant.
    """


def summary(agents):
        type = "This spiral "


# 6 Ages

# A high: People more likely to align to others, searching for answers, coherent zeitgeist
# A low: People less likely to align to others, disagreeability incoherent zeitgeist

# C high: People all more likely to cohere to one another? Closer proximity, not agreeability? Working together
# C low: People less drawn to one another. Dishonesty? 

# S high: Tumultuous, scattered, narcissicm? 
# S low: People 

# age_descriptors = [
#     'The mood is',
#     'Things seem',
#     'The world is',
#     'Again, it is',
#     'The air is',
#     'The world seems',
#     'All things act according to a',
#     'All things act in a',
#     'The world is tuned to a',
#     ]

# age_descriptor_suffixes = [
#     random.choice(['time','era','period','circumstance']),
#     '',
#     '',
#     '',
#     '',
#     '',
#     'nature',
#     random.choice(['manner', 'pattern','choreography','dance','movement','order']),
#     random.choice(['manner', 'pattern','choreography','dance','movement','order']),
#     ]

# ages = [
#     ['chaotic','aggressive'],
#     ['nascent',],
#     ['spiteful',],
#     ['harmonious',],
#     ['peaceful',],
#     ['soulful'],
#     ]



# ------


narrations = [
    "",
    "[The stage is unlit, but you can discern bodies moving and talking in the darkness.]",
    "[A spotlight shines on a lone figure, unmoving, centered at the back of the stage.]",
    "[They speak.]",
    "Since time immemorial, we have had to wrest history into the light of legibility.",
    "It is through the our interpretation of the countless moving, speaking figures that surround us" + "\n"
        + "that we participate in this most divine of rituals.",
    "What is it that renders our efforts illegible?",
    "I have thought about this for a long time.\n" + "I will venture a few humble theories.",
    "The force of illegibility is found in\n" + "the crushing pressure of the Earth's crust.",
    "The force of illegibility is found in\n" + "the flattening rot that takes hold of dead, buried matter.",
    "The force of illegibility is found in\n" + "the geological calculations of the turbulent forces below.",
    "It works its way from the earth, into the bodies of vital agents,",
    "waiting patiently...",
    "It reclaims all that emerges, back into the inscrutable wastes of the abyss.",

    "The desire to articulate is a divine one.",
    "To articulate, to speak, even to simply produce a sound is a miracle.",
    "It is the most sacred defense against the crushing threat"
        +"\n" 
        + "of time,\n"
        + "of entropy,\n"
        + "and of death.",

    "To speak or act truthfully is to channel the essence of vitality.",
    "To speak or act truthfully is to protect all forms of life from illegibilty.",
    "To speak or act truthfully is to risk life," + '\n'
        + "so that the world to see a reflection of itself.",

    "While there is great esteem in fighting illegibility,"
        + "\n"
        + "it is dangerous, ugly work.",
    "Articulation risks showing life how ugly it can be.",
    "To render the world more legible risks bringing the hideous to light.",
    "When ugliness is understood as truthful, it does not disappear," + "\n"
        + "but transcends into a sympathetic component of grace.",

    "It may seem horrifying, but I wager that the clarification of true ugliness" + "\n"
        + "is the only intellectual pursuit we have left.",

    "The horror will pass.",

    "The horror will pass and the work will begin, for each of us, asynchronously.",

    "The work wil be innate and unconscious, as it needs to be...",
    "...as it needed to be...",
    "...as it was...",
    
    "",

    "",

    ""

]