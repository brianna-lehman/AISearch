import Queue
import sys
import pdb
import re

class Me:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __cmp__(self, other):
		return cmp(self.age, other.age)

class AggState:
	def __init__(self, name, start, stop):
		self.name = name
		self.start = start
		self.stop = stop

def main():
	s = "[('S_1',1,1,350),('S_2',2,3,300),('S_3',1,5,280),('S_4',1,4,250),('S_5',4,0,250),('S_6',5,0,240),('S_7',9,3,220)]"
	print type(s)
	s = s.strip('[]')
	print s
	print re.split(r',(?!(?:[^(]*\([^)]*\))*[^()]*\))', s)

if __name__ == "__main__":
	main()