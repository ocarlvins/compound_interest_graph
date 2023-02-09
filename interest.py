from decimal import Decimal as d
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def cell(item):
    try:
        return f'{item:,.2f}'.rjust(20)
    except Exception as e:
        return str(item).rjust(20)



def outerFunction(self, input):
    self.external = input

class Person:
    deposits = d('0')
    month = d('1')
    interest = d('0')
    interest_perc = d('12')
    counter = 0
    
    def __init__(self, interest) -> None:
        if interest:
            self.interest = d(interest)/d(12)
        ...
    
    def new_month(self, deposit):
        ...
        self.interest += self.deposits * (self.interest_perc/d('12'))/d('100')
        self.deposits += d(deposit)
        self.counter +=1

        print(
            f"{cell(self.counter)}"+
            f"{cell(self.deposits)}"+ 
            f"{cell(round(self.interest, 2))}"
        )

    def outerFunction(self, input):
        outerFunction(self, input)
        print(self.external)

carl = Person(12)

print(f"{cell('Month')}{cell('Deposits')}{cell('Interest')}")

for i in range(20*12):
    carl.new_month('7000')

carl.outerFunction('some')

print(round(60000*12/100, 2))