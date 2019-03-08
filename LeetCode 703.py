import heapq

class kthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.lst = nums
        self.size = len(nums)
        self.k = k
        heapq.heapify(self.lst)
        while self.size > self.k:
            heapq.heappop(self.lst)
            self.size -= 1

    def add(self, val: int) -> int :
        if self.size < self.k:
            heapq.heappush(self.lst, val)
            self.size += 1
        elif self.lst[0] < val:
            heapq.heapreplace(self.lst, val)
        return self.lst[0]