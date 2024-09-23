'''
https://leetcode.com/problems/implement-trie-prefix-tree/
'''


class TrieNode:
    def __init__(self):
        self.children = {}  # 해시맵으로 자식 노드 관리
        self.is_end = False  # 해당 노드가 단어의 끝인지


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode()  # 자식 노드 추가

            cur_node = cur_node.children[char]  # 현재 가리키고 있는 노드 갱신
        cur_node.is_end = True

    def search(self, word: str) -> bool:
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]

        # for문이 종료되었다는 것은 마지막 단어까지 있다는 것(ex) word: abc, 저장된게: abcd)
        return cur_node.is_end

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for char in prefix:
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
