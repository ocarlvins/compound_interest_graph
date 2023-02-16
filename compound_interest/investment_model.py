from decimal import Decimal as d


class Investment:
    def __init__(self, perc, initial_deposit, per=None, compounding=True, times=0, show='points') -> None:
        self.perc = d('10')
        self.deposit = d('0')
        self.interest = d('0')
        self.period = 0
        self.compounding = True
        self.points = []
        if perc:
            self.perc = d(perc)
        if initial_deposit:
            self.initial = initial_deposit
            self.deposit = initial_deposit
        self.compounding = compounding

        self.per = d([1,12,365][per or 2])
        self.points = []
        self.monthly_returns = []
        self.show = show

        self.calculate(initial_deposit, times)

    def new_period(self, addition=d('0')):
        interest = self.deposit * self.perc/d(self.per)/d(100)
        self.interest += interest
        self.period += 1
        if self.compounding:
            self.deposit += interest + d(addition)
        else:
            self.deposit += d(addition)

        # self.points.append([d(f"{int(self.period/self.per)}.{(self.period%self.per)/self.per}"), self.deposit])
        self.points.append([self.period/self.per, self.deposit])
        self.monthly_returns.append([self.period/self.per, (self.deposit * self.perc) / (d('12') * d('100'))])

        # row(int(self.period/self.per), self.period%self.per, self.perc, self.interest, self.deposit)
        if self.compounding:
            return self.deposit
        else:
            return self.deposit + self.interest

    def get_points(self):
        return self.points

    def calculate(self, initial, times):
        additions = []# [41000, 6000]

        for i in range(365*20):
            try:
                addition=additions[i]
            except Exception as e:
                addition=d('0')


            deposit = self.new_period(addition=addition)
            if times:
                if deposit > (sum(additions) + initial)*times:
                    break

    def setShow(self, show='points'):
        self.show = show
        return self

    def __iter__(self):
        if self.show == 'points':
            yield from self.points
        elif self.show == 'monthly_returns':
            yield from self.monthly_returns

