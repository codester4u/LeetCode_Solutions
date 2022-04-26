class SeatManager:

    def __init__(self, n: int):
        self.res=[i for i in range(1,n+1)]

    def reserve(self) -> int:
        return heapq.heappop(self.res)

    def unreserve(self, seatNumber: int) -> None:
        return heappush(self.res, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)