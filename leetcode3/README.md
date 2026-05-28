# 3.无重复字符的最长字串

## 题目
[3.无重复字符的最长字串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-100-liked)

## 思路
1. 看到这个题目，就想到又要查询已出现的元素，就想到要用哈希表，到那时一开始方向不对，想的是当出现重复时用目前最长的字符直接从第一个开始匹配，但是好像是解决不了；
2. 看了解析之后，知道一个新的名词叫**滑动窗口**，即维护一个窗口 [left, right]，保证窗口内无重复字符，并不断尝试扩大右边界:
- 用一个集合或字典记录窗口内的字符。
- 当右边界字符已经存在于窗口中时，移动左边界直到删除那个重复字符。
- 每一步更新最大长度。
3. 可以用字典记录每个字符最后出现的位置，当遇到重复字符s[right]时，left 可以直接跳转到 result[s[right]] + 1,同时更新字典。

## 代码
见mian.py文件

## 复杂度
时间：O(n)

## 有趣的一点
```python
def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    max_len = 0
    seen = set()
    for right in range(len(s)):
        # 如果 s[right] 已经在窗口内，移动左边界直到删除重复
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        # 加入当前字符
        seen.add(s[right])
        # 更新最大长度
        max_len = max(max_len, right - left + 1)
    return max_len
```
这里采用的while + set 实际上在leetcode运行时间要短于字典记录最后的位置，明明是循环里又有个循环，为什么时间会更短呢，
实际上无重复的字符串自身的长度相对于总长度可以忽略，使得时间几乎也是O(n)