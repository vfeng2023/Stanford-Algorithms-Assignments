from heapq import heappush, heappop, heapify
class MedianFinder():
    def __init__(self):
        self.firsthalf = [] # maxheap, has first half of elements and more elemetns if odd
        self.secondhalf = [] # min heap, has second half of elements

    def add(self, val):
        heappush(self.firsthalf, (-val, val))

        while len(self.firsthalf) > len(self.secondhalf):
            _, val = heappop(self.firsthalf)
            heappush(self.secondhalf, (val, val))

        while len(self.secondhalf) > len(self.firsthalf):
            _, val = heappop(self.secondhalf)
            heappush(self.firsthalf, (-val,val))

    def findMedian(self):
        return self.firsthalf[0][1]
    


with open("Median.txt", "r") as f:
    nums = list(map(int, f.readlines()))

total = 0
med = MedianFinder()
for n in nums:
    med.add(n)
    total += med.findMedian()

print(total % 10000)
