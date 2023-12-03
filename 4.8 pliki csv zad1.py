import csv

fields = ['name','brench','tear']
row = ['radek','cloe','5']

zipped_dict = dict(zip(fields,row))
print(zipped_dict)

with open("records.csv", 'w', newline='') as csv_f:
    # csvwriter = csv.writer(csv_f)
    # csvwriter.writerow(fields)
    # csvwriter.writerow(row)
    cswriter = csv.DictWriter(csv_f, fieldnames=field)
    cswriter.writerow(zipped_dict)
    cswriter.writerows(  )