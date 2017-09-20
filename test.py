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
	them = Me("Them", 37)
	q = Queue.PriorityQueue()
	l = [me, you, we]

	q.put(me)
	q.put(you)
	q.put(we)

	if me in q.queue:
		print ("Object in queue")
	if me in l:
		print ("Object in list")
	if them not in q.queue:
		print ("Object not in queue")
	if them not in l:
		print ("Object not in list")
	if them not in q.queue:
		print ("Object is not in queue")
	if them not in l:
		print ("Object is not in list")


if __name__ == "__main__":
	main()