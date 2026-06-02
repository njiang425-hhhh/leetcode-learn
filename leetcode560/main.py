class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 定义前缀和的列表,长度为len(nums) + 1，其中s[0] = 0
        s = [0] * (len(nums) + 1)
        # 对s进行赋值
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x

        # 哈希表用来记录值为s[j]的前缀和的个数
        cnt = defaultdict(int)
        ans = 0
        # 遍历s
        for a in s:
            # s[j] - k查看前缀和为s[i]，而cnt[s[i]]又是查看个数
            ans += cnt[a - k]
            cnt[a] += 1

        return ans