class ENode:
    def compute(self):
        self.ord = -1
        self.val = 0
        
class DNodeOne:
    def compute(self):
        self.D.compute()
        self.ord = self.D.ord + 1
        self.val = self.D.val + 2**(self.ord)
        #print(self.__dict__)

class DNodeZero:
    def compute(self):
        self.d.compute()
        self.ord = self.d.ord + 1
        self.val = self.d.val

    