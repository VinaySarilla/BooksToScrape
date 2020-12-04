import requests
from bs4 import BeautifulSoup
import pymysql
import fb
import time

global t0
global t1

def getNoOfPages():
    url = 'https://books.toscrape.com'
    sourceCode = requests.get(url)
    plainText = sourceCode.text
    soup = BeautifulSoup(plainText, 'html.parser')
    noOfPages = soup.find('li', {'class':'current'}).string.strip()
    noOfPages = int(noOfPages[-2:])
    return noOfPages

def tradeSpider():
    page = 1
    noOfPages=getNoOfPages()

    while page <= noOfPages :
        t0 = time.time()
        url = 'https://books.toscrape.com/catalogue/page-' + str(page) + '.html'
        sourceCode = requests.get(url)
        plainText = sourceCode.text
        soup = BeautifulSoup(plainText, 'html.parser')
        #print(soup.prettify())
        for links in soup.find_all('article', {'class':'product_pod'}):
            #print(links)
            bookLink = 'https://books.toscrape.com/catalogue/' + links.h3.a.get('href')
            eachBook(bookLink)
            # print(temp)
            # title = links.h3.a.get('title')
            # print(title)
            # rating = links.p.get('class')
            # print(rating[1])
        t1 = time.time()
        print("-------Page "+str(page) + " Done--------\n")
        print(f"------Total time taken {round(t1-t0,2)} seconds")
        page += 1
# article class = "product_pod"  div = "image_container"


def eachBook(bookLink):
    sourceCode = requests.get(bookLink)
    plainText = sourceCode.text
    bookSoup = BeautifulSoup(plainText, 'html.parser')

    title = bookSoup.h1.string
    print(title)
    price = bookSoup.p.string
    rating = bookSoup.find_all('p')[2].get('class')[1]
    description = bookSoup.find_all('p')[3].string
    availability = bookSoup.find_all('td')[5].string
    upc = bookSoup.find_all('td')[0].string
    genre = bookSoup.find_all('li')[2].a.string
    formatting(title, rating, price, availability, description, genre, upc)

def formatting(title, rating, price, availability, description, genre, upc):
    title = title
    rating_dict = {'One': '1', 'Two': '2', 'Three': '3', 'Four': '4', 'Five': '5'}
    rating = int(rating_dict[rating])
    description=description
    price=float(price[2:])
    availability = int(availability[10:-11])
    upc = upc
    genre = genre
    insertingINdB(title, rating, price, availability, description, genre, upc)

def insertingINdB(title, rating, price, availability, description, genre, upc):
    con = pymysql.connect(host='localhost', user='root', passwd='', db='scrapedb')
    mycursor = con.cursor()
    args=(title, rating, price, availability, description, genre, upc)
    query="INSERT INTO books1 values(NULL, %s,  %s, %s, %s, %s, %s, %s)"
    mycursor.execute(query, args)
    con.commit()
    con.close()

fb.konnect()
tradeSpider()

