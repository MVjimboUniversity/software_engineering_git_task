def counter(n: int) -> int:
    return sum(range(n+1))


def mult(n: int) -> int:
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


if __name__ == "__main__":
    print(mult(5))
