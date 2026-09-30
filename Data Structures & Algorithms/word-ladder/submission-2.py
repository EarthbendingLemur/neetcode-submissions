class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        q = deque()
        q.append((beginWord, 0))
        wordSet = set(wordList)
        print(wordSet)
        visited = set()
        visited.add(beginWord)
        while q:
            cur, level = q.popleft()
            if cur == endWord:
                return level + 1

            for i in range(len(cur)):
                for j in range(26):
                    temp1 = cur[:i] + chr((ord(cur[i]) - ord('a') + j) % 26 + ord('a')) + cur[i + 1:]
                    temp2 = cur[:i] + chr((ord(cur[i]) - ord('a') - j) % 26 + ord('a')) + cur[i + 1:]
                    if temp1 not in visited and temp1 in wordSet:
                        q.append((temp1, level + 1))
                        visited.add(temp1)
                    if temp2 not in visited and temp2 in wordSet:
                        q.append((temp2, level + 1))
                        visited.add(temp2)

        return 0