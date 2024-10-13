# Shmuel Amir 316392323
from tailrecurse import *
from math import inf, sqrt, floor
from functools import reduce
import time
import sys


# recursion
# 1
def one(n):
    if n == 0:
        return ()
    return one(n - 1) + (n,)


def one_tail(n):
    @tail_call_optimized
    def tail(n, acc):
        if n == 0:
            return acc
        return tail(n - 1, (n,) + acc)

    return tail(n, ())


print(one_tail(100))


# 2
def my_sum(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + my_sum(lst[1:])


def sum_tail(lst):
    @tail_call_optimized
    def tail(lst, acc):
        if len(lst) == 0:
            return acc
        return tail(lst[1:], acc + lst[0])

    return tail(lst, 0)


print(sum_tail(one(100)))


# 3
def lcm(n1, n2):
    t = n1 % n2
    if t == 0:
        return n1
    return n1 * lcm(n2, t) // t


def lcm_tail(n1, n2):
    @tail_call_optimized
    def tail(n1, n2, acc):
        t = n1 % n2
        if t == 0:
            return acc
        return tail(n2, t, n1 * acc // t)

    return tail(n1, n2, n2)


print(lcm_tail(6, 4))


# 4
# it's also the tail solution
def isPalindrome(n):
    if n == "":
        return True
    if n[0] != n[-1]:
        return False
    return isPalindrome(n[1:-1])


print(isPalindrome(str(123454321)))


# 5
def sortedzip(lst):
    if len(lst[0]) == 0:
        return []
    return [set(sorted(l)[0] for l in lst)] + sortedzip([sorted(l)[1:] for l in lst])


def sortedzip_tail(lst):
    @tail_call_optimized
    def tail(lst, acc):
        if len(lst[0]) == 0:
            return acc
        return tail(
            [sorted(l)[1:] for l in lst], acc + [set(sorted(l)[0] for l in lst)]
        )

    return tail(lst, [])


print(sortedzip_tail([[3, 1, 2], [5, 6, 4], ["a", "b", "c"]]))


# generators
# 1
# a
def get_big_lst(n):
    return [n for n in range(n)]


def gen_big_lst(n):
    return (n for n in range(n))


start = time.time()
arr = get_big_lst(10000)
middle = time.time()
g2 = gen_big_lst(10000)
end = time.time()
print("no lazy:", (middle - start) * 100, sys.getsizeof(arr), type(arr))
print("lazy:", (end - middle) * 100, sys.getsizeof(g2))

# b
start = time.time()
new_arr = [n for n in arr if n < 5000]
middle = time.time()
new_gen = (n for n in g2 if n < 5000)
end = time.time()
print("no lazy:", (middle - start) * 100, sys.getsizeof(arr), type(arr))
print("lazy:", (end - middle) * 100, sys.getsizeof(g2))


# 2
def is_prime(n, divisor=None):
    if n < 2:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor - 1)


def gen_primes():
    return (n for n in range(100) if is_prime(n))


g1 = gen_primes()
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))


# 3
def powers(n):
    return (lambda x: x**i for i in range(n))


def assembly(n):
    return reduce(lambda a, c: a * c, range(1, n + 1), 1)


def tailor(x, p):
    return x**p / assembly(p)


def tailor_gen(x, n=0, total=0):
    yield total + tailor(x, n)
    yield from tailor_gen(x, n + 1, total + tailor(x, n))


g = tailor_gen(2)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
