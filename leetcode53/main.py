class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -10000
        min_sum = 0
        s = 0
        for i, x in enumerate(nums):
            s += x
            ans = max(ans, s - min_sum)
            min_sum = min(min_sum, s)

        return ans