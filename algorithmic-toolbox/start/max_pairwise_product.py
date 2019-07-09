# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
max = 0; second_max = 0

for i in range(0, n):
    if a[i] > max:
        second_max = max
        max = a[i]
    elif a[i] > second_max:
        second_max = a[i]

result = max * second_max

print(result)
