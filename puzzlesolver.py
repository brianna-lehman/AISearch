import sys
import Queue
import pdb
import time
import re
from math import sqrt

''' PROCESSING FILES '''

def main():
	problem_filename = sys.argv[1]
	search_algo = sys.argv[2]
	file = open(problem_filename, 'r')
	problem = file.readline().rstrip()

	if problem == "monitor" or problem == "Monitor":
		monitor(file, search_algo)
	elif problem == "aggregation" or problem == "Aggregation":
		aggregation(file, search_algo)

def monitor(file, algo):
	listOfSensors = []
	listOfTargets = []

	stringOfSensors = file.readline().strip().strip('[]')
	listOfSensorStrings = re.split(r',(?!(?:[^(]*\([^)]*\))*[^()]*\))', stringOfSensors)
	# pdb.set_trace()
	for sensorString in listOfSensorStrings:
		sensorString = sensorString.strip('()')
		sensor_list = sensorString.split(',')
		sensorState = MonitorState(sensor_list[0].strip('""'), int(sensor_list[1]), int(sensor_list[2]), int(sensor_list[3]), {})
		listOfSensors.append(sensorState)

	stringOfTargets = file.readline().strip().strip('[]')
	listOfTargetStrings = re.split(r',(?!(?:[^(]*\([^)]*\))*[^()]*\))', stringOfTargets)

	if len(listOfTargetStrings) > len(listOfSensorStrings):
		print("No solution")
		write(Solution())
		sys.exit()
	else:
		for targetString in listOfTargetStrings:
			targetString = targetString.strip('()')
			target_list = targetString.split(',')
			targetState = MonitorState(target_list[0].strip('""'), int(target_list[1]), int(sensor_list[2]), -1, {})
			listOfTargets.append(targetState)

		for sensor in listOfSensors:
			for target in listOfTargets:
				sensor.possible_edges[target] = euclideanDistance(sensor, target)

		for target in listOfTargets:
			for sensor in listOfSensors:
				target.possible_edges[sensor] = euclideanDistance(sensor, target)

		allStates = listOfSensors + listOfTargets

		solution = search(algo, MonitorProblem(allStates, MonitorState("root", 0, 0, 0, {}), 0))

		for s in allStates:
			print "Name %s Start %d Stop %d Power %d" %(s.name, s.start, s.stop, s.power)
			print "Possible edges: "
			for k, v in s.possible_edges.items():
				print "\t%s: %d" %(k.name, v)
			print "Attached edges: "
			for k, v in s.attached_edges.items():
				print "\t%s: %s" %(k.name, v)
			print ""

		write("monitor_"+algo+"_output", solution)

'''unfinished - processing the file and running the search to find the solution'''
def aggregation(file, algo):
	listOfStates = []

	stringOfStates = file.readline().strip().strip('[]')
	listOfStateStrings = re.split(r',(?!(?:[^(]*\([^)]*\))*[^()]*\))', stringOfStates)

	# pdb.set_trace()
	for stateString in listOfStateStrings:
		stateString = stateString.strip(" ").strip('()')
		state = stateString.split(',')
		print state
		aggState = AggState(state[0].strip('""'), int(state[1]), int(state[2]), {})
		listOfStates.append(aggState)

	for line in file:
		state_A = None
		state_B = None

		edge = line.strip().strip(" ").strip('()').split(",")
		stateA_name = edge[0].replace('"', '')
		print stateA_name
		stateB_name = edge[1].replace('"', '')
		print stateB_name
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

		stateA.edges[stateB] = weight
		stateB.edges[stateA] = weight

	problem = AggProblem(listOfStates, listOfStates[0], 0)
	solution = search(algo, problem)

	'''for state in listOfStates:
		print "\tState %s has children: " %state.name
		for child, weight in state.edges.items():
			print "\t\tChild %s, edge weight %d" %(child.name, weight)'''

	# print fields from solution to screen
	# write fields to file
	write("aggregate_"+algo+"_output", solution)

def write(filename, solution):
	output_file = open(filename+".txt", "w+")

	for x in solution.path:
		print "Path %s" %x.name
		output_file.write("Path %s\n" %x.name)

	print "Time %d" %solution.time
	print "Frontier space %d" %solution.frontier_space
	print "Explored space %d" %solution.explored_space
	print "Path cost %d" %solution.pathCost

	output_file.write("Time %d\n" %solution.time)
	output_file.write("Frontier space %d\n" %solution.frontier_space)
	output_file.write("Explored space %d\n" %solution.explored_space)
	output_file.write("Path cost %d\n" %solution.pathCost)

	output_file.close()

