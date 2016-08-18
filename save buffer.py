inputfile = open('myfile.txt', 'r')
outputfile = open('myoutputfile', "w")

msg = inputfile.read(10)

while len(msg):
	outputfile.write(msg)
	msg = inputfile.read(10)

inputfile.close()
outputfile.close()