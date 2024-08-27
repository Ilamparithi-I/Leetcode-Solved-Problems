class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        k1 = k
        count = 0
        m = 0
        for i in range(len(nums)):
            print (i, k1, count, start)
            if(nums[i] == 0):
                if k1 != 0:
                    k1 -= 1
                    count += 1
                else:
                    if nums[start] == 0:
                        start += 1
                    else:
                        while nums[start] != 0:
                            start += 1
                            count -= 1
                        start += 1
            else:
                count+=1
            if count > m:
                m = count
        return m