def euclideanDistance(sensor, target):
	a = sensor.start
	b = sensor.stop
	x = target.start
	y = target.stop

	return sqrt((a-x)**2 + (b-y)**2)

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
	print "Inside bfs"
	# pdb.set_trace()
	node = Node(problem.initial_state, None, None, 0)
	solution = Solution()
	solution.time += 1

	if node.state.name == "root":
		pass
	elif problem.goal_test(node):
		return solution

	frontier = Queue.Queue()
	frontier.put(node)
	explored = []

	while True:
		print "\tChecking nodes in queue"
		if frontier.empty():
			solution.explored_space = len(explored)
			return solution

		# pdb.set_trace()
		node = frontier.get()

		if node.state.name == "root":
			continue

		explored.append(node.state)

		node.state.visited = True
		solution.path.append(node.state)
		if node.parent is not None:
			solution.pathCost = problem.path_cost(solution.pathCost, node)

		for action in problem.actions(node.state):
			print "\t\tCreating child %s from node %s" %(action.name, node.state.name)
			child = node.child_node(problem, action)
			solution.time += 1

			if child.state not in explored and child not in frontier.queue:
				if problem.goal_test(child):
					solution.explored_space = len(explored)
					return solution
				frontier.put(child)
			# pdb.set_trace()
			if frontier.qsize() > solution.frontier_space:
				solution.frontier_space = frontier.qsize()

'''unfinished - how to take an element out of a priority queue (not at the front)'''
def unicost(problem):
	node = Node(problem.initial_state, None, None, 0)
	solution = Solution()
	solution.time += 1
	# print "Number of nodes created %d" %solution.time

	frontier = Queue.PriorityQueue()
	frontier.put(node)

	solution.frontier_space += 1

	explored = []

	while True:

		if frontier.empty():
			solution.explored_space = len(explored)
			return solution

		node = frontier.get()

		if problem.goal_test(node):
			solution.path.append(node.state)
			solution.explored_space = len(explored)
			return solution

		explored.append(node.state)

		node.state.visited = True
		solution.path.append(node.state)
		if node.parent is not None:
			# print "Original solution path cost: %d" %solution.pathCost
			# print "Path cost between %s and %s: %d" %(node.parent.state.name, node.state.name, problem.step_cost(node.parent.state, node.state))
			solution.pathCost = problem.path_cost(solution.pathCost, node)
			# print "Adding path: %d" %solution.pathCost

		for action in problem.actions(node.state):
			child = node.child_node(problem, action)
			print "child %s of parent %s has a path cost of %d" %(child.state.name, child.parent.state.name, child.pathCost)
			solution.time += 1
			# print "Number of nodes created: %d" %solution.time

			# pdb.set_trace()
			if child.state not in explored and child not in frontier.queue:
				print "Putting child %s of node %s in frontier" %(child.state.name, node.state.name)
				frontier.put(child)
			elif child.stateInQueueWithHigherCost(frontier):
				deletedNode = child.removeHigherNodeFromPQ(frontier)
				print "%s with weight %d is replaced by %s with weight %d" %(deletedNode.state.name, deletedNode.pathCost, child.state.name, child.pathCost)
				frontier.put(child)
				solution.pathCost = problem.remove_path_cost(solution.pathCost, deletedNode)
				solution.pathCost = problem.path_cost(solution.pathCost, child)

			if frontier.qsize() > solution.frontier_space:
				solution.frontier_space = frontier.qsize()

def iddfs(problem):
	for depth in xrange(sys.maxint):
		# print "inside iddfs %d" %depth
		solution = depth_limited_search(problem, depth)
		if solution != 'cutoff':
			return solution

def depth_limited_search(problem, limit):
	# print "inside depth_limited_search %d" %limit
	solution = Solution()
	solution.time += 1
	return recursive_dls(Node(problem.initial_state), problem, solution, limit)

def recursive_dls(node, problem, solution, limit):
	# print "inside recursive dls %d" %limit
	node.state.visited = True
	if problem.goal_test(node):
		# print "At goal state"
		return solution
	elif limit == 0:
		# print "At cutoff"
		return 'cutoff'
	else:
		atCutoff = False
		for action in problem.actions(node.state):
			child = node.child_node(problem, action)
			solution.time += 1
			solution.pathCost = problem.path_cost(solution.pathCost, child)
			result = recursive_dls(child, problem, solution, limit-1)
			if result == 'cutoff':
				atCutoff = True
			elif result is not None:
				return result
		if atCutoff == True:
			return 'cutoff'
		else:
			return None

def greedy(problem):
	pass

''' STANDARD CLASS DEFINITIONS '''

class State:
	def __init__(self, name, start, stop):
		self.name = name
		self.start = start
		self.stop = stop

