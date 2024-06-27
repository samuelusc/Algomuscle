class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0

        for fast in nums:
            if fast != val:
                nums[slow] = fast
                slow += 1
    
        return slow