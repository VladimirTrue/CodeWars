# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python
from collections import Counter as cnt


def find_it(seq):
    dct = cnt(seq)
    for dig, count in dct.items():
        if count % 2 != 0:
            return dig
