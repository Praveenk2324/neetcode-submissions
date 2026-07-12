class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = 1
        for i in range(len(nums)):
            res *= i

        return res