import sys
import csv

# jezeli uzytkownik poda za malo argumentow program zakonczy dzialanie
if len(sys.argv) < 2:
    print('Spróbuj jeszcze raz.Podałeś za mało danych')
    exit()

# nadanie zmiennych, ktorych wartosci zostana wprowadzone z terminala
file_in = sys.argv[1]
file_out = sys.argv[2]
changes = sys.argv[3:]

data = []

# odczyt danych z pliku csv
with open (file_in, 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        data.append(line)

# czesc odpowiadajaca za wyszukanie podanych wspolrzednych i zamianie wartosci
for change in changes:
    if len(change.split(',')) != 3:
        print('Podałeś błędne dane.Spróbuj jeszcze raz')
        exit()
    x, y, value = change.split(',')
    if not x.isdigit() or not y.isdigit():
        print('Podałeś nieprawidłowe wartości współrzędnych.Spróbuj jeszcze raz')
        exit()
    else:
        x = int(x)
        y = int(y)
    if x >= len(data[0]) or y >= len(data):
        print('Podałeś za duże wartości współrzędnych')
        exit()
    data[x][y] = value
print(f'Zmodyfikowany plik będzie miał następującą zawartość: \n{data}')

# zapis do pliku csv
with open (file_out, 'w', newline = '') as f:
    writer = csv.writer(f)
    for line in data:
        writer.writerow(line)