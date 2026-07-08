class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = 1
        z_count = 0
        res = [0] * n
        for i in range(n):
            if nums[i] == 0:
                z_count += 1
                continue
            prod *= nums[i]
        
        for i in range(n):
            if z_count == 1:
                if nums[i] == 0:
                    res[i] = prod
                else:
                    res[i] = 0
            elif z_count == 0:
                res[i] = prod // nums[i]
        return res
                


