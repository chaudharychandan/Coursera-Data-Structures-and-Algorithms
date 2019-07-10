# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    res = 0; index = 0
    value_weight_tuple_list = sorted(zip(values, weights), key=lambda x: x[0] / x[1], reverse=True)
    while(capacity > 0 and index < len(value_weight_tuple_list)):
        value, weight = value_weight_tuple_list[index]
        if capacity >= weight:
            res += value; capacity -= weight
        else:
            res += (value / weight) * (capacity)
            capacity = 0
        index += 1

    return res

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
