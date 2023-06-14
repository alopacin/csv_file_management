import sys
import csv

if len(sys.argv) < 2:
    print('Spróbuj jeszcze raz.Podaj nazwy dwóch plików')
    exit()
data = []
with open ('in.csv', 'r') as f:
    reader = csv.reader(f)
    for k in reader:
        data.append(k)
        print(k)

with open ('out.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    for k in data:
        writer.writerow(k)