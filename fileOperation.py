f = open('myFile.txt', 'r')

firstline = f.readline()
secondline = f.readline()
print(firstline)
print(secondline)

f.close()