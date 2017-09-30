import Queue
import sys
import pdb
import re

class State:
	def __init__(self, name, start, stop, edges):
		self.name = name
		self.start = start
		self.stop = stop
		self.edges = edges

def main():
	sensors = [State("S_"+str(x), x, x*2, {}) for x in range(10)]

	for s in sensors:
		print "%s %d %d" %(s.name, s.start, s.stop)
	print ""

	targets = [State("T_"+str(x), x+2, x**2, {}) for x in range(5)]

	for t in targets:
		print "%s %d %d" %(t.name, t.start, t.stop)
	print ""

	for s in sensors:
		print "In %s" %s.name
		print id(s.edges)
		for t in targets:
			s.edges[t] = t.stop - s.start
			print "\tAdding %s: %d" %(t.name, s.edges[t])
			print "\tCurrent edge array: "
			for k, v in s.edges.items():
				print "\t\t%s: %d" %(k.name, v)
			print ""

	for t in targets:
		print "In %s" %t.name
		for s in sensors:
			t.edges[s] = t.stop - s.start
			print "\tAdding %s: %d" %(s.name, t.edges[s])
			print "\tCurrent edge array: "
			for k, v in t.edges.items():
				print "\t\t%s: %d" %(k.name, v)

if __name__ == "__main__":
	main()