class Range:
    def __init__(self, a, b):
        self.min = min([a, b])
        self.max = max([a, b])
        assert(a < b)

    def mean(self):
        return (self.min + self.max)/2

    def __repr__(self):
        return "[{}, {}]".format(self.min, self.max)

    def is_in_range(self, value):
        return value <= self.max and value >= self.min
