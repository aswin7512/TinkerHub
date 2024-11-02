from random import choice


def shuffle():
    dic = {}
    list = ["Monkey", "Sloath", "Lizard", "Snake", "Cocroach", "Frog", "Snail", "Leech"]

    for i in range(len(list)):
        r = choice(list)
        dic[i+1] = r
        list.remove(r)
    return dic


def element(n, dic):
    return dic[n]

