class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        count = 0
        m = 0
        flag = False
        for i in range(len(nums)):
            if nums[i] == 0:
                if flag:
                    while (nums[start] != 0):
                        start += 1
                        count -= 1
                    start += 1
                else:
                    flag = True
            else:
                count += 1
            if count > m:
                m = count
        if flag: 
            return m
        # If there is no zero in the array, then we can remove one element from the array
        else:
            return m-1