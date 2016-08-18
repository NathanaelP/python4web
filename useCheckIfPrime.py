import sys
#this line adds my personal modules to the system path directory for python
if 'C:\\Users\natha\Documents\Python Web\pymod' not in sys.path:
	sys.path.append('C:\\Users\natha\Documents\Python Web\pymod')
import prime.py

answer = prime.checkIfPrime(13)

print(answer)