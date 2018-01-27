class TreeNode:
	def __init__(self, data, properties, color):
		self.data = data
		self.properties = properties
		self.color = color


if __name__ == '__main__':
		node = TreeNode(2, 3, ['r', 'b'])
		L = []
		L.append(node)

		print(L[0].color)

