# Uses python3
import sys, math

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    mid = (left + right) // 2
    half_element_count = (right - left) // 2

    left_maj = get_majority_element(a, left, mid)
    right_maj = get_majority_element(a, mid, right)

    left_maj_count = get_element_count(a, left, right, left_maj)
    if left_maj_count > half_element_count:
        return left_maj

    right_maj_count = get_element_count(a, left, right, right_maj)
    if right_maj_count > half_element_count:
        return right_maj

    return -1

def get_element_count(a, left, right, x):
    maj_count = 0
    for i in range(left, right):
        if a[i] == x:
            maj_count += 1
    return maj_count

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
