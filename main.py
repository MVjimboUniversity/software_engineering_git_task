def counter(n: int) -> int:
    return sum(range(n+1))


def mult(n: int) -> int:
    res = [i for i in range(1,n+1)]
    return sum(res)


if __name__ == "__main__":
    print(mult(5))
