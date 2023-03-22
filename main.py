import random


def counter(n: int) -> int:
    return sum(range(n+1))


def mult(n: int) -> int:
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


def generator(n: int) -> int:
    if n < 0:
        return 0
    return random.randint(0, n)


if __name__ == "__main__":
    print(generator(5))
