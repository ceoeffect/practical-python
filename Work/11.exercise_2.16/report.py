import csv

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        total_cost = 0
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            nshares = int(record['shares'])
            price = float(record['price'])
            total_cost +=  nshares * price
    return total_cost


total_cost = portfolio_cost('/Users/emrullahzengin/Desktop/practical-python/Work/Data/portfoliodate.csv')


print(f'Total cost: {total_cost}')