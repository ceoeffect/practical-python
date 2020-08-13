import os

cost = 0.0
with open('/Users/emrullahzengin/Desktop/practical-python/Work/Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        cost += int(row[1]) * float(row[2])

print(f'Total cost {cost}')


