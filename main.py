import openpyxl
import requests
from bs4 import BeautifulSoup

read_book = openpyxl.open('shop_price.xlsx', read_only=True)
sheet_read = read_book.active

clean_url = []

#витягую всі силки mebli-bristol
for row in sheet_read.iter_rows(min_row=4, max_row=4, min_col=2, max_col=16):
    for cell in row:
        url = cell.value
        #чистка формули в норм силку
        url = url[12:]
        while True:
            sample = 'html'
            symbol = -1
            url = url[:symbol]
            res = url.endswith(sample)
            if res == True:
                clean_url.append(url)
                #print(url)
                break

for url in clean_url:
    print(url)
    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text, features="html.parser")

    price = soup.find('span', {'class': 'price'})
    price = price.text

    price = price.replace(' ', '')
    price = price.replace('₴', '')
    print(price)