class Mean(object):
    def __init__(self):
        self.sum = 0
        self.entries = 0

    def add(self, item: int):
        self.sum += item
        self.entries += 1

    def __call__(self, item: int):
        self.add(item)

    def mean(self):
        return self.sum / self.entries

    def __len__(self):
        return self.entries
