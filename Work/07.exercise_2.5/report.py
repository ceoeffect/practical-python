import csv

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''

    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holdings = {'name':row[0], 'shares':int(row[1]), 'price':float(row[2])}
            portfolio.append(holdings)
    return portfolio


portfolio = portfolio_cost('/Users/emrullahzengin/Desktop/practical-python/Work/Data/portfolio.csv')

total_cost = 0.0
for s in portfolio:
    total_cost += s['shares'] * s['price']

print(f'Total cost: {total_cost}')