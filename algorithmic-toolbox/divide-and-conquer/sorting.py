# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    j = l
    m = r

    i = l
    while i <= m:
        if a[i] < x:
            a[i], a[j] = a[j], a[i]
            i += 1
            j += 1
        elif a[i] > x:
            a[i], a[m] = a[m], a[i]
            m -= 1
        else:
            i += 1
    return (j, m)

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
