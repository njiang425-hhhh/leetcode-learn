class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 定义左右双指针
        left, right = 0, len(height) - 1
        result = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            result = max(area, result)

            # 移动左右指针中高度更小的指针
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result