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