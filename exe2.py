# Shmuel Amir 316392323
import time
from functools import reduce
import datetime

# 1
func = lambda x: x / 2 + 2
l = list(map(func, range(10000)))

b = time.time()
print(sum(l))
print(time.time() - b)


def imptSum(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum


b = time.time()
print(imptSum(l))
print(time.time() - b)

print(reduce(lambda a, c: a + func(c), range(10000), 0))

# 2
lst = range(1, 10001)
odd = list(filter(lambda x: x % 2 != 0, lst))
even = list(filter(lambda x: x % 2 == 0, lst))

print(sum(map(lambda i: even[i] * even[i - 1], range(1, len(even)))))

s = list(map(lambda i: odd[i] + odd[i - 1], range(1, len(odd))))
print(
    sum(
        map(
            lambda i: (
                s[i - 1] / 2 + 2 + odd[i] if i + 1 != len(odd) - 1 else s[i] / 2 + 2
            ),
            range(1, len(odd)),
        )
    )
)


# 3
def jump(start_date, count, jump_amount):
    y, m, d = start_date.split("/")
    return list(
        map(
            lambda i: datetime.date(int(y), int(m), int(d))
            + datetime.timedelta(days=i * jump_amount),
            range(count),
        )
    )


print(jump("1996/09/05", 5, 2))


# 4
def power_function(p):
    return lambda x: x**p


def powers(n):
    return map(lambda i: power_function(i), range(n))


def assembly(n):
    return reduce(lambda a, c: a * c, range(1, n + 1), 1)


def tailor(x, p):
    return sum(map(lambda n: x**n / assembly(n), range(p)))


print(tailor(3, 40))


# 5
def task_manager(tasks):
    return {
        "add_task": lambda task, state="incomplete": {**tasks, task: state},
        "get_tasks": lambda: tasks,
        "complete_task": lambda task: {**tasks, task: "complete"},
    }


tm = task_manager({})
tm["add_task"]("Write email")
tm["add_task"]("Shopping", "in progress")
tm["add_task"]("Homework")

current_tasks = tm["get_tasks"]()
print(current_tasks)

tm["complete_task"]("Write email")

current_tasks = tm["get_tasks"]()
print(current_tasks)
