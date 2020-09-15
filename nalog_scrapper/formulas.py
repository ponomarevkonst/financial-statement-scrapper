represent = lambda number: str(round(100 * number, 2)) + '%'
profit_margin = lambda self, year: represent(self.find_in(2400, year) / self.find_in(2110, year))
ebit_margin = lambda self, year: represent(self.find_in(2300, year) / self.find_in(2110, year))
sales_margin = lambda self, year: represent(self.find_in(2200, year) / self.find_in(2110, year))
gross_margin = lambda self, year: represent(self.find_in(2100, year) / self.find_in(2110, year))
roe = lambda self, year: represent(self.find_in(2400, year) / (self.find_in(1300, year) + self.find_in(1300, year-1)))