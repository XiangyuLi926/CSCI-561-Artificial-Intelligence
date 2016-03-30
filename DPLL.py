import copy

import sys
""" READ THE INPUT FILE """
inputFile = open(sys.argv[2])
line_number = int(inputFile.readline())

string = []

for line in inputFile:
	string.append(line)
inputFile.close()

""" Check for Valid Number of Sentences"""
if line_number < 0 or line_number > 0x7fffffff:
	print 'Invalid Line Number'
	sys.exit(0)

# string = []
# string.append(["and", ["or", "A", "B"], ["or", ["not", "A"], "C"], ["or", ["not", "B"], "C"], ["or", ["not", "C"], "B"]])
# string.append(["and", ["or", "A", "B", "C"], ["or", ["not", "A"], ["not", "B"]], ["or", ["not", "B"], ["not", "C"]]])

""" Useful Fuctions """
def Do_DPLL(Clauses, Symbols, Model):

	#true
	if(len(Clauses) == 0):
		return 1

	#false
	if(len(Clauses) != 0):
		for clause in Clauses:
			if(len(clause) == 0):
				return 0

	P, Value = Find_Pure_Symbols(Symbols, Clauses, Model)
	if(P != None):
		Symbols.remove(P)
		if(Value == 'true'):
			Model.append(P)
		else:
			Model.append(P.lower())

		marklen = len(Clauses)
		if(Value == 'true'):
			for i in range(0, marklen):
				for clause in Clauses:
					if(P in clause):
						Clauses.remove(clause)
		else:
			for i in range(0, marklen):
				for clause in Clauses:
					if(P.lower() in clause):
						Clauses.remove(clause)	
		return Do_DPLL(Clauses, Symbols, Model)		


	P, Value = Find_Unit_Clause(Clauses, Model)
	if(P != None):
		if(P in Symbols):
			Symbols.remove(P)
			Model.append(P)

			marklen = len(Clauses)
			for i in range(0, marklen):
				for clause in Clauses:
					if(P in clause):
						Clauses.remove(clause)
			marklen = len(Clauses)
			for i in range(0, marklen):
				for clause in Clauses:
					if(P.lower() in clause):
						clause.remove(P.lower())
		else:
			Symbols.remove(P.upper())
			Model.append(P)

			marklen = len(Clauses)
			for i in range(0, marklen):
				for clause in Clauses:
					if(P in clause):
						Clauses.remove(clause)
			marklen = len(Clauses)
			for i in range(0, marklen):
				for clause in Clauses:
					if(P.upper() in clause):
						clause.remove(P.upper())

		return Do_DPLL(Clauses, Symbols, Model)


	value1 = 0
	value2 = 0

	if(len(Symbols) > 0):
		tempClauses = copy.deepcopy(Clauses)
		tempModel = copy.deepcopy(Model)

		P = Symbols[0]
		del Symbols[0]

		Model.append(P)
		marklen = len(Clauses)
		for i in range(0, marklen):
			for clause in Clauses:
				if(P in clause):
					Clauses.remove(clause)
		marklen = len(Clauses)
		for i in range(0, marklen):
			for clause in Clauses:
				if(P.lower() in clause):
					clause.remove(P.lower())
		value1 = Do_DPLL(Clauses, Symbols, Model)

		Clauses = copy.deepcopy(tempClauses)
		Model = copy.deepcopy(tempModel)

		Model.append(P.lower())
		marklen = len(Clauses)
		for i in range(0, marklen):
			for clause in Clauses:
				if(P in clause):
					Clauses.remove(clause)
		marklen = len(Clauses)
		for i in range(0, marklen):
			for clause in Clauses:
				if(P.upper() in clause):
					clause.remove(P.upper())

		value2 = Do_DPLL(Clauses, Symbols, Model)
	
		if(value1 == 0 and value2 == 0):
			return 0
		else:
			return 1
