# 560.和为k的子数组

## 题目
[560.和为k的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/submissions/728698927/?envType=study-plan-v2&envId=top-100-liked)

## 思路
1. 一开始想着是滑动窗口，窗口里的数之和小于k，就扩展right，大于k就移动left，但是这个有个前提就是列表要是单调的，显然不符合题目要求；
2. 于是了解到**前缀和**，s[j]表示nums前j个数的和，其中s的长度是len(nums) + 1,s[0]=0；
3. 那么nums[i]-nums[j - 1]的和就是s[j] - s[i]的值，s[j] - s[i] = k可以转化成s[j] - k = s[i];
4. 枚举当前的前缀和s[j]，看看曾经有多少个前缀和等于s[j] - k （配对）。每当我们在左边找到一个值等于s[j] - k的前缀和，就找到了一个和为k的子数组;
5. 在遍历s[j]的同时，用一个哈希表cnt统计s[j]的个数。哈希表的 key 是s[j]，value 是值为s[j]的前缀和的个数。遍历到s[j]时，从哈希表中就可以找到有cns[s[j] - k]个 ，加入答案.

## 代码
见main.py

## 复杂度
1. 时间：O(N)
2. 空间：O(N)

## 延申
main.py里是遍历两次的方法，下面这种是遍历一次的方法：
```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cns = defaultdict(int)
        cns[0] = 1
        ans = s = 0

        for x in nums:
            s += x
            ans += cns[s -k]
            cns[s] += 1
        return ans
```
