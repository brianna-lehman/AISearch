import sys
import Queue
import pdb
import time
from math import sqrt

''' PROCESSING FILES '''

def main():
	problem_filename = sys.argv[1]
	search_algo = sys.argv[2]
	file = open(problem_filename, 'r')
	problem = file.readline().rstrip()

	if problem == "monitor":
		monitor(file, search_algo)
	elif problem == "aggregation":
		aggregation(file, search_algo)

'''def monitor(file, algo):
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

	if len(listOfTargetStrings) > len(listOfSensors):
		write(Solution()) # prints the data from the Solution object to the screen and to a file
		sys.exit()
	else:
		for targetString in listOfTargetStrings:
			targetString = targetString.strip('()')
			target_list = targetString.split(' ')
			targetState = TargetState(target_list[0].strip(""), int(target_list[1]), int(sensor_list[2]))

			for sensor in listOfSensors:
				sensor.addAdjacentState(targetState)'''

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
		aggState = AggState(state[0].strip('""'), int(state[1]), int(state[2]))
		listOfStates.append(aggState)

	for line in file:
		state_A = None
		state_B = None

		edge = line.strip().strip('()').replace(',', ' ').split("  ")
		stateA_name = edge[0].replace('"', '')
		stateB_name = edge[1].replace('"', '')
		weight = int(edge[2])
		for s in listOfStates:
			if s.name == stateA_name:
				global stateA
				stateA = s
			elif s.name == stateB_name:
				global stateB
				stateB = s
			else:
				pass

		stateA.addAdjacentState(stateB, weight)
		stateB.addAdjacentState(stateA, weight)

	problem = AggProblem(listOfStates, listOfStates[0], 0)
	solution = search(algo, problem)

	# print fields from solution to screen
	# write fields to file
	write(solution)

def write(solution):
	for x in solution.path:
		print "Path %s" %x.state.name

	print "Time %d" %solution.time
	print "Frontier space %d" %solution.frontier_space
	print "Explored space %d" %solution.explored_space
	print "Path cost %d" %solution.path_cost

'''running the appropriate algorithm and returning the Solution object'''
def search(algo, problem):
	if algo == "bfs":
		return bfs(problem)
	elif algo == "unicost":
		return unicost(problem)
	elif algo == "iddfs":
		return iddfs(problem)
	elif algo == "greedy":
		return greedy()
	elif algo == "Astar":
		return astar()
	else:
		return None


''' SEARCHING ALGORITHMS '''

'''unfinished - will aways return None'''
def bfs(problem):
	node = Node(problem.initial_state, None, None, 0)
	solution = Solution()
	solution.time += 1

	if problem.goal_test(node):
		return solution

	frontier = Queue.Queue()
	frontier.put(node)
	explored = []

	while True:
		if frontier.empty():
			return solution

		# pdb.set_trace()
		node = frontier.get()
		explored.append(node.state)

		node.state.visited = True
		solution.explored_space += 1
		solution.path.append(node)
		if node.parent is not None:
			solution.path_cost += problem.step_cost(node.parent.state, node.state)

		for action in problem.actions(node.state):
			child = node.child_node(problem, action)
			solution.time += 1

			if child.state not in explored and child not in frontier.queue:
				if problem.goal_test(child):
					return solution
				frontier.put(child)
				if frontier.qsize() > solution.frontier_space:
					solution.frontier_space = frontier.qsize()

'''unfinished - how to take an element out of a priority queue (not at the front)'''
def unicost(problem):
	node = Node(problem.initial_state, None, None, 0)
	solution = Solution()
	solution.time += 1

	frontier = Queue.PriorityQueue()
	frontier.put(node)

	solution.frontier_space += 1

	explored = []

	while True:

		if frontier.empty():
			return solution.setSolutionMetrics(None)

		node = frontier.get()

		if problem.goal_test(node):
			return solution.setSolutionMetrics(node)

		explored.append(node.state)

		solution.explored_space += 1

		for action in problem.actions(node.state):
			child = node.child_node(problem, action)
			solution.time += 1

			if child.state not in explored and child not in frontier.queue:
				#global frontier
				frontier.put(child)
			elif child.stateInQueueWithHigherCost(frontier):
				deletedNode = child.removeHigherNodeFromPQ(frontier)
				frontier.put(child)

			if frontier.qsize() > solution.frontier_space:
				solution.frontier_space = frontier.qsize()

