import Queue
import sys

class Me:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __cmp__(self, other):
		return cmp(self.age, other.age)

def main():
	filename = sys.argv[1]
	search = sys.argv[2]

	file = open(filename, 'r')

	problem = file.readline()

	print(problem)
	print(problem.rstrip())
	print(search)

	file.close()

	me = Me("Bri", 22)
	you = Me("You", 57)
	we = Me("We", 2);
	q = Queue.PriorityQueue()

	q.put(me)
	q.put(you)
	q.put(we)

	while not q.empty():
		x = q.get()
		print(x.name, x.age)

if __name__ == "__main__":
	main()