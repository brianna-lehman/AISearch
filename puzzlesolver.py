import sys

def main():
	problem_filename = sys.argv[1]
	search_algo = sys.argv[2]
	# open this file
	# read in the first line (problem)
	if problem is "monitor":
		monitor(file, search_algo)
	elif problem is "aggregation":
		aggregation(file, search_algo);

def monitor(file, search_algo):
	# read in the list of sensors
	# make an array of Sensor objects

	# read in the list of targets
	# make an array of Target objects

	# for every Sensor in the array
		# do a search to find the nearest target?
		# what does the search return?
			# t/f if the sensor finds a target
			# or the target that the sensor is monitoring

def aggregation(file, search_algo):
	pass

def search(algo):
	if algo is "bfs":
		return bfs(problem)
	elif algo is "unicost":
		return unicost(problem)
	elif algo is "iddfs":
		return iddfs(problem)
	elif algo is "greedy":
		return greedy()
	elif algo is "Astar":
		return astar()
	else:
		return None

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

class Problem:
	initial_state
	actions = []

	def goal_test(state):
		# test if the goal has been reached
		# how do you you do that?

if __name__ == "__main__":
	main()