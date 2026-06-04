# 53.最大子数组和

## 题目
[53.最大子数组和](https://leetcode.cn/problems/maximum-subarray/description/?envType=study-plan-v2&envId=top-100-liked)

## 思路
1. 一看到题目就想到前缀和，记录完前缀和，再暴力循环就可以求出最大值，但是肯定会超时；
2. 要解决怎么缩减时间，在解析中看到一个分析，每次记录当前的最小值和最大值，用最大值前去最小值就是最终结果；
3. 需要注意的是要先求当前最大值，再求最小值。

## 代码
见main.py文件

## 复杂度
1. 时间: O(N)

## 延申
这道题了解到一个方法：**动态规划**

本题动态规划的解法：
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]

        dp[0] = nums[0]
        for i in range(1, size):
            if dp[i - 1] >= 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)
```

还有一种**贪心算法**的解法：
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        for num in nums:
            if current_sum <0:
                current_sum = num
            else:
                current_sum+=num
            if current_sum>max_sum:
                max_sum = current_sum
        return max_sum
```