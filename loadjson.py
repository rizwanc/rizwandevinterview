import json
import csv

#open the file
with open('quotes_api.json', encoding='UTF-8-SIG') as f:
  data = json.load(f)

# Create header columns
columnTitleRow = "ID, CompanyName, Symbol, CurrentPrice, Change, PercentChange"

# id variable to postgresql id column
id = 0

# create the quotes csv and write the data from quotes_api.json
# to it.
with open('quotes.csv', 'w', newline='\n') as f:
    writer = csv.writer(f)
    writer.writerow(["CompanyName, Symbol, CurrentPrice, Change, PercentChange"])
    for quotes in data:
        id = id + 1
        companyname = quotes['CompanyName']
        symbol = quotes['Symbol']
        currentprice = quotes['CurrentPrice']['Amount']
        change = quotes['Change']['Amount']
        percentchange = quotes['PercentChange']['Value']
        
        writer.writerow([id, companyname, symbol, currentprice, change, percentchange])
