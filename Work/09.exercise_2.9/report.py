import csv

def read_portfolio(filename):    
    data = []    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            data.append(row)   
    return data

def read_prices(filename):
    data = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                data[row[0]] = float(row[1])
            except:
                print('') 
    return data


def make_portfolio(portfolio, prices):
    data = []
    for item in portfolio:
        data.append((item[0], int(item[1]), float(item[2]), prices[item[0]] - float(item[2])))
    return data


portfolio = read_portfolio('/Users/emrullahzengin/Desktop/practical-python/Work/Data/portfolio.csv')
prices = read_prices('/Users/emrullahzengin/Desktop/practical-python/Work/Data/prices.csv')

report = make_portfolio(portfolio, prices)

print('      Name     Shares      Price      Change')
print('---------- ---------- ---------- -----------')
for item in report:
    print('%10s %10d %10.2f %10.2f' % item)



