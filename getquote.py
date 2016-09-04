import urllib.request, re, sys

symbol = sys.argv[0]
url = 'http://finance.google.com/finance?q='
content = urllib.request.urlopen(url+symbol).read()
m = re.search(b'span id="ref.*>(.*)<', content)

if m:
	quote = m.group(1)
else:
	quote = 'no quote for symbol: ' + symbol
	
print(quote)