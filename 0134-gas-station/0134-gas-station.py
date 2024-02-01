class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, cur_sum, start = 0, 0, 0

        for i in range(len(cost)):
            cur_sum += gas[i] - cost[i]
            total += gas[i] -cost[i]

            if cur_sum < 0:
                cur_sum = 0
                start = i + 1

        return start if total >= 0 else -1