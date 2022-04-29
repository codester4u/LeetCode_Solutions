class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time=timeToLive
        self.lookup=OrderedDict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.rm_expired(currentTime)
        self.lookup[tokenId]=self.time+currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.rm_expired(currentTime)
        if tokenId in self.lookup:
            self.lookup.move_to_end(tokenId)
            self.lookup[tokenId]=self.time+currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.rm_expired(currentTime)
        return len(self.lookup)
    def rm_expired(self, currentTime:int)->None:
        while self.lookup and next(iter(self.lookup.values()))<=currentTime:
            self.lookup.popitem(last=False)

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)