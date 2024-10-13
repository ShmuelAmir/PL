# Shmuel Amir - 316392323
import math
from functools import reduce


# !!!!!!!!!!!!!!!!!!!!!!!!! change to tuple whenever possible
# 1
def getPentaNum(n):
    return n * (3 * n - 1) / 2


def pentaNumRange(n1, n2):
    return list(map(getPentaNum, range(n1, n2 + 1)))


# 2
def sumDigit(n):
    return sum(map(int, str(n)))


# 3
# מילון גימטריה עברית
hebrew_gematria = {
    "א": 1,
    "ב": 2,
    "ג": 3,
    "ד": 4,
    "ה": 5,
    "ו": 6,
    "ז": 7,
    "ח": 8,
    "ט": 9,
    "י": 10,
    "כ": 20,
    "ל": 30,
    "מ": 40,
    "נ": 50,
    "ס": 60,
    "ע": 70,
    "פ": 80,
    "צ": 90,
    "ק": 100,
    "ר": 200,
    "ש": 300,
    "ת": 400,
}


def getGematria(word):
    return sum(map(lambda x: hebrew_gematria[x], word))


# 4
# a
def isPrime(n):
    if n < 2:
        return False
    return any(lambda i: n % i != 0, range(n, math.sqrt(n), -1))


# b
def twinPrimes(n):
    if isPrime(n + 2):
        return n + 2
    if isPrime(n - 2):
        return n - 2
    return False


# c
def twinPrimesRange(n):
    return reduce(
        lambda a, c: a + {c: twinPrimes(c)},
        filter(twinPrimes, filter(isPrime, range(n))),
        dict(),
    )


# 5
def add3dicts(d1, d2, d3):
    shared_keys_3 = lambda d1, d2, d3: d1.keys() & d2.keys() & d3.keys()
    shared_keys_2 = lambda d1, d2: d1.keys() & d2.keys()
    all_keys = lambda d1, d2, d3: d1.keys() | d2.keys() | d3.keys()

    def merge_key(key):
        if key in shared_keys_3(d1, d2, d3):
            return (key, (d1[key], d2[key], d3[key]))
        elif key in shared_keys_2(d1, d2):
            return (key, (d1[key], d2[key]))
        elif key in shared_keys_2(d1, d3):
            return (key, (d1[key], d3[key]))
        elif key in shared_keys_2(d2, d3):
            return (key, (d2[key], d3[key]))
        elif key in d1:
            return (key, d1[key])
        elif key in d2:
            return (key, d2[key])
        else:
            return (key, d3[key])

    return dict(map(merge_key, all_keys(d1, d2, d3))).items()


# 6
# a
multiplyBy2 = lambda n: n * 2
square = lambda n: n**2
opposite = lambda n: n * -1
operations = [multiplyBy2, square, opposite]


# b
def applyAll(lst, operations):
    return dict(map(lambda op: (op, map(op, lst)), operations))
