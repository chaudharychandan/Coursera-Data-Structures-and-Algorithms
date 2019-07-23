#Uses python3
import sys
import math

def minimum_distance(x, y):
    x, y = zip(*sorted(zip(x, y)))
    return closest_pair_distance(x, y, 0, len(x)-1)

def closest_pair_distance(x, y, start, end):
    if end - start < 2:
        return distance((x[start], y[start]), (x[end], y[end]))
    mid = (start + end) // 2

    min_distance = min(closest_pair_distance(x, y, start, mid), closest_pair_distance(x, y, mid, end))

    strip = []
    left = mid - 1; right = mid + 1
    while left >= start and x[mid] - x[left] < min_distance:
        strip.append(left)
        left -= 1

    left = mid - 1; right = mid + 1
    while right <= end and x[right] - x[mid]  < min_distance:
        strip.append(right)
        right += 1

    strip = sorted(strip, key=lambda i: y[i])

    return closest_split_pair(x, y, strip, min_distance)

def closest_split_pair(x, y, points, min_distance):
    min_dis = min_distance
    for index, i in enumerate(points[:-1]):
        for j in range(1, min(len(points) - index, 7)):
            z = points[index + j]
            d = distance((x[i], y[i]), (x[z], y[z]))
            if d < min_dis:
                min_dis = d
    return min_dis

def distance(p1, p2):
    return math.sqrt(math.pow(p2[0] - p1[0], 2) + math.pow(p2[1] - p1[1], 2))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
