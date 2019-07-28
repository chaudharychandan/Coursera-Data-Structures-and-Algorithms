#Uses python3

import sys

def lcs3(a, b, c):
    lena = len(a); lenb = len(b); lenc = len(c)
    dp = [[[0 for _ in range(lenc+1)] for _ in range(lenb+1)] for _ in range(lena+1)]

    for i in range(lena+1):
        for j in range(lenb+1):
            for k in range(lenc+1):
                if i == 0 or j == 0 or k == 0:
                    dp[i][j][k] = 0
                else:
                    dp[i][j][k] = 1 + dp[i - 1][j - 1][k - 1] if a[i - 1] == b[j - 1] and b[j - 1] == c[k - 1] else max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp[-1][-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
