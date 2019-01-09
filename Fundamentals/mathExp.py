# convert in to post fix

def inToPost():
	expO = raw_input("input infix exp seperated by spaces: ").split()
	operators = ['/','*','+','-']
	output = []
	opstack = []
	#bracket = False

	# for each item in input
	for item in exp0:

	# if open bracket, all operators have priority until close bracket
	#if item == "(":
	#	bracket = True

	# if operand, add to end of output
	elif item not in operators:
		output.append(item)

	# if operator
	if item in operators:
		while opstack != [] and operators.find(opstack[0]) < operators.find(item):
			output.append(opstack.pop())
		opstack.append(item)

	print('test')

if __name__ == "__main__":
	inToPost()