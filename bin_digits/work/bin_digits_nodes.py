class ENode:
    def compute(self):
        self.ord = -1
        self.val = 0
        
class DNodeOne:
    def compute(self):
        self.d.compute()
        self.ord = self.d.ord + 1
        self.val = self.d.val + 2**(self.ord)

class DNodeZero:
    def compute(self):
        self.d.compute()
        self.ord = self.d.ord + 1
        self.val = self.d.val

    