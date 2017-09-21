import Queue
import sys

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
	filename = sys.argv[1]
	search = sys.argv[2]

	file = open(filename, 'r')

	problem = file.readline()

	readFile(file)

	file.close()

	me = Me("Bri", 22)
	you = Me("You", 57)
	we = Me("We", 2);
	them = Me("Them", 37)
	q = Queue.PriorityQueue()
	l = [me, you, we]

	q.put(me)
	q.put(you)
	q.put(we)

	print q

def readFile(file):
	listOfStates = []

	stringOfStates = file.readline().strip().replace(",", " ").strip('[]')
	listOfStateStrings = stringOfStates.split('  ')
	print stringOfStates

	for x in listOfStateStrings:
		print x

	for stateString in listOfStateStrings:
		stateString = stateString.strip('()')
		state = stateString.split(' ')
		aggState = AggState(state[0].strip(""), int(state[1]), int(state[2]))
		listOfStates.append(aggState)

	for line in file:
		print line

if __name__ == "__main__":
	main()