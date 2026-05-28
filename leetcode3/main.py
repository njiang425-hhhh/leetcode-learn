class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 定义窗口的左边界
        left = 0
        max_len = 0

        # 定义字典用来检查字符是否出现及其索引
        result = {}

        # 窗口的右边界
        for right, m in enumerate(s):
            # 右边界要不小于左边界
            if m in result and result[m] >= left:
                left = result[m] + 1
            result[m] = right
            max_len = max(max_len, right - left + 1)

        return max_len