import sys
from math import sqrt

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

def bfs(problem, solution):
	initial_state = problem.initial_state
	path_cost = 0

	if problem.goal_test(initial_state)
		return Solution()

	frontier = Queue.Queue(0)
	frontier.put(initial_state)
	solution.frontier_space += 1
	explored = []

	while True:
		if frontier.empty():
			solution.path = None
			return solution
		curr_state = frontier.get()
		explored.append(curr_state)
		solution.explored_space += 1

		number_of_children = problem.get_number_of_children(curr_state)

		for i in range(0, number_of_children):
			child = problem.get_next_state(curr_state, i)
			if child not in explored and child not in frontier:
				if problem.goal_test(child) == True:
					return solution
				frontier.put(child);
				if frontier.length > solution.frontier_space:
					solution.frontier_space = frontier.length

class Node:
	'''
	name = String
	start = int
	stop = int
	adj_nodes = list
	visited = boolean
	'''
	def __init__(self, name, start, stop, adj_nodes=[], visited=False):
		self.name = name
		self.start = start
		self.stop = stop
		self.adj_nodes = adj_nodes
		self.visited = visited

	def addAdjacentNode(node):
		# add a new node to the list of nodes connected to this object
		self.adj_nodes.append(node)

class Sensor(Node):
	'''
	power = int
	'''
	def __init__(self, name, start, stop, power):
		Node.__init__(self, name, start, stop)
		self.power = power

	'''
	t_start = int
	t_stop = int
	'''
	def set_power(t_start, t_stop):
		euclidean_distance = Math.sqrt((self.start - t_start)^2 + (self.stop - t_stop)^2)
		self.power = self.power - euclidean_distance

		if self.power < 0:
			return False
		else:
			return True


class Target(Node):
	def __init__(self, name, start, stop, monitored=False):
		Node.__init__(self, name, start, stop)

class MonitorProblem:
	initial_state
	actions = []

	def goal_test(state):
		# test if the goal has been reached
		# return t/f
		# how do you you do that?
		pass

	def get_next_state():
		pass

	def get_number_of_children():
		pass

class AggregationProblem:
	'''
	nodes = list of Node objects
	initial_state = Node object
	'''
	def __init__(self, nodes, initial_state):
		self.nodes = nodes # a list of all the nodes
		self.initial_state = initial_state # starting node for traversing the graph

	def goal_test(state):
		for n in self.nodes:
			if n.visited = False:
				return False
		return True

	def get_next_state(state, i):
		# given the current node and index where the next child node lives
		# return the next child node
		return state.adj_nodes[i]

	def get_number_of_children(state):
		# given the current state, return the number of nodes attached to it
		return len(state.adj_nodes)

class Solution:
	def __init__(self):
		self.path = [] # array of states that lead to the solved solution (or None)
		self.time = 0 # total number of nodes created
		self.frontier_space = 0 # largest number of nodes in frontier
		self.explored_space = 0 # largest number of nodes in explored
		self.cost = 0 	# for monitor cost = P(sub t)
						# for agg cost = sum of weights in the path to visit all nodes

if __name__ == "__main__":
	main()