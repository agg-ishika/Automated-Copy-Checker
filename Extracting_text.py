#HTML Web Scraping using tool Beautiful Soup 4
#Step-0 Installed- bs4, requests, html5lib

import requests
from bs4 import BeautifulSoup
url = "https://www.geeksforgeeks.org/software-engineering-iterative-waterfall-model/"

#Step-1 Get the HTML
r = requests.get(url) #r=content
htmlContent = r.content
#print(htmlContent)

#Step-2 Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)

#Step-3 HTML tree traversal

#Commonly used type of objects:
# 1. Tag
# 2. Navigable String
# 3. BeautifulSoup
# 4. Comment

title = soup.title
#print(type(soup))
#print(type(title))
#print(type(title.string))



#Get all the paras from page
paras = soup.find_all('p')
print(paras)

#Get all the links from page
anchors = soup.find_all('a')
#print(anchors)

#get all the links from anchor tags
#for link in anchors:
#  print(link.get('href'))

#modified code to get links
#all_links=set()
#for link in anchors:
#  if(link.get('href') != '#'):
#    linkText="https://www.javatpoint.com/python-tutorial" +link.get('href')
#    all_links.add(link)
#    print(linkText)



#get first element of HTML page
#  print(soup.find('p'))

#get classes of any element in HTML page
#print(soup.find('p')['class'])

#find all the elements witha particular class
#print(soup.find_all("p", class_="lead"))

#get the text from the tags/soup
#print(soup.find('p').get_text()) #paras text
#print(soup.get_text()) #full HTML page text



