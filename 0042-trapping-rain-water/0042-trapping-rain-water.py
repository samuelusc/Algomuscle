class Solution:
    def trap(self, height: List[int]) -> int:
        """
        we will use double pointer approach
        """
        # initialize the left maxium height and right maxium height
        l_max, r_max = 0,0
        
        left, right = 0, len(height)-1
        res = 0

        while left < right:
            l_max = max(l_max,height[left])
            r_max = max(r_max,height[right])

            if l_max < r_max:
                res += l_max-height[left]
                left += 1
            else:
                res += r_max-height[right]
                right -=1

        return res        
                