class TrieNode:
    def __init__(self):
        self.children:Dict[str,TrieNode]={}
        self.isword=False
        self.isReplaced=False
class Solution:
    def  __init__(self):
        self.root=TrieNode()
        self.ans=""

    def insert(self,word: str)-> None:
        node: TrieNode=self.root
        for c in word:
            node=node.children.setdefault(c,TrieNode())
        node.isword=True

    def replace(self,prefix:str):
        node: TriNode=self.root
        for c in prefix:
            if c not in node.children:
                return
            node=node.children[c]
        node.isWord=True
        node.isReplaced=True
    def formAns(self,prefix:str):
        node:TrieNode=self.root
        tmp=""
        for c in prefix:
            if c in node.children:
                tmp=tmp+c
                node=node.children[c]
            if node.isReplaced:
                self.ans=self.ans+tmp+" "
                return
        self.ans=self.ans+tmp+" "
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        lst=list (sentence.split())
        for i in lst:
            self.insert(i)
        for i in dictionary:
            self.replace(i)
        for i in lst:
            self.formAns(i)
        return self.ans.strip()
