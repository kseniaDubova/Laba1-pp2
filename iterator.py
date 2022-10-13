
class Iterator:

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num

