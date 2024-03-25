class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in hashmap:
                return [hashmap[rest], i]

            hashmap[nums[i]] = i
        
        return -1