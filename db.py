import pymysql

def konnect():
    con=pymysql.connect(host='localhost', user='root', passwd='', db='scrapedb')
    mycursor=con.cursor()
    mycursor.execute('''CREATE TABLE IF NOT EXISTS scrapedb.books1 ( id INT NOT NULL AUTO_INCREMENT , title VARCHAR(50) NOT NULL , rating VARCHAR(50) NOT NULL , price VARCHAR(50) NOT NULL , stock VARCHAR(50) NOT NULL , descp TEXT(5000) NOT NULL , genre VARCHAR(50) NOT NULL , upc VARCHAR(50) NOT NULL , PRIMARY KEY (id)) ENGINE = InnoDB;''')
    con.commit()
    con.close()