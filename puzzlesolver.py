import sys
import Queue
from math import sqrt

''' PROCESSING FILES '''

def main():
	problem_filename = sys.argv[1]
	search_algo = sys.argv[2]
	file = open(problem_filename, 'r')
	problem = file.readline().rstrip()

	if problem is "monitor":
		monitor(file, search_algo)
	elif problem is "aggregation":
		aggregation(file, search_algo)

def monitor(file, algo):
	listOfSensors = []

	stringOfSensors = file.readline().strip().replace(',', ' ').strip('[]')
	listOfSensorStrings = stringOfSensors.split('  ')

	for sensorString in listOfSensorStrings:
		sensorString = sensorString.strip('()')
		sensor_list = sensorString.split(' ')
		sensorState = SensorState(sensor_list[0].strip(""), int(sensor_list[1]), int(sensor_list[2]), int(sensor_list[3]))
		listOfSensors.append(sensorState)

	stringOfTargets = file.readline().strip().replace(',', ' ').strip('[]')
	listOfTargetStrings = stringOfTargets.split('  ')

	for targetString in listOfTargetStrings:
		targetString = targetString.strip('()')
		target_list = targetString.split(' ')
		targetState = TargetState(target_list[0].strip(""), int(target_list[1]), int(sensor_list[2]))

		for sensor in listOfSensors:
			sensor.addAdjacentState(targetState)


'''unfinished - processing the file and running the search to find the solution'''
def aggregation(file, algo):
	listOfStates = []

	stringOfStates = file.readline().strip()
	stringOfStates = stringOfStates.replace(',', ' ')
	stringOfStates = stringOfStates.strip('[]')
	listOfStateStrings = stringOfStates.split('  ')

	for stateString in listOfStateStrings:
		stateString = stateString.strip('()')
		state = stateString.split(' ')
		aggState = AggState(state[0].strip(""), int(state[1]), int(state[2]))
		listOfStates.append(aggState)

	for line in file:
		edge = line.strip().strip('()').split(" ")
		stateA_name = edge[0].strip('""')
		stateB_name = edge[1].strip('""')
		weight = int(edge[2])
		for s in listOfStates:
			if s.name is stateA_name:
				stateA = s
			if s.name is stateB_name:
				stateB = s

		if stateA is None or stateB is None:
			print "Error - one of the states doesn't exist"
		else:
			stateA.addAdjacentState(stateB, weight)
			stateB.addAdjacentState(stateA, weight)

	problem = AggProblem(listOfStates, listOfStates[0], 0)
	solution = search(problem)

	# print fields from solution to screen
	# write fields to file

'''running the appropriate algorithm and returning the Solution object'''
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


''' SEARCHING ALGORITHMS '''

'''unfinished - will aways return None'''
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
			return Solution()
		node = frontier.get()
		explored.append(node.state)

		node.state.visited = True
		solution.path.append(node.state)
		solution.explored_space += 1

		for action in problem.actions(node.state):
			child = node.child_node(problem, action)

			solution.time += 1

			if child.state not in explored and child not in frontier.queue:
				solution.path_cost += child.path_cost
				if problem.goal_test(child.state):
					solution.path.append(child.state)
					return solution
				frontier.put(child)
				if len(frontier) > solution.frontier_space:
					solution.frontier_space = len(frontier)

'''unfinished - how to take an element out of a priority queue (not at the front)'''
def unicost(problem):
	node = Node(problem.initial_state, None, None, 0)
	solution = Solution()
	solution.time += 1

	frontier = Queue.PriorityQueue()
	frontier.put(node)
	frontier_set = [node.state]
	explored = []

	while True:
		if frontier.empty()
			return Solution()

		node = frontier.get()
		frontier_set.remove(node.state)

		if problem.goal_test(node.state):
			return solution

		explored.append(node.state)

		for action in problem.actions(node.state):
			child = node.child_node(problem, action)
			solution.time += 1

			if child.state not in explored and child not in frontier.queue:
				frontier.put(child)
				frontier_set.append(child.state)
			elif child.state in frontier_set:
				for node in frontier.queue:
					if child.state is node.state and node.path_cost > child.path_cost:
						# take node out of frontier priority queue
						frontier.put(child)
						frontier_set.append(child.state)

def iddfs(problem):
	for depth in xrange(sys.maxint):
		solution = depth_limited_search(problem, depth)
		if solution is not 'cutoff':
			return solution

def depth_limited_search(problem, limit):
	return recursive_dls(Node(problem.initial_state), problem, Solution(), limit)

def recursive_dls(node, problem, solution, limit):
	if problem.goal_test(node.state):
		return solution
	elif limit == 0:
		return 'cutoff'
	else:
		atCutoff = False


''' STANDARD CLASS DEFINITIONS '''

class State:
	def __init__(self, name, start, stop):
		self.name = name
		self.start = start
		self.stop = stop

class Node:
	def __init__(self, state, parent=None, action=None, path_cost=0):
		self.state = state
		self.parent = parent
		self.action = action
		self.path_cost = path_cost

	def __cmp__(self, other):
		return cmp(self.path_cost, other.path_cost)

	def child_node(self, problem, action):
		child_state = problem.result(self.state, action)
		path_cost = self.path_cost + problem.step_cost(self.state, action)
		return Node(child_state, self, action, path_cost)

class Solution:
	def __init__(self):
		self.path = [] # array of states that lead to the solved solution (or None)
		self.time = 0 # total number of nodes created
		self.frontier_space = 0 # largest number of nodes in frontier
		self.explored_space = 0 # largest number of nodes in explored
		self.cost = 0 	# for monitor cost = P(sub t)
						# for agg cost = sum of weights in the path to visit all nodes

''' PROBLEM SPECIFIC CLASS DEFINITIONS '''

''' MONITOR PROBLEM '''
class SensorState(State):
	def __init__(self, name, start, stop, power=0, edges=[]):
		State.__init__(self, name, start, stop)
		self.power = power
		self.edges = edges

	def addAdjacentState(self, target):
		self.edges.update(target)

class TargetState(State):
	def __init__(self, name, start, stop, visited=False):
		State.__init__(self, name, start, stop)
		self.visited = visited

class MonitorProblem():
	def __init__(self, states, initial_state, path_cost=0):
		self.states = states
		self.initial_state = initial_state
		self.path_cost = path_cost

	''''''
	def actions(self, state):
		pass

	def result(self, state, action):
		pass

	def goal_test(self, state):
		pass

	def path_cost(self, stateA, stateB):
		pass

	def step_cost(self, sensor, target):
		pass

''' AGGREGATION PROBLEM '''
class AggState(State):
	def __init__(self, name, start, stop, edges=[], visited=False):
		State.__init__(self, name, start, stop)
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