def resample(data, ratio: float):
    result = []
    for i, x in enumerate(data):
        while len(result) * ratio <= i:
            result.append(x)
    return result


def resample_rational(data, a: int, b: int):
    result = []
    for i, x in enumerate(data):
        while len(result) * a <= i * b:
            result.append(x)
    return result


if __name__ == '__main__':
    r = 3.14159265
    N = 100
    li = list(range(N))

    sub_li = resample(li, r)
    print(len(sub_li))
    print(sub_li)

    sup_li = resample(li, 1 / r)
    print(len(sup_li))
    print(sup_li)

    rational_li = resample_rational(li, 5, 3)
    print(len(rational_li))
    print(rational_li)
