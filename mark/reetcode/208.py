from typing import List


class Trie:

    words: List[str]
    def __init__(self):
        self.insert(str)
        self.search(str)
        self.startsWith(str)

    def insert(self, word: str) -> None:
        Trie.words.append(word)

    def search(self, word: str) -> bool:

        if Trie.words in word:
         return True
        else:
            return False


    def startsWith(self, prefix: str) -> bool:

        for word in Trie.words:
            print(word)

        return False


