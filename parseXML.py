import xml.sax

class FilmParser(xml.sax.ContentHandler):
	def __init__(self):
		xml.sax.ContentHandler.__init__(self)
		
	def startElement(self, name, attrs):
		print("start element: '" + name + " ' ")
		
	def endElement(self, name):
		print("end element: '" + name + "'")
		
	def charracters(self, content):
		print("characters: '" + content + "'")
		
def main(xmlFile):
	source = open(xmlFile)
	xml.sax.parse(source, FilmParser())
	
if __name__ = "__main__":
	main("films.xml")