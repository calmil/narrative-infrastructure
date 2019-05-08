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

age_descriptors = [
    'The mood is',
    'Things seem',
    'The world is',
    'Again, it is',
    'The air is',
    'The world seems',
    'All things act according to a',
    'All things act in a',
    'The world is tuned to a',
    ]

age_descriptor_suffixes = [
    random.choice(['time','era','period','circumstance']),
    '',
    '',
    '',
    '',
    '',
    'nature',
    random.choice(['manner', 'pattern','choreography','dance','movement','order']),
    random.choice(['manner', 'pattern','choreography','dance','movement','order']),
    ]

ages = [
    ['chaotic','aggressive'],
    ['nascent',],
    ['spiteful',],
    ['harmonious',],
    ['peaceful',],
    ['soulful'],
    ]



# ------


narrations = [
    "",
    "Since time immemorial, they have had to wrest history into the light of legibility.",
    "What is it that renders our efforts illegible?",
    "I have thought about this for a long time.\n" + "I believe I know the answer.",
    "The enemy of legibility is" "The crushing pressure of the Earth's crust.",
    "The efforts were innate and unconscious, as it needed to be.",

    "The horror is when you realize that this is the only challenge left"
]