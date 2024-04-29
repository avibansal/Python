import bs4
from bs4 import BeautifulSoup
import requests
#Beautiful Soup is a python library for pulling data out of HTML
#and XML files.It works with your favorite parser to provide
# idiomatic ways of navigation,searching and modifying the parse tree
# It commonly saves programmers hours of work
  
contents=requests.get("https://en.wikipedia.org/wiki/India").text
#print(contents)

soup=BeautifulSoup(contents,'lxml')
#lxml is the parser
#html can also be used but lxml is faster

'''
count=0
for tag in soup.findAll(True):
    count+=1
    #print(tag)
print(count)
'''

# print(soup.title)
# print(soup.body)

#FETCH ALL IMAGE TAGS
'''
for img in soup.findAll("img"):
    print(img['src'])
'''

#EXTRACT TABLE FROM HTML PAGE
Link = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_population"
data=requests.get(Link).text

soup1=BeautifulSoup(data,"lxml")

# print(soup1.title)

# for tbl in soup1.findAll("table"):
#     print(tbl)

#PRINT ALL TAGS NAME
#print(set([tag.name for tag in soup1.findAll(True)]))

for tag in soup1.findAll(True):
    print(tag.name)