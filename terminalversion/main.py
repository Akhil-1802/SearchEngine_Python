import requests
import trafilatura
import re
from collections import defaultdict
from db import createtables,geturl,inserturldata,invertedTable,findQuery,getUrlData

seed_urls = [
    "https://www.python.org/",
    "https://docs.python.org/3/",
    "https://realpython.com/",
    "https://www.geeksforgeeks.org/python-programming-language/",
    "https://www.w3schools.com/python/",
    "https://www.geeksforgeeks.org/",
    "https://www.tutorialspoint.com/index.htm",
    "https://www.programiz.com/",
    "https://www.freecodecamp.org/news/",
    "https://developer.mozilla.org/",
    "https://www.stackoverflow.com/",
    "https://towardsdatascience.com/",
    "https://medium.com/topic/programming",
    "https://www.kdnuggets.com/",
    "https://cp-algorithms.com/",
    "https://www.bigocheatsheet.com/",
    "https://visualgo.net/en",
    "https://github.com/",
    "https://docs.djangoproject.com/",
    "https://flask.palletsprojects.com/",
    "https://nodejs.org/en/docs",
    "https://react.dev/"
]

url_data = {}
def build_index(pages):
    index = defaultdict(set)
    for url,text in pages.items():
        words = re.findall(r'\b[a-zA-Z]{2,}\b',text.lower())
        for word in set(words):
            invertedTable(word,url)
            index[word].add(url)
    return index

def fetch_url(data):
    for url in data:
        response = requests.get(url=url) 
        # Check the response status and print data
        if response.status_code == 200:
            text = extract_text(response.text)
            url_data[url] = text
            inserturldata(url,text)
        else:
            print(f"Failed with status code: {response.status_code}")

def extract_text(html):
    text = trafilatura.extract(html, include_comments=False, include_tables=False)
    return text
    

        

def search_query(query,index):
    text = query.lower().split()
    results = [index.get(word) for word in text]
    if not results:
        print("no matching URL")
        return
    return results

def main():
    user_enter_data = True
    createtables() #Creation of table
    fetch_url(seed_urls) #Fetching Data of URL
    index = build_index(url_data) #Inverted Index building
    print("Search Engine is Working")
    while user_enter_data:
        query = input("Enter the query: ") #Taking the first query from the user
        result = findQuery(query.lower().split()[0]) #Finding the query in the database if the data is available in the database from the specific word
        for url in result: #for each url we are getting the data from the table
            print(getUrlData(url[0])[0][0])
        
        user_input = input("Do you want to continue? (yes/no): ")
        if(user_input.lower() == "no"):
            user_enter_data = False
            print("Search Engine is closed!")
        
    

main()