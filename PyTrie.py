from collections import defaultdict

class Trie(object):
	def __init__(self):
		self.map = defaultdict(Trie)
		self.is_leaf = False

	def insert(self, word):
		cur = self
		for w in word:
			if w not in cur.map:
				cur.map[w] = Trie()
			cur = cur.map[w]
		cur.is_leaf = True

	def traverse(self, root, parent=None):
		for k in root.map.keys():
			if parent:
				print("PARENT",parent)
			print("KEY",k)
			self.traverse(root.map[k], k)

t = Trie()

t.insert("hello")
t.insert("heck")

t.traverse(t)

print(t.map)
