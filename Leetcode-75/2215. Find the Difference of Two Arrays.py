class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        set1copy = set(nums1)
        for i in set1copy:
            if i in set2:
                set1.discard(i)
                set2.discard(i)
        return set1, set2
        