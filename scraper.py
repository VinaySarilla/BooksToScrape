import requests
import csv
from bs4 import BeautifulSoup
import pymysql
import db

def trade_spider(maxpages):
    page = 1
    while page <= maxpages:
        url = 'http://books.toscrape.com/catalogue/page-'+str(page)+'.html'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,'html.parser')

        for link in soup.findAll('article', {'class':'product_pod'}):
            href = 'http://books.toscrape.com/catalogue/' + link.h3.a.get('href')
            title = link.h3.a.get('title')
            rating = link.p.get('class')
            print(href)

            each_book_detail(href)
        page+=1

def each_book_detail(book_url):
    source_code = requests.get(book_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')


    for book in soup.findAll('article',{'class':'product_page'}):
        # print(book.prettify())

        title = book.h1.string
        # print(title)                                          #title

        price = soup.findAll('p')[0].string
        # print(price)                                        #price

        description = soup.findAll('p')[3].string
        # print(description)                    #desription

        UPC = soup.findAll('td')[0].string
        # print(UPC)                   # UPC

        stocks = soup.findAll('td')[5].string
        # print(stocks)                   # stocks available

        ratings = book.findAll('p')[2].get('class')[1]
        # print(ratings)           # ratings


    for get_genre in soup.findAll('div', {'class': 'page_inner'}):
        genre=soup.findAll('li')[2].a.string
        # print(genre)                   # genre
        break

    conn = pymysql.connect(host="localhost", user="root", passwd="", db="mypydb")
    myCursor = conn.cursor()
    args=(title,ratings,price,stocks,description,genre,UPC)
    query = "INSERT INTO test1 VALUES (NULL, %s, %s, %s, %s, %s, %s, %s)"
    myCursor.execute(query,args)
    myCursor.close()
    conn.commit()
    conn.close()

    print("done")

db.connect()
trade_spider(3)