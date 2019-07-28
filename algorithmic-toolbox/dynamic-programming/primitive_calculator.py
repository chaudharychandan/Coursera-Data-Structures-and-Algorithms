# Uses python3
import sys

def optimal_sequence(n):
    parent_list = [None] * (n + 1)
    min_operations = [0] + [None] * n

    for i in range(1, n + 1):
        prev = i - 1
        current_num_ops = min_operations[prev] + 1

        if i % 2 == 0:
            current_prev = i // 2
            num_ops = min_operations[current_prev] + 1
            if num_ops < current_num_ops:
                prev, current_num_ops = current_prev, num_ops

        if i % 3 == 0:
            current_prev = i // 3
            num_ops = min_operations[current_prev] + 1
            if num_ops < current_num_ops:
                prev, current_num_ops = current_prev, num_ops

        parent_list[i], min_operations[i] = prev, current_num_ops

    sequence = []
    i = n
    while i > 0:
        sequence.append(i)
        i = parent_list[i]
    sequence.reverse()

    return sequence

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
