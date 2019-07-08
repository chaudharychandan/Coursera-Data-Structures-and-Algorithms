# Uses python3
import sys

def lcm(a, b):
    return (a * b) // gcd(a, b)

def gcd(a, b):
    current_gcd = 1

    dividend, divisor = (a, b) if a < b else (b, a)

    while dividend % divisor != 0:
        r = dividend % divisor
        dividend = divisor
        divisor = r

    current_gcd = divisor

    return current_gcd

if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    print(lcm(a, b))

