class Me:
	def __init__(self, age):
		self.age = age

def main():
	me = Me(22)
	print(me.age)
	me.age += 1
	print(me.age)

if __name__ == "__main__":
	main()