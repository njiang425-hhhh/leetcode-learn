# 438.找到字符串中所有异位字符词

## 题目
[438.找到字符串中所有异位字符词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/?envType=study-plan-v2&envId=top-100-liked)

## 思路
1. 这道题还是用滑动窗口去维护出现的字母，然后去匹配；
2. 最初我的想法是右窗口去移动，当 right - left + 1 = len(p)时再检查这个长度是否与目标相同，而判断是否相同的方法是两个去排序之后看是否相同，结果方法可行但是超时；
3. 然后就了解到一种方法就是用Counter去统计每个字母出现的次数，去匹配次数就可以判断是否为异位字符串了。

## 代码
见main.py文件

## 复杂度
时间:O(m + n), m 是 s 的长度，n 是 p 的长度

## 其他
1. 最开始想法的代码
```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        result = []

        if len(s) < len(p):
            return result
            
        for right in range(len(s)):
            if s[right] in p:
                if right - left == len(p) - 1: 
                    left += 1 
                    if sorted(s[left - 1: right + 1]) == sorted(p):
                        result.append(left - 1)
            else:
                left = right + 1
        return result
```
2. main.py文件里是去看固定长度的窗口，还了解到一个不定长窗口
```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(p)  # 统计 p 的每种字母的出现次数
        ans = []

        left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1  # 右端点字母进入窗口
            while cnt[c] < 0:  # 字母 c 太多了
                cnt[s[left]] += 1  # 左端点字母离开窗口
                left += 1
            if right - left + 1 == len(p):  # t 和 p 的每种字母的出现次数都相同（证明见上）
                ans.append(left)  # t 左端点下标加入答案

        return ans
```