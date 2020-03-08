from CsvReader import CsvReader


def addition(a, b):
    a = int(a)
    b = int(b)
    return a + b


def subtraction(a, b):
    a = int(a)
    b = int(b)
    return b - a


def multiplication(a, b):
    a = int(a)
    b = int(b)
    return a * b


def division(a, b):
    return a / b


def square(a):
    a = int(a)
    return a ** 2


def squareroot(a):
    a = int(a)
    return float('{.10}'.format(a ** (1 / 2)))


def mean(data):
    mean = data
    return mean


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = a * b
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def square_root(self, a):
        self.result = squareroot(a)
        return self.result


class CSVStats(Calculator):
    data = []

    def __init__(self, data_file):
        self.data = CsvReader(data_file)
        pass

    def mean(self):
        mean(self.data)
