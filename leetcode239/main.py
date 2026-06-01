class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 输出列表的大小
        ans = [0] * (len(nums) - k + 1)
        # 定义一个双向的队列，用来控制每次窗口的数值
        q = deque()

        for i, x in enumerate(nums):
            # 做一个循环去控制队列是个递减的状态
            while q and nums[q[-1]] <= x:
                q.pop()
            # 记录下表，便于判断是否要窗口滑动时是否离开队列
            q.append(i)

            # 窗口左端现在的位置
            left = i - k + 1
            if left > q[0]:
                q.popleft()

            # 将窗口当前最大的数复制到ans中用于返回
            if left >= 0:
                ans[left] = nums[q[0]]

        return ans