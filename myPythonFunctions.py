import random
import os

def getUserPoint(userNams):
	f = open('userScores.txt', 'r')

	for line in f:
		content = line.split()