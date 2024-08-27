class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for i in arr:
            val = dic.get(i, 0)
            dic[i] = val + 1
        set1 = set(dic.values())
        if len(set1) == len(dic):
            return True 
        return False