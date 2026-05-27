class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()

        # i相当于a
        for i in range(len(nums)):
            # 如果nums[i]大于0，可以直接返回
            if nums[i] > 0:
                return result

            # 去重a，避免有重复的三元组
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # left相当于b
            left = i + 1
            # right相当于c
            right = len(nums) - 1

            while right > left:
                sum = nums[i] + nums[left] + nums[right]

                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # 当已经得到和为0的三元组时，如果nums[right] == nums[right - 1]或者nums[left] == nums[left + 1]可以直接跳过，避免重复
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1

                    # 如果不存在就right和left同时移动
                    right -= 1
                    left += 1

        return result