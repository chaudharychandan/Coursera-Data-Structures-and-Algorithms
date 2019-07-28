# Uses python3
def edit_distance(s, t, memo = {}):
    if len(s) == 0: return len(t)
    if len(t) == 0: return len(s)

    if (len(s), len(t)) in memo:
        return memo[(len(s), len(t))]
    delta = 1 if s[-1] != t[-1] else 0

    diag = edit_distance(s[:-1], t[:-1], memo) + delta
    vert = edit_distance(s[:-1], t, memo) + 1
    horz = edit_distance(s, t[:-1], memo) + 1

    min_distance = min(diag, vert, horz)

    memo[(len(s), len(t))] = min_distance

    return min_distance

if __name__ == "__main__":
    print(edit_distance(input(), input()))
