from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0  # Track the maximum area found so far

        while l < r:
            # 1. Width is the distance between the lines
            width = r - l
            
            # 2. Height is limited by the shorter of the two lines
            current_height = min(heights[l], heights[r])
            
            # 3. Calculate current area and update our maximum
            current_area = width * current_height
            max_area = max(max_area, current_area)
            
            # 4. Move the pointer pointing to the shorter line inward
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                
        return max_area