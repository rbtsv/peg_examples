class ENode:        
    def init(self):
        self.ord = -1
        self.val = 0
    
    def compute(self):
        self.init()
    
    def comp(self):
        self.init()
        self.d.compute()
        self.ord = self.d.ord + 1
        self.val = self.d.val
    
        
class DNodeOne(ENode):
    def compute(self):
        self.comp()
        self.val += 2**(self.ord)

class DNodeZero(ENode):
    def compute(self):
        self.comp()
    