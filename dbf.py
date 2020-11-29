import pymysql

def connect():
    conn = pymysql.connect(host="localhost", user="root", passwd="", db="mypydb")

    myCursor = conn.cursor()

    myCursor.execute(""" CREATE TABLE IF NOT EXISTS mypydb.test1 ( id INT NOT NULL AUTO_INCREMENT , title VARCHAR(50) NOT NULL , rating VARCHAR(30) NOT NULL , price VARCHAR(10) NOT NULL , stock VARCHAR(20) NOT NULL , descp VARCHAR(999) NOT NULL , genre VARCHAR(20) NOT NULL , UPC VARCHAR(20) NOT NULL , PRIMARY KEY (id)) ENGINE = InnoDB;""")

    conn.commit()
    conn.close()

    # CREATE TABLE `mypydb`.`id` ( `id` INT NOT NULL AUTO_INCREMENT , `title` VARCHAR(50) NOT NULL , `rating` VARCHAR(30) NOT NULL , `price` VARCHAR(10) NOT NULL , `stock` VARCHAR(20) NOT NULL , `descp` VARCHAR(999) NOT NULL , `genre` VARCHAR(20) NOT NULL , `UPC` VARCHAR(20) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;

    # CREATE TABLE mypydb.id ( id INT NOT NULL AUTO_INCREMENT , title VARCHAR(50) NOT NULL , rating VARCHAR(30) NOT NULL , price VARCHAR(10) NOT NULL , stock VARCHAR(30) NOT NULL , descp LONGTEXT NOT NULL , genre VARCHAR(20) NOT NULL , UPC VARCHAR(20) NOT NULL , PRIMARY KEY (id)) ENGINE = InnoDB;
