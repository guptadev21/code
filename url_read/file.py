import csv
import requests

def get_entry(n):

    # remove '#' if you from line 7, 8 if you want to access data from uploaded csv file
    # file = requests.get('C:\project_in\python-web-scrap\Amazon Scraping - Sheet1.csv')

    # f = (line.decode('utf-8') for line in file.iter_lines())

    rows = []
    fields=[]


        # creating a csv reader object
    csvreader = open('C:\project_in\python-web-scrap\Amazon Scraping - Sheet1.csv')
        
    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row.split(","))

    for row in rows[2:n+1]:
        # parsing each column of a row
        if (row[0] == str(n)):
            
            return([row[2], row[3]])