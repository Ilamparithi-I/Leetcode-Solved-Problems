class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high = 0
        current = 0
        for i in gain:
            current += i
            if current > high:
                high = current
        return high
        