import csv


def read_prices(filename):
    """
    Current stock prices
    """
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        d = {}
        for row in rows:
            try:
                d[row[0]] = float(row[1])
            except:
                print('Empty line...') 
    return d

def portfolio_cost(filename):
    """
    Read stock details from file and 
    counts total cost of stocks
    """  
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        d = []
        for row in rows:
            try:
                d.append(row)
            except:
                print("Coudn't parse line", row)
    return d

current_prices = read_prices('/Users/emrullahzengin/Desktop/practical-python/Work/Data/prices.csv')
portfolio = portfolio_cost('/Users/emrullahzengin/Desktop/practical-python/Work/Data/portfolio.csv')

profit_loss = 0

for i in portfolio:
    cost = (int(i[1]) * float(i[2])) - (current_prices[i[0]] * int(i[1]))
    profit_loss += cost

print(profit_loss)

