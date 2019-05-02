import random


def royal_title():
    royal_titles = [
        'chief',
        'king',
        'earl',
        'queen',
        'baron',
        'prince',
        'crown prince',
        'duke',
        'archduke',
        'vice duke',
        'princess',
        'duchess',
        'despot',
        'count',
        'viscount',
        'knight',
        'nobile',
        'elder',
        'gentleman',
    ]

    return royal_titles[(random.randint(0, len(royal_titles)-1))]


def academic_title():
    academic_titles = [
        'lecturer',
        'teaching assistant',
        'professor',
        'professor emeritus',
        'demonstrator',
    ]

    return academic_titles[(random.randint(0, len(academic_titles)-1))]


def religious_title():
    religious_titles = [
        'acolyte',
        'pope',
        'dalai lama',
        'saltigue',
        'father',
        'high priest',
        'cleric',
        'chaplain',
        'bishop',
        'deacon',
        'shaman',
        'oracle',
        'monk',
        'preistess',
        'archdeacon',
        'cardinal',
        'friar',
        'nun',
        'mullah',
        'rabbi',
        'scholar',
    ]

    return religious_titles[(random.randint(0, len(religious_titles)-1))]


def political_title():
    political_titles = [
        'ambassador',
        'prime minister',
        'president',
        'minister',
        'envoy',
        'monarch',
        'papal nuncio',
        'counselor',
        'secretary',
        'attaché',
        'ambassador-at-large',
        'trade representative',
    ]

    return political_titles[(random.randint(0, len(political_titles)-1))]


def military_title():
    military_titles = [
        'admiral',
        'commodore',
        'field marshal',
        'general',
        'colonel',
        'captain',
        'lieutenant',
        'major',
        'commandant',
        'squadron leader',
        'wing commander',
        'officer',
        'ensign',
        'midshipman',
        'lieutenant',
        'cadet'
        'seaman',
        'private',
        'trooper',
        'warrant officer',
        'sergeant',
        'corporal',
    ]
    return military_titles[(random.randint(0, len(military_titles)-1))]


def job_title():
    job_titles = [
        'director',
        'groundskeeper',
        'gravedigger',
        'night watchman',
        'security guard',
        'janitor',
        'postal worker',
        'intern',
        'composer',
        'architect',
        'engineer',
        'sculptor',
        'painter',
        'dancer',
        'choreographer',
        'creative director',
        'director',
        'violinist',
        'cellist',
        'bassist',
        'guitarist',
        'drummer',
        'organist',
        'pianist',
    ]

    return job_titles[(random.randint(0, len(job_titles)-1))]


# -------------------

# prefixes for jobs
title_rankings = [
    'assistant'
    'head',
    'senior',
    'high',
    'chief',
    'grand',
    'full-time',
    'associate',
    'adjunct',
    'former',
    'first',
    'executive',
    'secondary',
    'second',
    'third',
    'pimeiro'
]

title_prefixes = [
    'arch'
    'demi-'
]


def get_title():
    title = ""
    key = random.randint(0, 5)

    # Add title prefix
    # if random.choice([True, False, False, False, False]):
    #     title += (title_rankings[random.randint(0, len(title_rankings) - 1)])
    #     title += " "

    # Generate title
    if key == 0:
        title += (royal_title())
    elif key == 1:
        title += (academic_title())
    elif key == 2:
        title += (religious_title())
    elif key == 3:
        title += (political_title())
    elif key == 4:
        title += (military_title())
    elif key == 5:
        title += (job_title())

    return title