def Find_Pure_Symbols(Symbols, Clauses, Model):

	if(len(Symbols) == 0):
		return None, None

	for i in range(0, len(Symbols)):
		Flag1 = 0 # mark P
		Flag0 = 0 # mark not P
		for j in range(0, len(Clauses)):
			if(Symbols[i] in Clauses[j]):
				Flag1 = 1
				for k in range(0, len(Clauses)):
					if(Symbols[i].lower() in Clauses[k]):
						Flag0 = 1
				
				if(Flag0 == 0):
					return Symbols[i], 'true'
			elif(Symbols[i].lower() in Clauses[j]):
				Flag0 = 1

				for k in range(0, len(Clauses)):
					if(Symbols[i] in Clauses[k]):
						Flag1 = 1

				if(Flag1 == 0):
					return Symbols[i], 'false'

	return None, None

def Find_Unit_Clause(Clauses, Model):

	for clause in Clauses:
		if(len(clause) == 1):
			return clause[0], 'true'
	return None, None

#string[i] = eval(string[i])
""" MAIN PART """

for i in range(0, line_number):
	Clauses_outer = []
	Symbols_outer = []
	Model_outer = []

	string[i] = eval(string[i])

	if(string[i][0] == 'not'):
		Clauses_outer = string[i]
		Symbols_outer.append(Clauses_outer[1])
		Clauses_outer = [string[i][1].lower()]

	elif(string[i][0] == 'or'):
		Clauses_outer = string[i]
		for j in range(1, len(Clauses_outer)):
			if(len(Clauses_outer[j]) == 1):
				if(Clauses_outer[j] not in Symbols_outer):
					Symbols_outer.append(Clauses_outer[j])
			else:
				if(Clauses_outer[j][1] not in Symbols_outer):
					Symbols_outer.append(Clauses_outer[j][1])
				Clauses_outer[j] = Clauses_outer[j][1].lower()

		Clauses_outer.remove('or')
		Clauses_outer = [Clauses_outer]

	elif(string[i][0] == 'and'):
		Clauses_outer = string[i]
		for j in range(1, len(Clauses_outer)):
			if(Clauses_outer[j][0] == 'not'):
				if(Clauses_outer[j][1] not in Symbols_outer):
					Symbols_outer.append(Clauses_outer[j][1])
				Clauses_outer[j] = [Clauses_outer[j][1].lower()]

			elif(Clauses_outer[j][0] == 'or'):
				for k in range(1, len(Clauses_outer[j])):
					if(len(Clauses_outer[j][k]) == 1):
						if(Clauses_outer[j][k] not in Symbols_outer):
							Symbols_outer.append(Clauses_outer[j][k])
					else:
						if(Clauses_outer[j][k][1] not in Symbols_outer):
							Symbols_outer.append(Clauses_outer[j][k][1])
						Clauses_outer[j][k] = Clauses_outer[j][k][1].lower()
				Clauses_outer[j].remove('or')

			elif(len(Clauses_outer[j]) == 1):
				if(Clauses_outer[j] not in Symbols_outer):
					Symbols_outer.append(Clauses_outer[j])
				Clauses_outer[j] = [Clauses_outer[j][0]]
		Clauses_outer.remove('and')
	else: # simple atom
		Clauses_outer = [string[i]]
		Symbols_outer.append(Clauses_outer[0][0])

	Value_of_Clauses = Do_DPLL(Clauses_outer, Symbols_outer, Model_outer)

	# print '\r'
	# print Value_of_Clauses
	# print Clauses_outer
	# print Symbols_outer
	# print Model_outer

	if(len(Symbols_outer) > 0):
		for j in range(0, len(Symbols_outer)):
			Model_outer.append(Symbols_outer[j])

	if(Value_of_Clauses == 1):
		string[i] = []
		string[i].append('true')
		for j in range(0, len(Model_outer)):
			if(ord(Model_outer[j]) >= 65 and ord(Model_outer[j]) <= 90):
				string[i].append(Model_outer[j] + '=true')
			else:
				string[i].append(Model_outer[j].upper() + '=false')

	else:
		string[i] = []
		string[i].append('false')

	# print string[i]


""" OUT TO FILE """

outputFile = open("CNF_satisfiability.txt", "w")
for i in range(0, line_number):
	outputFile.write(str(string[i]))
	outputFile.write('\n')