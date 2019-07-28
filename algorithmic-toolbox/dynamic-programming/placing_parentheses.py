# Uses python3

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinMax(i, j, ops, m, M):
    minimum = float('inf')
    maximum = -minimum

    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], ops[k])
        b = evalt(M[i][k], m[k+1][j], ops[k])
        c = evalt(m[i][k], M[k+1][j], ops[k])
        d = evalt(m[i][k], m[k+1][j], ops[k])

        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)

    return (minimum, maximum)

def get_maximum_value(dataset):
    ops = dataset[1:len(dataset):2]
    ds = dataset[0:len(dataset)+1:2]
    n = len(ds)

    m = [[int(ds[i]) if i == j else 0 for i in range(n)] for j in range(n)]
    M = list(map(lambda l: l[:], m))

    for i in range(1, n):
        for j in range(n-i):
            k = i + j
            m[j][k], M[j][k] = MinMax(j, k, ops, m, M)

    return M[0][n-1]

if __name__ == "__main__":
    print(get_maximum_value(input()))
