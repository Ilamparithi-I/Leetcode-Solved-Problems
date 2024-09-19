class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowset = set(allowed)
        final = []
        count = len(words)
        for i in words:
            for s in i:
                if s not in allowset:
                    count -= 1
                    break
        return count
