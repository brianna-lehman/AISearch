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
	# make a dictionary of Sensor objects [Sensor_name: Sensor object]

	# read in the list of targets
	# make a dictionary of Target objects

	# for every Sensor in the array
		# do a search to find the nearest target?
		# what does the search return?
			# t/f if the sensor finds a target
			# or the target that the sensor is monitoring

def aggregation(file, search_algo):
	# read in list of nodes
	# make a dictionary of Node objects [Node_name: Node object]

	# for every line until EOF
		# get first node name
		# get the corresponding Node object based on name
		# get second node name
		# get corresponding Node object based on name
		# get weight
		# firstNode.addAdjacentNode((secondNode, weight))
		# secondNode.addAdjacentNode((firstNode, weight))

	# what is the start state?

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
	def __init__(self, name, start, stop, adj_nodes=[]):
		self.name = name
		self.start = start
		self.stop = stop
		self.adj_nodes = adj_nodes

	def addAdjacentNode(edge):
		self.adj_nodes.append(edge)

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