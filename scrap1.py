import requests,json
from bs4 import BeautifulSoup
import pandas as pd


innerUrls=[]
urlContainer=[
    "http://www.ekantipur.com/eng",
        "https://thehimalayantimes.com/",
# "http://www.fb.com/",
    "http://kathmandupost.ekantipur.com/",
    "http://annapurnapost.com/"
   # "http://www.nepalipatra.com/"
]

for eachurl in urlContainer:
    request=requests.get(eachurl,headers={'User-Agent': 'Mozilla/5.0'})
    # request=requests.get("https://kec.edu.np/",headers={'User-Agent': 'Mozilla/5.0'})
    if request.status_code==200:
        print('Request was successfull')
        # print(request.content)
        #print(request.text)
        soup=BeautifulSoup(request.content,"lxml",from_encoding='utf-8')
        for script in soup(["script", "style"]):
            script.extract()
            #remove all the scripts and styles

        print(soup.prettify().encode('utf-8'))
        print('title of page',soup.title.text.encode('ascii', errors='replace').decode().replace("?", ""))
        # print('p ',soup.find_all('p'))
        # #print(soup.get_text()) gets all the text including code js
        for eachParagraph in soup.find_all('p'):
            print(eachParagraph.text.encode('ascii', errors='replace').decode().replace("?", ""))
            
        for url in soup.find_all('a'):
            # print(url.text)
            # #get the tags but we need the actual link 
            print(url.get('href'))
            innerUrls.append(url.get('href'))
            # print('all the div ')


        
            
        for eachdiv in soup.find_all('div'):
            print(eachdiv.text.encode('ascii', errors='replace').decode().replace("?", ""))

print('total inner urls are ',len(innerUrls))
for url in innerUrls:
    print(url)

print('program ended success')



