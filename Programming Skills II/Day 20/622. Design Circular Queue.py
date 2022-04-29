class MyCircularQueue:

    def __init__(self, k: int):
        self.size=k
        self.queue=['']*k
        self.head=-1
        self.tail=-1
        
    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            if self.head==-1:
                self.head=0
            self.tail=(self.tail+1)%self.size
            self.queue[self.tail]=value
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            if self.head==self.tail:
                self.head, self.tail= -1, -1
            else:
                self.head=(self.head+1)%self.size
            return True
        return False
    

    def Front(self) -> int:
        if self.isEmpty(): return -1
        else: return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        else: return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.head==-1 and self.tail==-1

    def isFull(self) -> bool:
        return (self.tail+1)%self.size==self.head


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()