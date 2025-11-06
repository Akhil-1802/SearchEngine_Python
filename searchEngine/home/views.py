from django.shortcuts import render
from .db import createtables,findQuery,geturl,inserturldata,geturldata,invertedTable,getInvertedTable,getUrlData,insertUrl
import re
import requests
import trafilatura
from django.http import JsonResponse
# Create your views here.
seed_urls = [
    "https://www.geeksforgeeks.org/",
    "https://www.w3schools.com/",
    "https://developer.mozilla.org/",
    "https://stackoverflow.com/",
    "https://www.freecodecamp.org/",
    "https://realpython.com/",
    "https://www.djangoproject.com/",
    "https://flask.palletsprojects.com/",
    "https://react.dev/",
    "https://nodejs.org/",
    "https://expressjs.com/",
    "https://nextjs.org/",
    "https://www.mongodb.com/",
    "https://dev.to/",
    "https://www.learncpp.com/",
    "https://www.tutorialspoint.com/",
    "https://www.codecademy.com/",
    "https://roadmap.sh/",
    "https://www.kaggle.com/",
    "https://www.python.org/",
    "https://www.nasa.gov/",
    "https://www.noaa.gov/",
    "https://www.nationalgeographic.com/",
    "https://www.scientificamerican.com/",
    "https://www.britannica.com/",
    "https://www.space.com/",
    "https://www.newscientist.com/",
    "https://www.science.org/",
    "https://ocw.mit.edu/",
    "https://www.edx.org/",
    "https://www.coursera.org/",
    "https://www.khanacademy.org/",
    "https://www.openai.com/research/",
    "https://www.futurelearn.com/",
    "https://www.udemy.com/",
    "https://www.bbc.com/",
    "https://www.cnn.com/",
    "https://www.reuters.com/",
    "https://www.nytimes.com/",
    "https://www.aljazeera.com/",
    "https://indianexpress.com/",
    "https://www.hindustantimes.com/",
    "https://www.thehindu.com/",
    "https://timesofindia.indiatimes.com/",
    "https://www.deccanherald.com/",
    "https://www.livemint.com/",
    "https://www.economist.com/",
    "https://techcrunch.com/",
    "https://www.wired.com/",
    "https://www.forbes.com/",
    "https://dribbble.com/",
    "https://www.behance.net/",
    "https://www.awwwards.com/",
    "https://www.canva.com/",
    "https://www.figma.com/",
    "https://uxdesign.cc/",
    "https://99designs.com/",
    "https://www.creativebloq.com/",
    "https://www.adobe.com/",
    "https://www.deviantart.com/",
    "https://www.mit.edu/",
    "https://www.stanford.edu/",
    "https://www.harvard.edu/",
    "https://www.ox.ac.uk/",
    "https://www.cam.ac.uk/",
    "https://www.iitb.ac.in/",
    "https://www.iitm.ac.in/",
    "https://www.iisc.ac.in/",
    "https://www.caltech.edu/",
    "https://www.berkeley.edu/",
    "https://www.google.com/",
    "https://www.microsoft.com/",
    "https://about.meta.com/",
    "https://www.apple.com/",
    "https://aws.amazon.com/",
    "https://cloud.google.com/",
    "https://azure.microsoft.com/",
    "https://www.ibm.com/",
    "https://www.oracle.com/",
    "https://www.salesforce.com/",
    "https://www.adobe.com/",
    "https://www.intel.com/",
    "https://www.tesla.com/",
    "https://www.samsung.com/",
    "https://www.nvidia.com/",
    "https://github.com/",
    "https://gitlab.com/",
    "https://www.reddit.com/",
    "https://www.wikipedia.org/",
    "https://www.quora.com/",
    "https://medium.com/",
    "https://news.ycombinator.com/",
    "https://www.producthunt.com/",
    "https://www.pinterest.com/",
    "https://www.linkedin.com/",
    "https://twitter.com/",
    "https://x.com/",
    "https://www.instagram.com/",
    "https://www.tumblr.com/",
    "https://www.goodreads.com/"
]


def index(request):
    createtables()
    # For inserting url in the database
    # for url in seed_urls:
    #     insertUrl(url)
    urls = geturl()
    # For inserting data in url_data
    # for url in urls:
    #     u = url[1]
    #     print(u)
    #     response = requests.get(url=u) 
    #     # Check the response status and print data
    #     if response.status_code == 200:
    #         text = trafilatura.extract(response.text, include_comments=False, include_tables=False)
    #         if text:  # Only insert if text is not None
    #             inserturldata(u,text)
    #     else:
    #         print(f"Failed with status code: {response.status_code}")
    
    url_data = geturldata()
    #For making inverted table
    # for item in url_data:
    #     url = item[1]
    #     url_data = item[2]
    #     if url_data:  # Only process if data exists
    #         words = re.findall(r'\b[a-zA-Z]{2,}\b',url_data.lower())
    #         for word in set(words):
    #             invertedTable(word,url)
    return render(request, 'index.html')


def search(request,word):
    data = {}
    urls = findQuery(word)
    for url in urls:
        url_data = getUrlData(url[0])
        data[url[0]] = url_data[0][0]
    return render(request,'search.html',{"result":data,"query":word})

def text(request,url):
    print(url)
    url_data = getUrlData(url)
    data = url_data[0][0]
    
    return render(request,'text.html',{"url":url,"data":data})
    

