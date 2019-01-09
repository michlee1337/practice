# convert in to post fix

def inToPost():
	expO = raw_input("input infix exp seperated by spaces: ").split()
	operators = ['/','*','+','-','(']
	output = []
	opstack = []

	# for each item in input
	for item in expO:

		# if open bracket, add to opp stack
		if item == "(":
			opstack.append(item)

		# if close bracket, pop all ops until open bracket
		elif item == ")":
			while opstack[-1] != "(":
				output.append(opstack.pop())
			opstack.pop()

		# if operator, add to opstack after removing prioritised operators
		elif item in operators:
			while opstack != [] and operators.index(opstack[-1]) < operators.index(item):
				output.append(opstack.pop())
			opstack.append(item)

		# if operand, add to end of output
		else:
			output.append(item)


	# pop anything remaining on opstack
	while len(opstack) != 0:
		output.append(opstack.pop())



	print(" ".join(output))

if __name__ == "__main__":
	inToPost()