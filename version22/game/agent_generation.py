import random
import math

# [x] of [group]
royal_titles = [
    'chief',
    'king',
    'caliph',
    'padishah',
    'sultan',
    'maharaja',
    'emir',
    'raja',
    'lala',
    'earl',
    'baron',
    'viscount',
    'prince',
    'crown prince',
    'high king',
    'emperor',
    'kaiser',
    'agustus',
    'tzar',
    'huangdi',
    'samrat',
    'sapa inka',
    'king of kings',
    'mansa',
    'phraroah',
    'rex',
    'omukama',
    'duke',
    'doge',
    'archduke',
    'vice duke',
    'duchess',
    'despot',
    'sheikh',
    'emir',
    'taoiseach',
    'tywysog',
    'dauphin',
    'infante',
    'elector',
    'landgrave',
    'count',
    'viscount',
    'primor',
    'baronet',
    'dominus',
    'vidame',
    'knight',
    'patrician',
    'nobile',
    'elder',
    'edler',
    'junker',
    'gentleman',
    'bibi',
    'imperator',
    'caesar',''
]

# [x] at [group]
academic_titles = [
    'lecturer',
    'teaching assistant',
    'professor',
    'professor emeritus',
    'demonstrator',
    'dacent',
    'rektar',
    'prarektar',
    'hoogleraar',
    'docent',
    'aspirant',
    'rector',
    'decaan',
    'recteur',
    'dean',
    'ostadh motafaregh',
    'modarres',
    'emeriitprofessor',
    'student',
    'tutor',
    'hall monitor',
    'TA',
    'registrar',
    'administrative assistant',
    'jokyō',
    'kōshi',
    'kyōju',
    'meiyo kyōju',
]

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
    'mufti',
    'khatib',
    'hafiz',
    'qadi',
    'hieromonk',
    'marja',
    'murshid',
    'marabout',
    'dervish',
    'khalifatu i-masih',
    'cantor',
    'shochet',
    'mohel',
    'jathedar',
    'sacred king',
    'vicar',
    'advocatus',
    'antipope',
    'chorbishop',
    'crucifer',
    'exarch',
]

# [x] of [district/site]
political_titles = [
    'ambassador',
    'prime minister',
    'president',
    'minister',
    'chargés d\'affaires',
    'envoy',
    'monarch',
    'papal nuncio',
    'counselor',
    'secretary',
    'attaché',
    'ambassador-at-large',
    'trade representative',
    'conselheiro',
    'ministro',
    'consigliere',
    'secretario',
    'embajador',
    'apocrisiarius'
]

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
    'gunner',
    'trooper',
    'airman',
    'warrant officer',
    'sergeant',
    'corporal',
    # ancient greek
    'strategos',
    'polemarchos',
    'taxiarchos',
    'syntagmatarchis',
    'tagmatarches',
    'lokhagos',
    'hipparch',
    'tetrarch',
    'hoplite',
    'trierarch',
    'ilarchos',
    # Ancient Rome
    'praetor',
    'consul',
    'proconsul',
    'legate',
    'tribuni militum',
    'equestrian',
    'tribunus laticlavius',
    'praefectus castrorum',
    'centurio',
    'optio',
    'pilus prior',
    'pilus posterior',
    'princeps prior',
    'princeps posterior',
    'hastatus prior',
    'hastatus posterior',
    # ancient persia
    'eran spahbod',
    'aspwargan salar',
    'tirbodh',
    'argbod',
    ''
]

# [x] / [x] at [group]
job_titles = [
    'director',
    'groundskeeper',
    'gravedigger',
    'night watchman',
    'security guard'
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
    ''
]

# [x]
mythical_species = [
    'familiar',
    'drude',
    'cambion',
    'spectra',
    'goblin',
    'hellhound',
    'kitsune',
    'hind',
    'qilin',
    'kelpie',
    'griffin',
    'black dog',
    'satyr',
    'manticore',
    'mermaid',
    'kishi',
    'drop bear',
    'bunyip',
    'baku',
    'satori',
    'yowie',
    'yeti',
    'cipactli',
    'sewer alligator',
    'wyvern',
    'basilisk',
    'gorgon',
    'homunculus',
    'tulpa',
    'shabti',
    'werewolf',
    'cyclops',
    'hydra',
    'valkyrie',
    'ghost',
    'banshee',
]

humanoid_species = [
    'incubus',
    'succubus',
    'angel',
    'demon',
    'witch',
    'god',
    'genie',
    'nymph',
    'dryad',
    'cherubim',
    'erelim',
    'chayot',
]


#-------------------

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

# - - - - -
objects = [
    'totem',
    'talisman',
    'boulder',
    'rumor'
]

def round_nearest(x, a):
    return round(round(x / a) * a, -int(math.floor(math.log10(a))))

def get_nature():
    # weights and words that describe them.
    # how do these affect their neighbors?

    # are these how they affect? or are affected! !

    # same dir. as neighbors
    alignment_nature = [
        'passive',
        'agnostic',
        'listless',
        'uninspired',
        'questionable',
        'agreeable',
        'cooperative',
        'harmonious',
        'active',
        'obsessive',
        'dogmatic',
        'vehement',
        'fanatical',
    ]

    # drawn toward neighbors.
    cohesion_nature = [
        'uninterested',
        'lonesome',
        'solitary',
        'wandering',
        'easygoing',
        'amicable',
        'sociable',
        'social',
        'hospitable',
        'attentive',
        'convivial',
        'vigilant',
        'absorbed',
        'inescapable',
        'isolophobial',
    ]

    # repulsed
    separation_nature = [
        'patient',
        'monastic',
        'tolerant',
        'liberal',
        'unbiased',
        'dispassionate',
        'neutral',
        'distant',
        'disdainful',
        'impatient',
        'scornful',
        'isolated',
        'agoraphobic',
    ]

    a_index = random.randint(0, len(alignment_nature) - 1)
    c_index = random.randint(0, len(cohesion_nature)-1)
    s_index = random.randint(0, len(separation_nature)-1)

    a_weight = round_nearest(a_index / len(alignment_nature), 0.05)
    c_weight = round_nearest(c_index / len(cohesion_nature), 0.05)
    s_weight = round_nearest(s_index / len(separation_nature), 0.05)

    nature = str(
                 alignment_nature[a_index] +
                 ", " +
                 cohesion_nature[c_index] +
                 ", & " +
                 separation_nature[s_index]
                )

    return nature, a_weight, c_weight, s_weight

    # take count of possible natures
    # get values equally scaled across a reasonable range, set for each
    # return a value normalized.


my_nature, a_val, c_val, s_val = get_nature()
print(my_nature, a_val, c_val, s_val)