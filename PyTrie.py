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
			print()
			self.traverse(root.map[k], k)

	def exists(self, word):
		cur = self
		for w in word:
			if w not in cur.map:
				return False
			cur = cur.map[w]
		return cur.is_leaf

	def starts_with(self, prefix):
		cur = self
		for p in prefix:
			if p not in cur.map:
				return False
			cur = cur.map[p]
		return True

t = Trie()

t.insert("hello")
t.insert("heck")

print("exists")
print("hello", t.exists("hello")) # True
print("heck", t.exists("heck")) # True
print("head", t.exists("head")) # False
print("hear", t.exists("hear")) # False

print("starts with")
print("hell", t.starts_with("hell")) # True
print("hec", t.starts_with("hec")) # True
print("head", t.starts_with("head")) # False
print("hear", t.starts_with("hear")) # False
