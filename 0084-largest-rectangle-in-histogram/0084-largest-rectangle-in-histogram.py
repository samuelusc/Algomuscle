class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [0]
        heights = [0] + heights + [0]

        res = 0

        for i in range(1, len(heights)):
            if heights[i] >= heights[stack[-1]]:
                stack.append(i)

            else:
                while stack and heights[i] < heights[stack[-1]]:
                    mid = stack.pop()
                    left = stack[-1]
                    right = i

                    w = right - left -1
                    h = heights[mid]
                    res = max(h*w, res)

                stack.append(i)
        
        return res