data = [
    dict(
        base_currency = 'KSH',
        conversions=[
            dict(
                name='USD',
                buying= 100,
                selling= 120
            ),
            dict(
                name= 'RMB',
                buying= 19,
                selling= 25
            ),
            dict(
                name= 'GBP',
                buying= 140,
                selling= 145
            ),
        ]
    )
]

def convert(in_curr='KSH', out_curr='USD', amount=0):
    for conversion in data:
        if conversion['base_currency'] == 'KSH':
            for curr in conversion['conversions']:
                if (in_curr== conversion['base_currency'] and out_curr == curr['name']) or (out_curr== conversion['base_currency'] and in_curr == curr['name']):
                    if in_curr == conversion['base_currency']:
                        return dict(name=out_curr, amount= amount/curr['selling'])
                    else:
                        return dict(name=out_curr, amount = amount*curr['buying'])

print(convert('KSH', 'USD', 120))
print(convert('USD', 'KSH', 1))