class FibonacchiLst:
    def __init__(self, lst):
        self.lst = lst
        self.idx = 0
        self.fib_set = self._generate_fibonacci_set(max(lst))
    
    def _generate_fibonacci_set(self, n):
        fib_set = set()
        a, b = 0, 1
        while a <= n:
            fib_set.add(a)
            a, b = b, a + b
        return fib_set
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.idx < len(self.lst):
            num = self.lst[self.idx]
            self.idx += 1
            if num in self.fib_set:
                return num
        raise StopIteration

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
fib_iterator = FibonacchiLst(lst)
print(list(fib_iterator))

