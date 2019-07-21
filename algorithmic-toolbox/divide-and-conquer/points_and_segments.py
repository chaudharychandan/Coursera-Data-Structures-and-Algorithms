# Uses python3
import sys, functools

def sort_points(p1, p2):
    if p1[0] < p2[0]:
        return -1
    elif p1[0] > p2[0]:
        return 1
    else:
        p1_label = p1[1]; p2_label = p2[1]
        return -1 if p1_label < p2_label else 1


def fast_count_segments(starts, ends, points):
    cnt = {}
    segment_num = 0

    points_list = [(p, 'l') for p in starts]
    points_list += [(p, 'p') for p in points]
    points_list += [(p, 'r') for p in ends]

    points_list = sorted(points_list, key=functools.cmp_to_key(sort_points))

    for p in points_list:
        if p[1] == 'l':
            segment_num += 1
        elif p[1] == 'r':
            segment_num -= 1
        else:
            cnt[p[0]] = segment_num

    return [cnt[p] for p in points]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
