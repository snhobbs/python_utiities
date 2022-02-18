from scipy import constants

class Range:
    def __init__(self, a, b):
        self.min = min([a, b])
        self.max = max([a, b])
        assert(a < b)

    @property
    def low(self):
        return self.min

    @property
    def high(self):
        return self.max

    def mean(self):
        return (self.min + self.max)/2

    def __repr__(self):
        return "[{}, {}]".format(self.min, self.max)

    def is_in_range(self, value):
        return value <= self.max and value >= self.min

    def mult(self, a):
        return Range(self.min*a, self.max*a)

class Temperature:
    def __init__(self, celsius):
        self._temp = 0
        if type(celsius) is Temperature:
            self.set_celsius(celsius.celsius)
        else:
            self.set_celsius(celsius)

    def __lt__(self, b):
        return self.kelvin < b.kelvin

    def __gt__(self, b):
        return self.kelvin > b.kelvin

    def __eq__(self, b):
        return self.kelvin == b.kelvin

    def __ge__(self, b):
        return self.kelvin >= b.kelvin

    def __le__(self, b):
        return self.kelvin <= b.kelvin


    def set_celsius(self, t):
        self.set_kelvin(t + constants.zero_Celsius)

    def set_kelvin(self, t):
        assert(t>=0)
        self._temp = t

    @property
    def celsius(self):
        return self._temp - constants.zero_Celsius

    @property
    def kelvin(self):
        return self._temp
