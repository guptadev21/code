import csv
import requests

def get_entry(n):
    file = requests.get('https://docs.google.com/spreadsheets/d/1BZSPhk1LDrx8ytywMHWVpCqbm8URTxTJrIRkD7PnGTM/edit#gid=0')

    f = (line.decode('utf-8') for line in file.iter_lines())

    fields = []
    rows = []


        # creating a csv reader object
    csvreader = csv.reader(f, delimiter=',', quotechar='"')
        
    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # printing the field names
    
    for row in rows[2: 10]:
        # parsing each column of a row
        if (row[0] == str(n)):
            return(row[2], row[3])