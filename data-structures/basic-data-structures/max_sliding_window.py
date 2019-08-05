# python3


def max_sliding_window_naive(sequence, m):
    queue = Queue()
    maximums = []

    return maximums


class Stack():
    def __init__(self):
        self.__stack = []
        self.max_stack = []

    def Push(self, a):
        if len(self.max_stack) > 0:
            if a > self.max_stack[-1]:
                self.max_stack.append(a)
            else:
                self.max_stack.append(self.max_stack[-1])
        else:
            self.max_stack.append(a)
        self.__stack.append(a)

    def Pop(self):
        self.max_stack.pop()
        return self.__stack.pop()

    def Max(self):
        return None if self.is_empty() else self.max_stack[-1]

    def is_empty(self):
        return True if len(self.__stack) == 0 else False

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(" ".join(map(str, max_sliding_window_naive(input_sequence, window_size))))
