import random


def royal_title():
    # [x]
    # [x] of [group]
    royal_titles = [
        'chief',
        'king',
        # 'caliph',
        # 'padishah',
        # 'sultan',
        # 'maharaja',
        # 'emir',
        # 'raja',
        # 'lala',
        'earl',
        'baron',
        'viscount',
        'prince',
        'crown prince',
        # 'high king',
        # 'emperor',
        # 'kaiser',
        # 'agustus',
        # 'tzar',
        # 'huangdi',
        # 'samrat',
        # 'sapa inka',
        # 'king of kings',
        # 'mansa',
        # 'phraroah',
        # 'rex',
        # 'omukama',
        'duke',
        # 'doge',
        'archduke',
        'vice duke',
        'duchess',
        'despot',
        # 'sheikh',
        # 'emir',
        # 'taoiseach',
        # 'tywysog',
        # 'dauphin',
        # 'infante',
        # 'elector',
        # 'landgrave',
        'count',
        'viscount',
        # 'primor',
        # 'baronet',
        # 'dominus',
        # 'vidame',
        'knight',
        # 'patrician',
        'nobile',
        'elder',
        'edler',
        # 'junker',
        'gentleman',
        # 'bibi',
        # 'imperator',
        # 'caesar', ''
    ]

    return royal_titles[(random.randint(0, len(royal_titles)-1))]


def academic_title():
    # [x] at [group]
    academic_titles = [
        'lecturer',
        'teaching assistant',
        'professor',
        'professor emeritus',
        'demonstrator',
        # 'dacent',
        # 'rektar',
        # 'prarektar',
        # 'hoogleraar',
        # 'docent',
        # 'aspirant',
        'rector',
        # 'decaan',
        # 'recteur',
        # 'dean',
        # 'ostadh motafaregh',
        # 'modarres',
        # 'emeriitprofessor',
        # 'student',
        # 'tutor',
        # 'hall monitor',
        # 'TA',
        # 'registrar',
        # 'administrative assistant',
        # 'jokyō',
        # 'kōshi',
        # 'kyōju',
        # 'meiyo kyōju',
    ]

    return academic_titles[(random.randint(0, len(academic_titles)-1))]


def religious_title():
    # [x] of/for [group]
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
        # 'mufti',
        # 'khatib',
        # 'hafiz',
        # 'qadi',
        # 'hieromonk',
        # 'marja',
        # 'murshid',
        # 'marabout',
        # 'dervish',
        # 'khalifatu i-masih',
        # 'cantor',
        # 'shochet',
        # 'mohel',
        # 'jathedar',
        # 'sacred king',
        # 'vicar',
        # 'advocatus',
        # 'antipope',
        # 'chorbishop',
        # 'crucifer',
        # 'exarch',
    ]

    return religious_titles[(random.randint(0, len(religious_titles)-1))]


def political_title():

    # [x] of [district/site]
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
        # 'conselheiro',
        # 'ministro',
        # 'consigliere',
        # 'secretario',
        # 'embajador',
        # 'apocrisiarius'
    ]

    return political_titles[(random.randint(0, len(political_titles)-1))]


def military_title():
    # [x] in
    military_titles = [
        # english
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
        # ancient greek
        # 'strategos',
        # 'polemarchos',
        # 'taxiarchos',
        # 'syntagmatarchis',
        # 'tagmatarches',
        # 'lokhagos',
        # 'hipparch',
        # 'tetrarch',
        # 'hoplite',
        # 'trierarch',
        # 'ilarchos',
        # Ancient Rome
        # 'praetor',
        # 'consul',
        # 'proconsul',
        # 'legate',
        # 'tribuni militum',
        # 'equestrian',
        # 'tribunus laticlavius',
        # 'praefectus castrorum',
        # 'centurio',
        # 'optio',
        # 'pilus prior',
        # 'pilus posterior',
        # 'princeps prior',
        # 'princeps posterior',
        # 'hastatus prior',
        # 'hastatus posterior',
        # # ancient persia
        # 'eran spahbod',
        # 'aspwargan salar',
        # 'tirbodh',
        # 'argbod',
        # ''
    ]
    return military_titles[(random.randint(0, len(military_titles)-1))]


def job_title():
    # [x] / [x] at [group]
    job_titles = [
        'director',
        'groundskeeper',
        'gravedigger',
        'night watchman',
        'security guard',
        'janitor',
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

    if key < 2:
        title += (title_rankings[random.randint(0, len(title_rankings) - 1)])
        title += " "

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
    # elif key == 6:
    #     title += (mythical_species())
    # elif key == 7:
    #     title += (humanoid_species())

    return title
