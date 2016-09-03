import urllib, htmllib, formatter, sys

website = urllib.urlopen("http://www.profmcmillan.com")
data = website.read()
website.close()
format = formatter.AbstractFormatter(formatter.NullWrtiter())

ptext = htmllib.HTMLParser(format)
ptext.feet(data)
print(ptext.anchorlist)