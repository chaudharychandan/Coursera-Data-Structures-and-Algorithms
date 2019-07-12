#Uses python3

import sys, functools


def largest_number(a):
    res = ""
    a = sorted(a, key=functools.cmp_to_key(compare))
    for x in a:
        res += x

    return res

def compare(x, y):
    xy = int(str(x) + str(y)); yx = int(str(y) + str(x))
    if xy > yx:
        return -1
    elif yx > xy:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
