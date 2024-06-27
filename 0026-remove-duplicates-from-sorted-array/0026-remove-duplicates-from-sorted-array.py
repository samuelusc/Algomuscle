class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0

        for fast in nums:
            if fast != nums[slow]:
                slow +=1
                nums[slow] = fast
            
        return slow+1