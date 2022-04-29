class RandomizedSet:

    def __init__(self):
        self.values=[]
        self.valToIndex=defaultdict(int)

    def insert(self, val: int) -> bool:
        if val in self.valToIndex: return False
        self.valToIndex[val]=len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valToIndex: return False
        index=self.valToIndex[val]
        self.valToIndex[self.values[-1]]=index
        del self.valToIndex[val]
        self.values[index]=self.values[-1]
        self.values.pop()
        return True

    def getRandom(self) -> int:
        index=randint(0, len(self.values)-1)
        return self.values[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()