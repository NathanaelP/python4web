from urllib.request import urlopen
from html.parser import HTMLParser

urlTEXT = []

#define html parser text
class parserText(HTMLParser):
     
     def handle_data(self, data):
         if data != '\n':
             urlTEXT.append(data)
             
#creat instance of html parser
lParser = parserText()

thisurl = "http://www-rohan.sdsu.edu/~gawron/index.html"
#Feed HTML into parser
lParser.feed(urlopen(thisurl).read())
lParser.close()
for item in urlTEXT:
    print(item)