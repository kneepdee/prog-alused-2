from turtle import *
from random import *


def puu(pikkus):
    if pikkus < 5:
        forward(pikkus)
        back(pikkus)
    else:
        forward(pikkus)
        left(45)
        puu(randint(6, 7) / 10 * pikkus)
        right(90)
        puu(randint(6, 7) / 10 * pikkus)
        left(45)
        back(pikkus)
