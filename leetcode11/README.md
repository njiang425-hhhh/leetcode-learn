# 11.接最多水的容器

## 题目
[11.接最多水的容器](https://leetcode.cn/problems/container-with-most-water/?envType=study-plan-v2&envId=top-100-liked)

## 思路
1. 这是一个区间最值的问题，初步就是暴力的循环，但是这样的时间复杂度有O(n²)；
2. 暴力方法时间太大，注意到面积是由宽度和两端的最小高度两者一起决定的；
3. 由此定义双指针left初始为0，right初始为len(height) - 1；
4. 两指针的移动是由两个指针高度谁更矮决定的。

## 代码
见main.py文件

## 复杂度
1. 时间：O(N)
2. 空间：O(1)

## 延申
1. 提交后注意到用时最短的解法，其实本质上也是使用的双指针，只不过巧妙的剪枝了；
2. 之前就注意到面积是由宽度和高度决定的，但我们已经计算出来的面积比之后最大高度乘宽度还大时，就没必要比较了，应该在之后的区域里不可能还存在更大的面积了
3. 代码如下：
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        ans = 0
        maxH = max(height)
        while left < right:
            distance = (right - left)
            if ans > distance * maxH:
                break
            area = distance * min(height[left],height[right])
            ans = max(ans,area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
```
4. 其中
```python
if ans > distance * maxH:
   break
```
这段代码就是关键减少时间的部分