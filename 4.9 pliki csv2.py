import csv

fields[]
rows = []

filename = 'records.csv'
with open(filename, 'r') as f:
    csvreader = csv.reader(f)
    print((csvreader))