class Node:
	def __init__(self, state, parent=None, action=None, pathCost=0):
		self.state = state
		self.parent = parent
		self.action = action
		self.pathCost = pathCost

	def __cmp__(self, other):
		return cmp(self.pathCost, other.pathCost)

	def child_node(self, problem, action):
		child_state = problem.result(self.state, action)
		pathCost = self.pathCost + problem.step_cost(self.state, action)
		return Node(child_state, self, action, pathCost)

	'''given a node and a priority queue
	if the state of the node is in the pq with a higher cost return true
	else return false'''
	def stateInQueueWithHigherCost(self, pq):
		# pdb.set_trace()
		for pq_node in pq.queue:
			if self.state is pq_node.state:
				if self.pathCost < pq_node.pathCost:
					return True
		return False

	'''take out all the elements currently in the queue and put them all back
	except for the one that needs removed'''
	def removeHigherNodeFromPQ(self, pq):
		# pdb.set_trace()
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
		self.pathCost = 0 	# for monitor cost = P(sub t)
						# for agg cost = sum of weights in the path to visit all nodes

	''' this is never called '''
	def setSolutionMetrics(self, node):
		solution_path = []

		curr = node

		while curr is not None:
			self.path.append(curr.state)
			curr = curr.parent

		if node is not None:
			self.pathCost = node.pathCost

		return self

''' PROBLEM SPECIFIC CLASS DEFINITIONS '''

''' MONITOR PROBLEM '''
class MonitorState(State):
	def __init__(self, name, start, stop, power, possible_edges, attached_edges={}, visited=False):
		State.__init__(self, name, start, stop)
		self.power = power
		self.possible_edges = possible_edges
		self.attached_edges = attached_edges
		self.visited = visited

	def addAdjacentState(self, target, distance):
		self.possible_edges[target] = distance

class MonitorProblem():
	def __init__(self, states, initial_state, pathCost=0):
		self.states = states
		self.initial_state = initial_state
		self.pathCost = pathCost

	''' given the state, what states can this state go to? '''
	def actions(self, state):
		children = []

		for child in state.possible_edges:
			children.append(child)

		return children

	''' a state attaches itself to a new state
		if the original state is a sensor:
			state.power = state.power - euclideanDistance between sensor(state) and target(action)
		if the original state is a target:
			action.power = action.power - euclideanDistance between sensor(action) and target(state)'''
	def result(self, state, action):

		if state.power != -1:
			state.power -= euclideanDistance(state, action)
		else:
			action.power -= euclideanDistance(action, state)

		action.attached_edges[state] = euclideanDistance(state, action)
		state.attached_edges[action] = euclideanDistance(state, action)
		return action

	''' given a node, if the node is a sensor
	    return true if all the targets that this sensor can visit
	    are being monitored'''
	def goal_test(self, node):
		# pdb.set_trace()
		goal = True
		if node.state.power != -1:
			for target in node.state.possible_edges:
				if target.visited == False:
					goal = False

		return goal

	def path_cost(self, current_path_cost, node):
		return current_path_cost + self.step_cost(node.parent.state, node.state)

	def remove_path_cost(self, current_path_cost, node):
		return current_path_cost - self.step_cost(node.parent.state, node.state)

	''' if stateA is a target
	check that stateB is monitoring the target
	and return stateB's power '''
	def step_cost(self, stateA, stateB):
		if stateA.power == -1:
			for sensor in stateA.attached_edges:
				if sensor is stateB:
					return sensor.power
		else:
			return stateA.power

''' AGGREGATION PROBLEM '''
class AggState(State):
	def __init__(self, name, start, stop, edges, visited=False):
		State.__init__(self, name, start, stop)
		self.edges = edges
		self.visited = visited

	def addAdjacentState(self, state, weight):
		# add a new node to the list of nodes connected to this object
		self.edges.update({state: weight})
		print len(self.edges)
		print "States attached to %s" %self.name
		for state, weight in self.edges.items():
			print "\t%s %d" %(state.name, weight)

class AggProblem:
	def __init__(self, states, initial_state, pathCost=0):
		self.states = states # a list of all the states
		self.initial_state = initial_state # starting node for traversing the graph
		self.pathCost = pathCost

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
		for n in self.states:
			if n.visited == False:
				return False

		return True

	def path_cost(self, current_path_cost, node):
		return current_path_cost + self.step_cost(node.parent.state, node.state)

	def remove_path_cost(self, current_path_cost, nodeA):
		return current_path_cost - self.step_cost(node.parent.state, node.state)

	# find the weight of the edge between these two states
	def step_cost(self, stateA, stateB):
		#pdb.set_trace()

		if stateB in stateA.edges.keys():
			return stateA.edges[stateB]
		return 0

if __name__ == "__main__":
	main()