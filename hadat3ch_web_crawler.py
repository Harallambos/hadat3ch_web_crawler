from urllib.request import urlopen
from lxml import etree

"""
This website crawler uses the tree structure of an XMP file and Xpath expresions 
to search and return all the elemnts we want to retreive from the website.

"""
# Website link that you want to scrap data from
weburl="https://www.imdb.com/search/keyword/?keywords=movie-review"

#File is loaded in the response object
response = urlopen(weburl) 

#Invoke HTMLParser object of lxml package
htmlparser = etree.HTMLParser() 

# Create a document tree using the response and parser
tree = etree.parse(response, htmlparser)

#We can generate Xpath queries using tree
#XPath expressions
titles=tree.xpath('//h3[@class="lister-item-header"]/a/text()') 
reviews=tree.xpath('//div[@class="lister-item-content"]/p[@class=""]/text()')
genre=tree.xpath('//div[@class="lister-item-content"]/p/span[@class="genre"]/text()')
#directors=tree.xpath('//div[@class="lister-item-content"]/p[contains(text(),"Director:")]/a/text()')

"""
Q1. Generate Xpath query to find all the movie reviews, genre and directors from this page.
Hint: Use predicate for browsing to a specific class of a tag as shown above.
You can match a specific word too:
p[contains(text(),"Director:")]

"""

for i,t in enumerate(titles):
    try:
        print(t.strip(),"\n", reviews[i].strip(), "\n", genre[i].strip(), "\n \n \n")
    except:
        continue



