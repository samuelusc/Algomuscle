#27. Remove Element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for num in nums:
            if num != val:
                nums[slow] = num
                slow += 1
        return slow
    def main():
        solution = Solution()
        # Test case 1
        nums1 = [3, 2, 2, 3]
        val1 = 3
      
        print("Test case 1 - Original List: {}, Value to Remove: {}".format(nums1, val1))
        new_length1 = solution.removeElement(nums1, val1)
        print("New length:", new_length1)
        print("Modified List:", nums1[:new_length1])  # Print the modified list up to the new length
    
        # Test case 2
        nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
        val2 = 2
        print("\nTest case 2 - Original List: {}, Value to Remove: {}".format(nums2, val2))
        new_length2 = solution.removeElement(nums2, val2)
        print("New length:", new_length2)
        print("Modified List:", nums2[:new_length2])  # Print the modified list up to the new length
  

  if __name__ == "__main__":
        main()
            
