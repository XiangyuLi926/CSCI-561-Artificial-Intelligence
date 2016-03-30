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

""" Useful Fuctions """
def Biconditional_elimination(B_e_str):

	if(len(B_e_str) > 1):
		for i in range(1, len(B_e_str)):
			B_e_str[i] = Biconditional_elimination(B_e_str[i])

	if(B_e_str[0] == 'iff'):
		B_e_str[0] = 'and'
		Be_temp1 = B_e_str[1]
		Be_temp2 = B_e_str[2]
		B_e_str[1] = ['implies', Be_temp1, Be_temp2]
		B_e_str[2] = ['implies', Be_temp2, Be_temp1]

	return B_e_str

def Implication_elimination(I_e_str):

	if(len(I_e_str) > 1):
		for i in range(1, len(I_e_str)):
			I_e_str[i] = Implication_elimination(I_e_str[i])

	if(I_e_str[0] == 'implies'):
		I_e_str[0] = 'or'
		I_e_str[1] = ['not', I_e_str[1]]

	return I_e_str

def De_Morgan_laws(D_M_str):

	if(len(D_M_str) > 1):
		for i in range(1, len(D_M_str)):
			D_M_str[i] = De_Morgan_laws(D_M_str[i])

	if(D_M_str[0] == 'not'):

		if(len(D_M_str[1]) > 2):
			if(D_M_str[1][0] == 'and'):
				D_M_str[0] = 'or'
				for i in range(1, len(D_M_str[1])):
					D_M_str.append(['not', D_M_str[1][i]])
				del D_M_str[1]

			elif(D_M_str[1][0] == 'or'):
			 	D_M_str[0] = 'and'
				for i in range(1, len(D_M_str[1])):
					D_M_str.append(['not', D_M_str[1][i]])
				del D_M_str[1]

	return D_M_str

def Double_negation_elimination(Double_str):

	if(len(Double_str) > 1):
		for i in range(1, len(Double_str)):
			Double_str[i] = Double_negation_elimination(Double_str[i])

	if(Double_str[0] == 'not'):
		if(len(Double_str[1]) == 2):
			Double_str = Double_str[1][1]

	return Double_str

def Distributivity_of_dis_on_con(Distribute_str):

	if(len(Distribute_str) > 1):
		for i in range(1, len(Distribute_str)):
			Distribute_str[i] = Distributivity_of_dis_on_con(Distribute_str[i])

	Distri_temp1 = []
	Distri_temp2 = []
	if(Distribute_str[0] == 'or'):
		for i in range(1, len(Distribute_str)):
			if(Distribute_str[i][0] == 'and'):			
				Distri_temp1 = Distribute_str[i]			
				del Distribute_str[i]
				del Distribute_str[0]	
				Distri_temp2 = Distribute_str
				Distribute_str = ['and']
				for j in range(1, len(Distri_temp1)):
					Distribute_str.append(['or', Distri_temp1[j]])
					for k in range(0, len(Distri_temp2)):
						Distribute_str[j].append(Distri_temp2[k])

				break
	return Distribute_str

def Duplicate_elimination_of_or_and(D_e_str):

	if(len(D_e_str) > 1):
		for i in range(1, len(D_e_str)):
			D_e_str[i] = Duplicate_elimination_of_or_and(D_e_str[i])	

	if(D_e_str[0] == 'or'):
		for i in range(1, len(D_e_str)):
			if(D_e_str[i][0] == 'or'):
				D_e_temp = D_e_str[i]
				del D_e_str[i]
				for j in range(1, len(D_e_temp)):
					D_e_str.append(D_e_temp[j])	

	if(D_e_str[0] == 'and'):
		for i in range(1, len(D_e_str)):
			if(D_e_str[i][0] == 'and'):
				D_e_temp = D_e_str[i]
				del D_e_str[i]
				for j in range(1, len(D_e_temp)):
					D_e_str.append(D_e_temp[j])
			
	return D_e_str

def Duplicate_elimination_same_variable(D_e_s_v_str):

	if(D_e_s_v_str[0] == 'or'):
		tempstr = ['or']
		for i in range(1, len(D_e_s_v_str)):
			if(D_e_s_v_str[i] not in tempstr):
				tempstr.append(D_e_s_v_str[i])
		if(len(tempstr) == 2):
			D_e_s_v_str = tempstr[1]
		else:
			D_e_s_v_str = tempstr

	elif(D_e_s_v_str[0] == 'and'):
		for i in range(1, len(D_e_s_v_str)):
			# remove in [and, [or]]
			if(len(D_e_s_v_str[i]) > 2):
				tempstr = ['or']
				for j in range(1, len(D_e_s_v_str[i])):
					if(D_e_s_v_str[i][j] not in tempstr):
						tempstr.append(D_e_s_v_str[i][j])
				tempstr.remove('or')
				tempstr.sort()
				tempstr.insert(0,'or')
				if(len(tempstr) == 2):
					D_e_s_v_str[i] = tempstr[1]
				else:
					D_e_s_v_str[i] = tempstr

		tempstr = ['and']
		for i in range(1, len(D_e_s_v_str)):
			if(D_e_s_v_str[i] not in tempstr):
				tempstr.append(D_e_s_v_str[i])
		if(len(tempstr) == 2):
			D_e_s_v_str = tempstr[1]
		else:
			D_e_s_v_str = tempstr

	return D_e_s_v_str
""" MAIN PART """

for i in range(0, line_number):
	string[i] = eval(string[i])
	string[i] = Biconditional_elimination(string[i])
	string[i] = str(string[i])

	string[i] = eval(string[i])
	string[i] = Implication_elimination(string[i])
	string[i] = str(string[i])

	# calculete the recursive depth before De Morgan laws, do it from inside to outside
	ReCursiveCont = 0 
	for j in range(1, len(string[i])):
		if(string[i][j] == '['):
			ReCursiveCont = ReCursiveCont + 1
	string[i] = eval(string[i])
	for j in range(0, ReCursiveCont):
		string[i] = De_Morgan_laws(string[i])
	string[i] = str(string[i])

	string[i] = eval(string[i])
	string[i] = Double_negation_elimination(string[i])
	string[i] = str(string[i])

	ReCursiveCont = 0 
	for j in range(1, len(string[i])):
		if(string[i][j] == '['):
			ReCursiveCont = ReCursiveCont + 1
	string[i] = eval(string[i])
	for j in range(0, ReCursiveCont):
		string[i] = Distributivity_of_dis_on_con(string[i])
	string[i] = str(string[i])


	ReCursiveCont = 0 
	for j in range(1, len(string[i])):
		if(string[i][j] == '['):
			ReCursiveCont = ReCursiveCont + 1
	string[i] = eval(string[i])
	for j in range(0, ReCursiveCont):
		string[i] = Duplicate_elimination_of_or_and(string[i])
	string[i] = str(string[i])

	string[i] = eval(string[i])
	string[i] = Duplicate_elimination_same_variable(string[i])
	string[i] = str(string[i])

""" OUT TO FILE """

outputFile = open("sentences_CNF.txt", "w")
for i in range(0, line_number):
	outputFile.write(string[i])
	outputFile.write('\n')