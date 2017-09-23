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

	me = Me("Me", 22)
	you = Me("You", 57)
	we = Me("We", 2);
	them = Me("Them", 37)
	q = Queue.PriorityQueue()

	q.put(me)
	q.put(you)
	q.put(we)
	q.put(them)

	print "original priority queue: we, me, them, you"
	for x in q.queue:
		print x.name

	remove(q)

	print "changed priority queue: we, me"
	for x in q.queue:
		print x.name

def remove(q):
	temp = Queue.PriorityQueue()

	print "removing non-front element from queue..."
	while not q.empty():
		x = q.get()
		if x.age < 30:
			temp.put(x)

	while not temp.empty():
		q.put(temp.get())

if __name__ == "__main__":
	main()