def iddfs(problem):
	for depth in xrange(sys.maxint):
		print "inside iddfs %d" %depth
		solution = depth_limited_search(problem, depth)
		if solution != 'cutoff':
			return solution

def depth_limited_search(problem, limit):
	print "inside depth_limited_search %d" %limit
	solution = Solution()
	solution.time += 1
	return recursive_dls(Node(problem.initial_state), problem, solution, limit)

def recursive_dls(node, problem, solution, limit):
	print "inside recursive dls %d" %limit
	if problem.goal_test(node):
		print "At goal state"
		return solution.setSolutionMetrics(node)
	elif limit == 0:
		print "At cutoff"
		return 'cutoff'
	else:
		atCutoff = False
		for action in problem.actions(node.state):
			child = node.child_node(problem, action)
			solution.time += 1
			result = recursive_dls(child, problem, solution, limit-1)
			if result == 'cutoff':
				atCutoff = True
			elif result is not None:
				return result
		if atCutoff == True:
			return 'cutoff'
		else:
			return None


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

	'''given a node and a priority queue
	if the state of the node is in the pq with a higher cost return true
	else return false'''
	def stateInQueueWithHigherCost(self, pq):
		for pq_node in pq.queue:
			if self.state is pq_node.state:
				if self.path_cost < pq_node.path_cost:
					return True
		return False

	def removeHigherNodeFromPQ(self, pq):
		temp = Queue.PriorityQueue()
		while not pq.empty():
			pq_node = pq.get()
			if self.state is not pq_node.state:
				temp.put(pq_node)
			else:
				deletedNode = pq_node
		while not temp.empty():
			pq.put(temp.get())

		return deletedNode

class Solution:
	def __init__(self):
		self.path = [] # array of states that lead to the solved solution (or None)
		self.time = 0 # total number of nodes created
		self.frontier_space = 0 # largest number of nodes in frontier
		self.explored_space = 0 # largest number of nodes in explored
		self.path_cost = 0 	# for monitor cost = P(sub t)
						# for agg cost = sum of weights in the path to visit all nodes

	def setSolutionMetrics(self, node):
		solution_path = []

		curr = node

		while curr is not None:
			self.path.append(curr.state)
			curr = curr.parent

		if node is not None:
			self.path_cost = node.path_cost

		return self

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

	''' given the state, what states can this state go to? '''
	def actions(self, state):
		pass

	''' a state attaches itself to a new state
		if the original state is a sensor:
			state.power = state.power - euclideanDistance between sensor(state) and target(action)
		if the original state is a target:
			action.power = action.power - euclideanDistance between sensor(action) and target(state)'''
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
	def __init__(self, name, start, stop, edges={}, visited=False):
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
			children.append(new_state)

		return children

	# given the parent state and the child that needs returned
	# find if the child is attached to the parent and return it
	def result(self, parent_state, child_state):
		if child_state in parent_state.edges.keys():
			return child_state
		return None

	# return false if at least one of the states hasn't been visited
	# true otherwise
	def goal_test(self, node):
		curr = node

		while curr is not None:
			curr.state.visited = True
			curr = curr.parent

		for n in self.states:
			if n.visited == False:
				return False

		return True

	# currently uncalled
	def path_cost(self, stateA, stateB):
		if stateB in edge.keys():
			self.path_cost += edge[stateB]

	# find the weight of the edge between these two states
	def step_cost(self, stateA, stateB):
		#pdb.set_trace()

		if stateB in stateA.edges.keys():
			return stateA.edges[stateB]
		return 0

if __name__ == "__main__":
	main()