# 56.合并区间

## 题目
[56.合并区间](https://leetcode.cn/problems/merge-intervals/?envType=study-plan-v2&envId=top-100-liked)

## 思路
1. 这道题感觉挺简单的，合并区间，无非就是比较当前区间的左边界和上一个区间的的右边界；
2. 知道了主要实现步骤，还有一个关键的就是要将原来的数组进行排序，这也好理解，因为区间肯定是要从小到大才方便排序。

## 代码
见main.py文件

## 复杂度
1. 时间：O(nlogn),即排序sort所需要的时间
2. 空间：O(logn)，也是排序所需要的