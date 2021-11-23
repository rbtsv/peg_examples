class ENode(object):        
    def init(self):
        self.ord = -1
        self.val = 0
    
    def compute(self):        
        self.init()
        if hasattr(self, "d"):
            self.d.compute()
            self.ord = self.d.ord + 1
            self.val = self.d.val
    
        
class DNodeOne(ENode):
    def compute(self):
        super(DNodeOne, self).compute()
        self.val += 2**(self.ord)
    