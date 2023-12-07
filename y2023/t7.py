from collections import Counter
from functools import cmp_to_key

import utils as ut


def get_hand(val):
    set_len = len(set(val))
    if set_len == len(val):
        return 1
    if len(val) == set_len + 1:
        return 2
    cnt = Counter(val)
    cnt_val = sorted(cnt.values())
    if cnt_val == [1, 2, 2]:
        return 3
    if cnt_val == [1, 1, 3]:
        return 4
    if cnt_val == [2, 3]:
        return 5
    if cnt_val == [1, 4]:
        return 6
    if cnt_val == [5]:
        return 7

mapp = {
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}


def cmp_cards(val1, val2):
    for i in range(len(val1)):
        score1 = mapp.get(val1[i]) or int(val1[i])
        score2 = mapp.get(val2[i]) or int(val2[i])
        if score1 != score2:
            return score1 - score2

    return 0


def map_score(val1, val2):
    if val1[0] != val2[0]:
        return val1[0] - val2[0]
    return cmp_cards(val1[1], val2[1])


def task_1():
    file = ut.read()
    all_hands = []
    for line in file:
        cards, bid = line.split(' ')
        all_hands.append((get_hand(cards), cards, int(bid)))

    res = sorted(all_hands, key=cmp_to_key(map_score))
    return sum([(i+1) * r[2] for i, r in enumerate(res)])


mapp_v2 = {
    'J': 1,
    'T': 10,
    'Q': 12,
    'K': 13,
    'A': 14,
}


def get_hand_v2(val):
    cnt = Counter(val)
    if len(set(val)) == 1:
        return 7

    if 'J' in cnt:
        most = cnt.most_common(2)
        if most[0][0] != 'J':
            cnt[most[0][0]] += cnt['J']
        else:
            cnt[most[1][0]] += cnt['J']
        del cnt['J']

    cnt_val = sorted(cnt.values())
    if cnt_val == [1, 1, 1, 1, 1]:
        return 1
    if cnt_val == [1, 1, 1, 2]:
        return 2
    if cnt_val == [1, 2, 2]:
        return 3
    if cnt_val == [1, 1, 3]:
        return 4
    if cnt_val == [2, 3]:
        return 5
    if cnt_val == [1, 4]:
        return 6
    if cnt_val == [5]:
        return 7


def cmp_cards_v2(val1, val2):
    for i in range(len(val1)):
        score1 = mapp_v2.get(val1[i]) or int(val1[i])
        score2 = mapp_v2.get(val2[i]) or int(val2[i])
        if score1 != score2:
            return score1 - score2

    return 0


def map_score_v2(val1, val2):
    if val1[0] != val2[0]:
        return val1[0] - val2[0]
    return cmp_cards_v2(val1[1], val2[1])


def task_2():
    file = ut.read()
    all_hands = []
    for line in file:
        cards, bid = line.split(' ')
        all_hands.append((get_hand_v2(cards), cards, int(bid)))

    res = sorted(all_hands, key=cmp_to_key(map_score_v2))
    return sum([(i + 1) * r[2] for i, r in enumerate(res)])
