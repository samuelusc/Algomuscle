class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # slicing T:O(n) S:O(1)
        s[:] = s[::-1]

        # reversed V.S reverse
        # s[:] = reversed(s)  with iterable parameter
        # s.reverse() no parameter in ()

        # reverse can only be used with lists and reveses the element of the list in place
        # reversed can work with any iterable(lists, tuples, strings,etc). It doesn't modify the original iterable instead
        # it creates a reverse iterator 

