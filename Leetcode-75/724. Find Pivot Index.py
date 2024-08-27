class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for i in nums:
            total += i
        leftsum = 0
        for i in range(len(nums)):
            if (total - nums[i]) == leftsum:
                return i
            else:
                total-=nums[i]
                leftsum+=nums[i]
        return -1