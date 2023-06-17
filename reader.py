import sys
import csv

# nadanie zmiennych, ktorych wartosci zostana wprowadzone z terminala
file_in = sys.argv[1]
file_out = sys.argv[2]
change = sys.argv[3:]

# jezeli uzytkownik poda za malo argumentow lub poda nieprawidlowe program zakonczy dzialanie
if len(sys.argv) < 2:
    print('Spróbuj jeszcze raz.Podałeś za mało danych')
    exit()
elif file_in != 'in.csv':
    print('Spróbuj jeszcze raz.Nieprawidłowa nazwa pliku')
    exit()
elif file_out != 'out.csv':
    print('Spróbuj jeszcze raz.Nieprawidłowa nazwa pliku')
    exit()

data = []

# odczyt danych z pliku in.csv
with open (file_in, 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        data.append(line)

# czesc odpowiadajaca za wyszukanie podanych wspolrzednych i zamianie wartosci
for changes in change:
    x, y, value = changes.split(',')
    x = int(x)
    y = int(y)
    if x >= len(data[0]) or y >= len(data):
        print('Podałeś za duże wartości współrzędnych')
        exit()
    data[x][y] = value

# zapis do pliku out.csv
with open (file_out, 'w', newline = '') as f:
    writer = csv.writer(f)
    for line in data:
        writer.writerow(line)