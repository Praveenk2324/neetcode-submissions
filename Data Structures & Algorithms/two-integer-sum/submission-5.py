class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      
        sorted_num = sorted(nums)
        i = 0
        j = len(sorted_num) - 1
        for k in range(len(sorted_num)):
            sum_ =  sorted_num[i] + sorted_num[j] 
            if sum_ == target:
                return [i, j]
            if sum_ <= target:
                i += 1
            else:
                j -= 1
        return []