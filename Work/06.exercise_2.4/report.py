import csv

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''

    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio


portfolio = portfolio_cost('/Users/emrullahzengin/Desktop/practical-python/Work/Data/portfolio.csv')

total_cost = 0.0

for s in portfolio:
    total_cost += s[1] * s[2]

print(f'Total cost: {total_cost}')