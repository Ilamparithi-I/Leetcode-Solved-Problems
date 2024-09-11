class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            i = abs(i)
            # If the same index was visited twice, the num will be negative
            if nums[i] < 0:
                return i
            # mark visited as negative
            nums[i] = -nums[i]