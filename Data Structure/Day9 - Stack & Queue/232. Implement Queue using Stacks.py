class MyQueue:

    def __init__(self):
        self.sta1=[]
        self.sta2=[]

    def push(self, x: int) -> None:
        while self.sta1:
            self.sta2.append(self.sta1.pop())
        self.sta1.append(x)
        
        while self.sta2:
            self.sta1.append(self.sta2.pop())
            

    def pop(self) -> int:
        return self.sta1.pop()

    def peek(self) -> int:
        return self.sta1[-1]

    def empty(self) -> bool:
        return not self.sta1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()