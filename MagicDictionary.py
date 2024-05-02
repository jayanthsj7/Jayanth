class TrieNode:

    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.isWord = False
class MagicDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.res = []
    def addWord(self, word: str) -> None:
        node: TrieNode = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
        node.isWord = True

    def buildDict(self, dictionary: List[str]) -> None:
        for i in dictionary:
            self.addWord(i)

    def search(self, searchWord: str) -> bool:
        self.res = []
        self._dfs(searchWord, 0, self.root, [])
        return any(self.res)

    def _dfs(self, word, s, node, letters):
        if s == len(word):
            if(node.isWord):
                i = 0
                count = 0
                while i < len(word):
                    if word[i] != letters[i]:
                        count+=1
                    i+=1
                if count == 1:
                    self.res.append(True)
                    return
            self.res.append(False)
            return
        for letter, child in node.children.items():
            self._dfs(word, s+1, child, letters+[letter])
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
