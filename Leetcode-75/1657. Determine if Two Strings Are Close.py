class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        leng = len(word1)
        if leng != len(word2):
            return False
        dict1 = {}
        dict2 = {}
        for i in range(leng):
            val1 = dict1.get(word1[i], 0) 
            val2 = dict2.get(word2[i], 0) 
            dict1[word1[i]] = val1 + 1
            dict2[word2[i]] = val2 + 1
        if len(dict1) != len(dict2):
            return False
        if set(dict1.keys()) != set(dict2.keys()):
            return False
        values1 = list(dict1.values())
        values2 = list(dict2.values())
        return sorted(values1) == sorted(values2)