# convert in to post fix

def inToPost():
	expO = raw_input("input infix exp seperated by spaces: ").split()
	operators = ['/','*','+','-']
	output = []
	opstack = []
	bracket = False

	# for each item in input
	for item in exp0:

	# if open bracket, all operators have priority until close bracket
	if item == "(":
		bracket = True

	# if operand, add to end of output
	elif item not in operators:
		output.append(item)

	# if operator
	if item in operators:
		if bracket is True:
			while opstack is not None and operarors.find(opstack[0]) > operators.find(item):
				output.append(opstack.pop())
#! change this to make brackets work better

		# if any higher priority in operand stack
			# pop to end of output
		# append operator

	# for all operators remaining in stack
		# pop to end of output

	print(expO)

if __name__ == "__main__":
	inToPost()