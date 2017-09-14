import sys

def main():
	problem_filename = sys.argv[1]

class Node:
	def __init__(self, name, start, stop):
		self.name = name
		self.start = start
		self.stop = stop

class Sensor(Node):
	def __init__(self, name, start, stop, power):
		Node.__init__(self, name, start, stop)
		self.power = power

class Target(Node):
	def __init__(self, name, start, stop, monitored=False):
		Node.__init__(self, name, start, stop)
		self.monitored = monitored

if __name__ == "__main__":
	main()