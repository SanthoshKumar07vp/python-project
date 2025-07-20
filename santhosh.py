class Number:
    def __init__(self,max):
        self.main=0
        self.max=max
    def __iter__(self):
        return self
    def __next__(self):
        if self.min<self.max:
            val=self.main
            self.min += 1
            return val
        else:
            raise StopIteration