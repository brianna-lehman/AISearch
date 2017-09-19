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

def aggregation(file, algo):
	'''read in the second line of the file
	for every element in the returned list
		create an AggState(name, start, stop)
		put the new state object in a list
	for every line until EOF
		create a list out of the line [nameA, nameB, weight] <- states
		find the state in the list w/ name = nameA <- stateA
		find the state in the list w/ name = nameB <- stateB
		stateA.addAdjacentState(stateB, weight)
		stateB.addAdjacentState(stateA, weight)

	problem = AggProblem(states, state[0], 0)
	solution = search(algo, problem)
	print the date from solution to the screen
	put the date from solution into a file'''

def search(algo, problem):
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
	solution = Solution()
	solution.time += 1

	if problem.goal_test(node.state):
		return solution

	frontier = Queue.Queue()
	frontier.put(node)
	explored = []

	while True:
		if frontier.empty()
			return None
		node = frontier.get()
		explored.append(node.state)

		node.state.visited = True
		solution.path.append(node.state)
		solution.explored_space += 1

		for action in problem.actions(node.state):
			child = child_node(problem, node, action)

			solution.time += 1

			if child.state not in explored and child.state not in frontier:
				solution.path_cost += child.path_cost
				if problem.goal_test(child.state):
					solution.path.append(child.state)
					return solution
				frontier.put(child)
				if len(frontier) > solution.frontier_space:
					solution.frontier_space = len(frontier)

def unicost(problem):
	node = Node(problem.initial_state, None, None, 0)
	solution = Solution()
	solution.time += 1

	frontier = Queue.PriorityQueue()
	explored = []

def child_node(problem, parent_node, action):
	child_state = problem.result(parent_node.state, action)
	path_cost = parent.path_cost + problem.step_cost(parent.state, action)
	return Node(child_state, parent_node, action, path_cost)

class Node:
	def __init__(self, state, parent, action, path_cost):
		self.state = state
		self.parent = parent
		self.action = action
		self.path_cost = path_cost

	def __cmp__(self, other):
		return cmp(self.path_cost, other.path_cost)

class Solution:
	def __init__(self):
		self.path = [] # array of states that lead to the solved solution (or None)
		self.time = 0 # total number of nodes created
		self.frontier_space = 0 # largest number of nodes in frontier
		self.explored_space = 0 # largest number of nodes in explored
		self.cost = 0 	# for monitor cost = P(sub t)
						# for agg cost = sum of weights in the path to visit all nodes

class AggState:
	def __init__(self, name, start, stop, edges=[], visited=False):
		self.name = name
		self.start = start
		self.stop = stop
		self.edges = edges
		self.visited = visited

	def addAdjacentState(self, state, weight):
		# add a new node to the list of nodes connected to this object
		self.edges.update({state: weight})

class AggProblem:
	def __init__(self, states, initial_state, path_cost=0):
		self.states = states # a list of all the states
		self.initial_state = initial_state # starting node for traversing the graph
		self.path_cost = path_cost

	# given a state, return a list of all the states attached to it
	def actions(self, state):
		children = []
		for new_state in state.edges:
			children.append(new_state[0])

		return children

	# given the parent state and the child that needs returned
	# find if the child is attached to the parent and return it
	def result(self, parent_state, child_state):
		if child_state in parent_state.edges.keys():
			return child_state
		return None

	# return false if at least one of the states hasn't been visited
	# true otherwise
	def goal_test(self, state):
		for n in self.states:
			if n.visited = False:
				return False
		return True

	# currently uncalled
	def path_cost(self, stateA, stateB):
		if stateB in edge.keys():
			self.path_cost += edge[stateB]
			break

	# find the weight of the edge between these two states
	def step_cost(self, stateA, stateB):
		if stateB in stateA.edges.keys():
			return stateA.edges[stateB]
		return 0

if __name__ == "__main__":
	main()