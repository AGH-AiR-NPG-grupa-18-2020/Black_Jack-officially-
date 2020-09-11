#!/usr/bin/python
# -*- coding: utf-8 -*-

#
#   W TYM PLIKU ZAPISANE SĄ WSZYSTKIE PODSTAWOWE WARTOŚCI
#


DEFAULT_DECK_NA = [('3', 3, 'kier'), ('3', 3, 'kier'), ('7', 7, 'pik'),  ('Ace', 0, 'pik'),('Ace', 0, 'pik'),('Ace', 0, 'pik'),('Ace', 0, 'pik'),('Ace', 0, 'pik'),('Ace', 0, 'pik'),
                   ('3', 3, 'kier'), ('3', 3, 'kier'),  ('Ace', 0, 'pik'),
                   ('3', 3, 'kier'), ('5', 5, 'karo'), ('7', 7, 'pik'),
                   ('3', 3, 'kier'), ('3', 3, 'kier'), ('7', 7, 'pik'),   ('Ace', 0, 'pik'),
                   ('3', 3, 'kier'), ('3', 3, 'kier'),   ('Ace', 0, 'pik'),
                   ('3', 3, 'kier'), ('5', 5, 'karo'), ('7', 7, 'pik'),
                   ('3', 3, 'kier'), ('3', 3, 'kier'), ('7', 7, 'pik'),   ('Ace', 0, 'pik'),
                   ('3', 3, 'kier'), ('3', 3, 'kier'),   ('Ace', 0, 'pik'),
                   ('3', 3, 'kier'), ('5', 5, 'karo'), ('7', 7, 'pik'),
                   ('Ace', 0, 'pik'),
                   ]


DEFAULT_TESTS = [('Ace', 0, 'pik'),('Ace', 0, 'pik'),('Ace', 0, 'pik'),('Ace', 0, 'pik'),
                 ('Ace', 0, 'pik'),('Ace', 0, 'pik'),('Ace', 0, 'pik'),('Ace', 0, 'pik'),
                 ('Ace', 0, 'pik'),('Ace', 0, 'pik'),('Ace', 0, 'pik'),('Ace', 0, 'pik')]


DEFAULT_DECK = [('Ace', 0, 'karo'), ('2', 2, 'karo'), ('3', 3, 'karo'), ('4', 4, 'karo'),
                   ('5', 5, 'karo'), ('6', 6, 'karo'), ('7', 7, 'karo'), ('8', 8, 'karo'),
                   ('9', 9, 'karo'), ('10', 10, 'karo'), #('Jack', 10, 'karo'),
                   ('Queen', 10, 'karo'), ('King', 10, 'karo'), ('Ace', 0, 'pik'),
                   ('2', 2, 'pik'), ('3', 3, 'pik'), ('4', 4, 'pik'), ('5', 5, 'pik'),
                   ('6', 6, 'pik'), ('7', 7, 'pik'), ('8', 8, 'pik'), ('9', 9, 'pik'),
                   ('10', 10, 'pik'), #('Jack', 10, 'pik'),
                ('Queen', 10, 'pik'), ('King', 10, 'pik'),
                   ('Ace', 0, 'trefl'), ('2', 2, 'trefl'), ('3', 3, 'trefl'), ('4', 4, 'trefl'),
                   ('5', 5, 'trefl'), ('6', 6, 'trefl'), ('7', 7, 'trefl'), ('8', 8, 'trefl'),
                   ('9', 9, 'trefl'), ('10', 10, 'trefl'), #('Jack', 10, 'trefl'),
                # ('Queen', 10, 'trefl'),
                   ('King', 10, 'trefl'), ('Ace', 0, 'kier'), ('2', 2, 'kier'), ('3', 3, 'kier'),
                   ('4', 4, 'kier'), ('5', 5, 'kier'), ('6', 6, 'kier'), ('7', 7, 'kier'),
                   ('8', 8, 'kier'), ('9', 9, 'kier'), ('10', 10, 'kier'), #('Jack', 10, 'kier'),
                   ('Queen', 10, 'kier'), ("King", 10, 'kier')]

DEFAULT_FLAGS = [{

    "hit": False,
    "DD": False,
    "split": False,
    "insurance": False,
    "stand": False,
    "blackJack": False

}]

DEFAULT_BET = [10]
NUM_PLAYERS = 2  # musi być mniejszy niż 8 bo tak
NUM_DECKS = 3
DEFAULT_SCORE = [0]
DEFAULT_CARDS = [[]]
DEFAULT_BUDGET = 200
BET_MIN = 5

