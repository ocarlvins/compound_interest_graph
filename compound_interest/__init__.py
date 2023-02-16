from decimal import Decimal as d
from compound_interest.chart import deposit_chart, monthly_return_chart
from compound_interest.investment_model import Investment


def cell(item):
    try:
        return f'{item:,.2f}'.rjust(20)
    except Exception as e:
        return str(item).rjust(20)


def row(*args):
    print(''.join([cell(i) for i in args]))


periods = {
    'annually': 0,
    'monthly': 1,
    'daily': 2
}

initial = 1000000
multiplier = 1
times = 0
vests = [
    Investment(d('17'), initial_deposit=initial*multiplier, per=periods['daily'], compounding=True, times=times),
    Investment(d('16'), initial_deposit=initial*multiplier, per=periods['daily'], compounding=True, times=times),
    Investment(d('15'), initial_deposit=initial*multiplier, per=periods['daily'], compounding=True, times=times),
    Investment(d('14'), initial_deposit=initial*multiplier, per=periods['daily'], compounding=True, times=times),
    Investment(d('13'), initial_deposit=initial*multiplier, per=periods['daily'], compounding=True, times=times),
    Investment(d('12'), initial_deposit=initial*multiplier, per=periods['daily'], compounding=True, times=times),
    Investment(d('11'), initial_deposit=initial*multiplier, per=periods['daily'], compounding=True, times=times),
    Investment(d('10'), initial_deposit=initial*multiplier, per=periods['daily'], compounding=True, times=times),
    Investment(d('9'), initial_deposit=initial*multiplier, per=periods['daily'], compounding=True, times=times),
    Investment(d('8'), initial_deposit=initial*multiplier, per=periods['daily'], compounding=True, times=times),
    Investment(d('7'), initial_deposit=initial*multiplier, per=periods['daily'], compounding=True, times=times),
    Investment(d('6'), initial_deposit=initial*multiplier, per=periods['daily'], compounding=True, times=times),
]
deposit_chart(
    *vests, times=times, multiplier=multiplier
)
monthly_return_chart(
    *[i.setShow('monthly_returns') for i in vests], times=times, multiplier=multiplier
)

'''
                             Inferences
                       ---------------------

- Takes deposit of 20,000,000 to make 131,209 monthly interest if compounding daily at 7.7%
    if doing Safaricom Mali

Questions
    How long does it take to make 120,000 monthly?
    How long does it take to double the capital?

To Dos
    Create various models that will answer the questions above


Mansa X
    200 classes
    bonds and bills
    sydney
    asia
    europe
    kenya government 
    hedge fund 
        SIB
        Laurium Capital - South Africa

    5% fee
    gross 20.99%
    5% - finanial services chrge, management fees
    no tax on capital gains except real estate
    no joining
'''