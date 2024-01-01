class Solution:
    def isHappy(self, n: int) -> bool:
        def next_number(num):
            total_sum = 0
            # or we can use sum(int(digit) ** 2 for digit in str(num))
            while num:
                num, remainder = divmod(num, 10)
                total_sum += remainder ** 2
            return total_sum

        slow = n
        fast = next_number(n)
        # tend to make mistake to set next_number(n)
        while slow != fast:
            slow = next_number(slow)
            fast = next_number(next_number(fast))

        return slow == 1
            