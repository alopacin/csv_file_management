import sys
import csv

#nadanie zmiennych, ktorych wartosci zostana wprowadzone z terminala
input = sys.argv[1]
output = sys.argv[2]
change = sys.argv[3:]

#jezeli uzytkownik poda za malo argumentow lub poda nieprawidlowe program zakonczy dzialanie
if len(sys.argv) < 2:
    print('Spróbuj jeszcze raz.Podałeś za mało danych')
    exit()
elif input == 'in.csv':
    print('Spróbuj jeszcze raz.Nieprawidłowa nazwa pliku')
    exit()
elif input == 'out.csv':
    print('Spróbuj jeszcze raz.Nieprawidłowa nazwa pliku')
    exit()

data = []
with open (input, 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        data.append(line)
        print(line)

for changes in change:
    print(changes)


with open (output, 'w', newline = '') as f:
    writer = csv.writer(f)
    for line in data:
        writer.writerow(line)