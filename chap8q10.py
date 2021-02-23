class Calculator:
    def __init__(self, reflist):
        self.reflist = reflist
    
    def sum(self):
        ref=0
        for i in self.reflist:
            ref += i
        return ref
    
    def avg(self):
        total = self.sum()
        return total/len(self.reflist)

if __name__ == '__main__':
    cal1 = Calculator([1,2,3,4,5])
    print(cal1.sum())
    print(cal1.avg())