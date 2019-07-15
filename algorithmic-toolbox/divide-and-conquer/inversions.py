# Uses python3
import sys

def merge(a, b, left, mid, right):
    inversions = 0
    i, j, k = left, mid, left

    while i < mid and j <= right:
        if a[i] > a[j]:
            b[k] = a[j]
            j += 1
            inversions += mid - i
        else:
            b[k] = a[i]
            i += 1
        k += 1
    while i < mid:
        b[k] = a[i]
        i += 1
        k += 1
    while j <= right:
        b[k] = a[j]
        j += 1
        k += 1
    for i in range(left, right+1):
        a[i] = b[i]
    return inversions

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right <= left:
        return number_of_inversions
    ave = left + ((right - left) // 2)
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave+1, right)
    number_of_inversions += merge(a, b, left, ave+1, right)

    return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)-1))