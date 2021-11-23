class ENode(object):
    def compute(self):
        self.ord = -1
        self.val = 0
        
class DNodeOne(object):
    def compute(self):
        self.d.compute()
        self.ord = self.d.ord + 1
        self.val = self.d.val + 2**(self.ord)

class DNodeZero(object):
    def compute(self):
        self.d.compute()
        self.ord = self.d.ord + 1
        self.val = self.d.val

    