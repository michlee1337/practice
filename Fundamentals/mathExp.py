# convert in to post fix

def inToPost(exp):
	exp = exp.split()
	operators = ['/','*','+','-','(']
	output = []
	opstack = []

	# for each item in input
	for item in exp:

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
			while opstack != [] and operators.index(opstack[-1]) <= operators.index(item):
				output.append(opstack.pop())
			opstack.append(item)

		# if operand, add to end of output
		else:
			output.append(item)


	# pop anything remaining on opstack
	while len(opstack) != 0:
		output.append(opstack.pop())
	return(output)

def postEval(exp):
	oprStack = []
	operators = ['/','*','+','-']
	# read from left to right
	for item in exp:
		# if operator, eval with last two operands
		if item in operators:
			B = oprStack.pop()
			A = oprStack.pop()
			if item == '/':
				oprStack.append(A/B)
			elif item == '*':
				oprStack.append(A*B)
			elif item == '+':
				oprStack.append(A+B)
			elif item == '-':
				oprStack.append(A-B)
		# if operands, store
		else:
			oprStack.append(int(item))
	return(oprStack.pop())

		



	print(" ".join(output))

if __name__ == "__main__":
	expL = ["1 + 2 * 3 + 4", "( 1 + 2 ) * ( 3 + 4 )", "1 * 2 + 3 * 4", "1 + 2 + 3 + 4"]
	postL = []
	convertedL = map(inToPost,expL)
	print(list(convertedL))
	evalL = map(postEval,convertedL)
	print(list(evalL))

