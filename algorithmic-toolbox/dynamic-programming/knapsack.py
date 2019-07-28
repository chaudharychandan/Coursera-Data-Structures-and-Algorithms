# Uses python3
import sys

def optimal_weight(W, w):

    res = [[0 for _ in range(W+1)] for _ in range(len(w)+1)]

    for i in range(1, len(res)):
        for j in range(1, len(res[i])):
            res[i][j] = res[i-1][j]
            if w[i-1] > j:
                continue
            x = res[i-1][j - w[i-1]] + w[i-1]
            if x > res[i][j]:
                res[i][j] = x

    return res[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
