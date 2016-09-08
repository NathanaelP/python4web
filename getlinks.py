<<<<<<< HEAD
import urllib, htmllib, formatter

website = urllib.urlopen("http://www.profmcmillan.com")
data = website.read()
website.close()
format = formatter.AbstractFormatter(formatter.NullWriter)

ptext = htmllib.HTMLParser(format)
ptext.feed(data)
print(ptext.anchorlist)
||||||| merged common ancestors
=======
<<<<<<< HEAD
import urllib, htmllib, formatter, sys
=======
import urllib, http, formatter
>>>>>>> 7638b311e7759361057f919cf3c0700e6fa128ea

website = urllib.URLOpener("http://www.profmcmillan.com")
data = website.read()
website.close()
format = formatter.AbstractFormatter(formatter.NullWrtiter())

ptext = htmllib.HTMLParser(format)
ptext.feet(data)
print(ptext.anchorlist)
>>>>>>> 802c9662feca1fb5fbecb9b769a4e694340c24cb
