# 49.字母异位词分组

## 题目
[49.字母异位词分组](https://leetcode.cn/problems/group-anagrams/?envType=study-plan-v2&envId=top-100-liked)

## 思路
1. 这个也是要与已查看过的字符串进行对比，既然涉及到查看已查询过的单元，就要考虑哈希；
2. 哈希中有key和value，就要想到什么作为key，又什么作为value，显然要将排序好的字符串作为key，value就是与之相同的字符串；
3. 涉及排序就要又sorted(),而sort()是把字符串拆开排序好，所有又要有'分隔符'join(列表)来将其组合起来；
4. 最后就返回字典的value即可。

## 代码
见main.py文件

## 复杂度
1. 时间
- 平时可以看成为O(n)
- 但是严格意义上讲为O(N⋅klogk)，sorted(s) 对单个字符串排序：Python 底层 Timsort，复杂度 O(klogk)，在乘上遍历的O(n)，就可以得出。
2. 空间 O(N)

## 延申
1. 在提交之后看到一个时间复杂度为O(N)的解法，采用了质数乘法
- 将26个字母分别赋值为一个质数，只要两个字符串字母种类和数量完全一样，它们的乘积一定相同！
2. 代码实现
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = {
            'a':2,'b':3,'c':5,'d':7,'e':11,'f':13,'g':17,
            'h':19,'i':23,'j':29,'k':31,'l':37,'m':41,'n':43,
            'o':47,'p':53,'q':59,'r':61,'s':67,'t':71,
            'u':73,'v':79,'w':83,"x":89,'y':97,'z':101
            }

        resmap = {}
        for s in strs:
            m = 1
            for char in s:
                m*= map[char]

            if m not in resmap:
                resmap[m] = []

            resmap[m].append(s)

        return list(resmap.values())
```
3. 这个方法就真正的做到了将时间复杂度为O(N)
