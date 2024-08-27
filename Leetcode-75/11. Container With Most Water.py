class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max = 0
        while (l != r):
            if height[l] > height[r]:
                curr = (r-l) * height[r]
                r -= 1
            else:
                curr = (r-l) * height[l]
                l += 1
            if curr > max:
                max = curr
        return max