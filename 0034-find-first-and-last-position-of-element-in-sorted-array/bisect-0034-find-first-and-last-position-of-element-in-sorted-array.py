class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # nums must be sorted Array and can apply bisect module
        left = bisect.bisect_left(nums, target)
        right = bisect_left(nums, target + 1)
        # (target, target ) at the same pos then return [-1,-1]
        return [-1,-1] if left == right else [left, right -1]
