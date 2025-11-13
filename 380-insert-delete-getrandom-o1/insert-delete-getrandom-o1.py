import random

class RandomizedSet:
    def __init__(self):
        self.m, self.a = {}, []
    
    def insert(self, val: int) -> bool:
        if val in self.m: return False
        self.m[val] = len(self.a)
        self.a.append(val)
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.m: return False
        i, last = self.m[val], self.a[-1]
        self.m[last], self.a[i] = i, last
        self.a.pop()
        del self.m[val]
        return True
    
    def getRandom(self) -> int:
        return random.choice(self.a)