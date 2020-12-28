import json
from unique import Unique
from print_result import print_result
from cm_timer import cm_timer_1
from random import randint
from gen_random import gen_random
from field import field
import re
import sys

path = 'data_light.json'


with open(path) as f:
    data = json.load(f)


@print_result
def f1(arg):
    return Unique(field(data, "job-name"), ignore_case=True)


@print_result
def f2(arg):
    return filter(lambda x: re.search(r'\bПрограммист\b', x) or
re.search(r'\bпрограммист\b', x), arg)


@print_result
def f3(arg):
    return list(map(lambda x: x+' с опытом Python', arg))


@print_result
def f4(arg):
    price = gen_random(len(arg), 100000, 200000)
    res = list(zip(arg, (list(map(lambda x: ', зарплата' + x + 'руб', ''.join(str(list(price)))[1:-1].split(','))))))
    return [''.join(i) for i in res]


def main():
    with cm_timer_1():

        f4(f3(f2(f1(data))))


if __name__ == '__main__':
    main()