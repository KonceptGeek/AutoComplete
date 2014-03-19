class Node:
	def __init__(self):
		self.nodeName = None
		self.childNodes = {}
		self.wordEnd = False
	
	def printNode(self):
		print "NodeName - " + self.nodeName
		for val in self.childNodes.values():
			self.printChildNode(val)

	def printChildNode(self, node):
		print "ChildNodeName - " + node.nodeName

class Trie:
	def __init__(self):
		self.nodes = {}

	def hasNode(self, chars):
		return chars in self.nodes

	def addNode(self, chars, prevChar):
		newNode = Node()
		newNode.nodeName = chars
		try:
			self.nodes[prevChar].childNodes[chars] = newNode
		except:
			pass
		self.nodes[chars] = newNode

	def makeFinal(self, chars):
		self.nodes[chars].wordEnd = True

	def getWords(self, word):
		wordList = set()
		try:
			node = self.nodes[word]
			if node.wordEnd:
				wordList.add(node.nodeName)
		except:
			return set()
		wordList.update(self.getWordList(node))
		return wordList

	def getWordList(self, node):
		results = set()
		for childNode in node.childNodes.values():
			if childNode.wordEnd:
				results.add(childNode.nodeName)
			results.update(self.getWordList(childNode))
		return results

	def printTrie(self):
		for key, val in self.nodes.items():
			val.printNode()

class AutoComplete:
	def __init__(self):
		self.trie = Trie()

	def insertWord(self, word):
		prevChars = ''
		for char in word:
			if not self.trie.hasNode(prevChars + char):
				self.trie.addNode(prevChars + char, prevChars)
			prevChars = prevChars + char
		self.trie.makeFinal(prevChars)

	def printTrie(self):
		self.trie.printTrie()

	def completeWord(self, word):
		wordList = self.trie.getWords(word)
		return sorted(wordList)

if __name__ == '__main__':
	ac = AutoComplete()
	with open('data.txt','r') as dataFile:
		for line in dataFile:
			line = line.strip('\n\r')
			ac.insertWord(line.lower())

	prefix = raw_input("Please type the prefix of a word:\n")
	wordList = ac.completeWord(prefix.lower())
	print
	print "Suggestions:"
	print '\n'.join([word.rstrip('\'\"-,.:;!?)(') for word in wordList])