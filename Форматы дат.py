class AmericanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_day(self, day):
        self.day = day

    def get_day(self):
        return self.day

    def set_month(self, month):
        self.month = month

    def get_month(self):
        return self.month

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def format(self):
        return '.'.join([str(i).rjust(2, '0') for i in [self.month, self.day, self.year]])



class EuropeanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_day(self, day):
        self.day = day

    def get_day(self):
        return self.day

    def set_month(self, month):
        self.month = month

    def get_month(self):
        return self.month

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def format(self):
        return '.'.join([str(i).rjust(2, '0') for i in [self.day, self.month, self.year]])


if __name__ == '__main__':
    american = AmericanDate(2000, 4, 10)
    european = EuropeanDate(2000, 4, 10)
    print(american.format())
    print(european.format())