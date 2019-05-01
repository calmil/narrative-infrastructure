import datetime

console_width = 60

x = [
     "> Since time immemorial, they have had to wrest history into the light of legibility.",
     "> From the beginning, they fought - unkowingly - against the greatest threat life could face: illegibility."
]

def intro():
    '''Commemorate a time-specific cycle'''

    date = datetime.datetime.now()

    print(
               ("-" * console_width) + '\n'
               + "We gather here as witness to the matter cycle of " + str(date) + "." + '\n'
               + "May it bear meaning, joy, or humor. " + '\n'
               + "God willing. " + '\n'
               + ("-" * console_width)
        )

# def ():

def counter(duration):
     print(
               ("-" * console_width) + '\n'
               + 'Cycle ' + str(int(duration/100)) + ' begins.' + '\n'
               + ("-" * console_width)
          )