import urllib, htmllib, formatter

website = urllib.urlopen("http://www.profmcmillan.com")
data = website.read()
website.close()
format = formatter.AbstractFormatter(formatter.NullWriter)

ptext = htmllib.HTMLParser(format)
ptext.feed(data)
print(ptext.anchorlist)