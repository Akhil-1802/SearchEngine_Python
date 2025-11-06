import sqlite3

db = "search_engine.db"
# Connect to a database (creates one if it doesn’t exist)
def createtables():
    conn = sqlite3.connect(db)
    cursor= conn.cursor()
   
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS urls (
        id INTEGER PRIMARY KEY,
        url TEXT NOT NULL
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS url_data(
        id INTEGER PRIMARY KEY,
        url TEXT NOT NULL,
        data TEXT NOT NULL
    )
                   ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inverted(
        id INTEGER PRIMARY KEY,
        word TEXT NOT NULL,
        url TEXT NOT NULL
    )
                   ''')
    conn.commit()

def insertUrl(url):
    conn = sqlite3.connect(db)
    cursor= conn.cursor()
    cursor.execute('''
    INSERT INTO urls (url) VALUES (?)
    ''',(url,))
    conn.commit()
    
def geturl():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM urls')
    urls = cursor.fetchall()
    return urls

def geturldata():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM url_data')
    urls = cursor.fetchall()
    return urls

def getInvertedTable():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inverted')
    urls = cursor.fetchall()
    return urls

def inserturldata(url,data):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO url_data(url,data) VALUES(?,?)
    ''',(url,data))
    conn.commit()
    
    
def invertedTable(word,url):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO inverted(word, url) VALUES(?, ?)
    ''',(word, url))
    conn.commit()
    
    
def findQuery(word):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT url FROM inverted WHERE word = ?
                   ''',(word,))
    urls = cursor.fetchall()
    return urls

def getUrlData(url):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT data FROM url_data WHERE url=(?)''',(url,))
    data = cursor.fetchall()
    return data