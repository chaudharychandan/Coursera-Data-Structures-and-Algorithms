# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
	def read(self):
		self.n = int(sys.stdin.readline())
		self.parent = list(map(int, sys.stdin.readline().split()))

		self.nodes = []
		self.root = None

		self.nodes = [[] for i in range(self.n)]

		for child_index in range(self.n):
			parent_index = self.parent[child_index]
			if parent_index == -1:
				self.root = child_index
			else:
				self.nodes[parent_index] += [child_index]

	def compute_height(self):
		queue = []; height = 0
		queue.append(self.root)

		while True:
			node_count = len(queue)
			if node_count == 0:
				return height
			height += 1
			while node_count > 0:
				node = queue.pop(0)
				if self.nodes[node]:
					for x in self.nodes[node]:
						queue.append(x)
				node_count -= 1

def main():
	tree = TreeHeight()
	tree.read()
	print(tree.compute_height())

threading.Thread(target=main).start()
