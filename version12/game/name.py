from random import randint
import time

left_chars = [
    # sym
    "<",">",
    "«","»",
    "(", ")",
    "⇇", "⇉",

    # non sym
    "-",
    "_",
    ".",
    "=",
    "!",
    " ",

    "¡",
    "˚",
    "˙",
]

right_chars = [
    # sym
    ">","<",
    "»","«",
    ")","(",
    "⇉","⇇",

    # non sym
    "-",
    "_",
    ".",
    "=",
    "!",
    " ",

    "¡",
    "˚",
    "˙",
]

mid_chars = [
    "O",
    "o",
    "|",
    "-",
    "T",
    "I",
    ":",
    "V",
    "*",
    "!",
    "~",
    "^",
    "§",
    "•",
    "°",
    "·",
    "¡",
    "+",
    "↔︎",
    "⏐",
    "⎯",
    "•",
    "✦",
    "△",
    "ȸ",
    "ȹ",
    "Ȣ",
    "ȣ",
    "º",
    "×",
    "±",
    "∓",
    "∔",
    "∴",
    "∷",
    "∵",
    "⋏",
    "⦁",
    "♦",
    "︎⚬",
    "⚲",
    "∞",
    "∫"
    # ℵ
]

def gen(name_length):
    name = []
    name_index = []

    # Generate Name_Index (string of numbered indexes of the chars)
    for char in range(0, name_length):
        name_index.append(randint(0, len(left_chars)-1))

    # Left Wing
    for i in range(0, len(name_index)):
        name.append(left_chars[name_index[i]])

    # Crown
    name.append(mid_chars[randint(0, len(mid_chars)-1)])

    # Right Wing
    name_index.reverse()
    for i in range(0, len(name_index)):
        name.append(right_chars[name_index[i]])

    return name