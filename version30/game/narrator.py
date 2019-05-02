import datetime
import math
# from termcolor import colored

console_width = 80
console_indent = (" " * math.floor(console_width/5))

x = [
     "> Since time immemorial, they have had to wrest history into the light of legibility.",
     "> From the beginning, they fought - unkowingly - against the greatest threat life could face: illegibility."
]

def intro():
    '''Commemorate the beginning of a Spiral'''
    date = datetime.datetime.now()

    print(
                 ("-" * console_width) + '\n'
               + '>' + console_indent + "We gather here as witness to the matter spiral of " + str(date) + "." + '\n'
               + '>' + console_indent + "May it bear meaning, joy, or humor. " + '\n'
               + '>' + console_indent + "God willing. " + '\n'
               + ("-" * console_width)
        )


def counter(cycle):
    print(
               ("-" * console_width) + '\n'
               + '>' + console_indent + 'Period ' + str(cycle) + ' begins.' + '\n'
               + ("-" * console_width)
        )


# # After x cycles
# x = """
# Life is abundant.
#     """