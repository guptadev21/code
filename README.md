# python-web-scraping
In this repo we use selenium, csv and requests(if you want data from internet) library to scrape data from website and store it in dictionary.

## Library Installation
```bash
pip install selenium
```
```bash
pip install csv
```
```bash
pip install requests
```

## How I did it?
First, I tried to extract country and asin code from csv file.

Then, I replace {country} with country code and {asin} with asin in url in main.py.
I used selenium and firefox to open websites and extract data like :

* Product Name
* Product Price
* Image Link
* Product details


## License
[MIT]
(https://choosealicense.com/licenses/mit/)
