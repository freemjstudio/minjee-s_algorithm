class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        n = len(nums)
        for i in range(0, n, 2):
            total += nums[i]
        return total
