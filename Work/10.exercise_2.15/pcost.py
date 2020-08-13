import csv
import sys

def portfolio_cost(filename):
    """
    Read stock details from file and 
    counts total cost of stocks
    """
    cost = 0.0    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for lineno, row in enumerate(rows, start=1):
            record = dict(zip(headers,row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                cost += nshares * price
            except:
                print(f'Row {lineno}: Bad row: {row}')
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = '/Users/emrullahzengin/Desktop/practical-python/Work/Data/portfoliodate.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
