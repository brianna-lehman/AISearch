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

def bfs(problem):
	node = Node(problem.initial_state, None, None, 0)

	if problem.goal_test(node.state):
		return new Solution(node)

	frontier = new Queue.Queue()
	explored = []

	while True:
		if frontier.empty()
			return None
		node = frontier.get()
		explored.append(node.state)
		node.state.visited = True

		for action in problem.actions(node.state):
			child = child_node(problem, node, action)
			if child.state not in explored and child.state not in frontier:
				if problem.goal_test(child.state):
					return new Solution(child)
					frontier.put(child)

def child_node(problem, parent_node, action):
	child_state = problem.result(parent_node.state, action)
	path_cost = parent.path_cost + problem.step_cost(parent.state, action)
	return new Node(child_state, parent_node, action, path_cost)

class AggState:
	'''
	name = String
	start = int
	stop = int
 adj_edges = list of tuples (Node obj, int)
	visited = boolean
	'''
	def __init__(self, name, start, stop, adj_edges=[], visited=False):
		self.name = name
		self.start = start
		self.stop = stop
		self.adj_edges = adj_edges
		self.visited = visited

	def addAdjacentState(state, weight):
		# add a new node to the list of nodes connected to this object
		self adj_edges.append((state, weight))

class Node:
	def __init__(self, state, parent, action, path_cost):
		self.state = state
		self.parent = parent
		self.action = action
		self.path_cost = path_cost

class AggregationProblem:
	'''
	states = combination of possible states
	initial_state = where the agent starts
	actions = given a state, the set of actions that can be found
	transition_model = a description of each action
	goal_test = given a state, is the goal achieved?
	path_cost = numeric cost to each path
	'''
	def __init__(self, states, initial_state, path_cost):
		self.states = states # a list of all the states
		self.initial_state = initial_state # starting node for traversing the graph
		self.path_cost = path_cost

	def actions(state):
		children = []
		for new_state in state.adj_edges:
			children.append(new_state[0])

		return children

	def result(parent_state, child_state):
		# find the child that's attached to the parent and return it
		for state in parent_state adj_edges:
			if state[0] is child_state:
				return child_state
		return None

	def goal_test(state):
		for n in self.states:
			if n.visited = False:
				return False
		return True

	def path_cost(stateA, stateB):
		for edge in stateA adj_edges:
			if edge[0] is stateB:
				self.path_cost += edge[1]
				break

	# find the weight of the edge between these two states
	def step_cost(stateA, stateB):
		for state in stateA adj_edges:
			if state[0] is stateB:
				return state[1]
		return 0



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