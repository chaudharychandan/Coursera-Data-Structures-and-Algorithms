# Uses python3
import sys

def optimal_summands(n):
    num = 1
    summands = []
    while n > 2 * num:
        summands.append(num)
        n -= num
        num += 1

    if n > 0: summands.append(n)

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
