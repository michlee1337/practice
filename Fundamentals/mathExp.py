# convert in to post fix

def inToPost():
	expO = raw_input("input infix exp seperated by spaces: ").split()
	operators = ['/','*','+','-']
	output = []
	opstack = []
	#bracket = False

	# for each item in input
	for item in expO:
		print('t',output)

		# if operand, add to end of output
		if item not in operators:
			output.append(item)

		# if operator, add to opstack after removing prioritised operators
		elif item in operators:
			while opstack != [] and operators.index(opstack[0]) < operators.index(item):
				output.append(opstack.pop())
			opstack.append(item)

	# pop anything remaining on opstack
	while len(opstack) != 0:
		print(opstack)
		output.append(opstack.pop())



	print(output)

if __name__ == "__main__":
	inToPost()