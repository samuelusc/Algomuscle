class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        #先满足height 然后满足k
        # 排序 
        people.sort(key = lambda x: (-x[0],x[1]))

        queue = []

        for each in people:
            # 将 each 按照k的位置插入
            queue.insert(each[1], each)

        return queue