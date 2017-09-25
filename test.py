import Queue
import sys
import pdb

class Me:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __cmp__(self, other):
		return cmp(self.age, other.age)

class AggState:
	def __init__(self, name, start, stop):
		self.name = name
		self.start = start
		self.stop = stop

def main():
	file = open(sys.argv[1])
	file.readline()
	monitor(file)

def monitor(file):
	# pdb.set_trace()
	listOfSensors = []
	listOfTargets = []

	stringOfSensors = file.readline().strip().replace(',', ' ').strip('[]')
	listOfSensorStrings = stringOfSensors.split('  ')

	for sensorString in listOfSensorStrings:
		sensorString = sensorString.strip('()')
		sensor_list = sensorString.split(' ')
		for x in sensor_list: print x
		listOfSensors.append(sensor_list[0])

	stringOfTargets = file.readline().strip().replace(',', ' ').strip('[]')
	listOfTargetStrings = stringOfTargets.split('  ')

	if len(listOfTargetStrings) > len(listOfSensors):
		print len(listOfTargetStrings) > len(listOfSensors)
		sys.exit()
	else:
		for targetString in listOfTargetStrings:
			targetString = targetString.strip('()')
			target_list = targetString.split(' ')
			for x in target_list: print x
			listOfTargets.append(target_list[0])

		for sensor in listOfSensors:
			for target in listOfTargets:
				print "Target %s is reachable from sensor %s" %(target, sensor)

		for target in listOfTargets:
			for sensor in listOfSensors:
				print "Sensor %s is reachable from target %s" %(sensor, target)

		allStates = listOfSensors + listOfTargets

		print "Number of sensors + targets: %d" %len(allStates)
		print "All possible states: "
		for x in allStates: print x

if __name__ == "__main__":
	main()