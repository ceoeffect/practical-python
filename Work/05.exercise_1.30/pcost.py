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
        for row in rows:
            try:
                cost += int(row[1]) * float(row[2])
            except:
                print("Coudn't parse line", row)
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = '/Users/emrullahzengin/Desktop/practical-python/Work/Data/missing.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
