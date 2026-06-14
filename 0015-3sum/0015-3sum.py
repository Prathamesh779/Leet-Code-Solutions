class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = set()

        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return [list(t) for t in res]