import random
class RandomizedSet:
    
    
    def __init__(self):
        self.visit=set()
        

    def insert(self, val: int) -> bool:
        if val in self.visit:
            return False
        self.visit.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.visit:
            self.visit.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        if not self.visit:
            return 0
        return random.choice(tuple(self.visit))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()