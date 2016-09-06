import urllib
import HTMLParser

urlTEXT = []

#define html parser text
class parserText(HTMLParser.HTMLParser):
     
     def handle_data(self, data):
         if data != '\n':
             urlTEXT.append(data)
             
#creat instance of html parser
lParser = parserText()

thisurl = "http://www-rohan.sdsu.edu/~gawron/index.html"
#Feed HTML into parser
lParser.feed(urllib.urlopen(thisurl).read())
lParser.close()
for item in urlTEXT:
    print(item)