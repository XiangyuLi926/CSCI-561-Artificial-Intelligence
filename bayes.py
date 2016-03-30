""" READ THE INPUT FILE """
import sys
inputFile = open(sys.argv[2])
inputFile_name = sys.argv[2]
inputFile_name_list = inputFile_name.split('/') # $LIB/input.txt
inputFile_name = inputFile_name_list[len(inputFile_name_list) - 1] # Last one element in inputFile name: input.txt
inputFile_name_without_kind = inputFile_name.split('.')[0] # without .txt

string = []
for line in inputFile:
	string.append(line)
inputFile.close()

""" Build The Data Struct """
#Read the numbers of diseases and patients
Numbers_temp = string[0].split() # list of numbers

Number_of_Diseases = int(Numbers_temp[0]) # n in description
Number_of_Patients = int(Numbers_temp[1]) # k in description

#Read Diseases' information------4*n part
Diseases_name = []
Diseases_findings_num = []
Diseases_P = []

Diseases_findings = []

With_Disease_findings_P = []
Without_Disease_findings_P = []

for i in range(0, Number_of_Diseases):
	#Read Diseases's name and number of findings and P(D)
	Diseases_name_findings_P_temp = string[1 + i * 4].split(' ')

	Diseases_name.append(str(Diseases_name_findings_P_temp[0]))
	Diseases_findings_num.append(int(Diseases_name_findings_P_temp[1]))
	Diseases_P.append(float(Diseases_name_findings_P_temp[2]))
	#Read Diseases's findings and corresponding probability with or without the disease
	Diseases_findings.append(eval(string[2 + i * 4]))
	With_Disease_findings_P.append(eval(string[3 + i * 4]))
	Without_Disease_findings_P.append(eval(string[4 + i * 4]))

#Read Patient's information-------n*k part

Patients_findings = []
for i in range(0, Number_of_Patients):
	Patients_findings.append([])
	for j in range(0, Number_of_Diseases):
		Patients_findings[i].append(eval(string[4 * Number_of_Diseases + Number_of_Diseases * i + j + 1]))

""" Useful Fuctions """
# P(D|xi) = 1/(1 + P(xi|~D)/P(xi|D) ) where xi represent T or F in the database
# We can compute P(xi|~D)/P(xi|D) first
diction_1 = {}
diction_2 = {}
diction_3 = {}

def Problem():

	for i in range(0, Number_of_Diseases):
		diction_1[Diseases_name[i]] = ' '	
		diction_2[Diseases_name[i]] = [' ', ' ']
		diction_3[Diseases_name[i]] = [' ', ' ', ' ', ' ']

	for i in range(0, Number_of_Patients):
		# print 'Patient-' + str(i + 1) +  ':' #Outputpart
		outputFile.write('Patient-' + str(i + 1) + ':'+ '\r\n')
		for j in range(0, Number_of_Diseases):
			product1 = 1.0 # P(xi|~D)
			product2 = 1.0 # P(xi|D)
			product1 *= (1 - Diseases_P[j])
			product2 *= Diseases_P[j]

			problem2_min_prod = 1.0
			problem2_max_prod = 1.0
			problem2_min_prod_flag = 0

			Uncertain_Finding_flag = 0
			Decrease_Most_pro = 0.0 # smallest value of non-nagetive float 
			Increase_Most_pro = 1.7976931348623157e+308  # largest value of float
			Most_Decrease_Name = 'zzzzzzzzzzzzzzzzzzzzzzzz' # For alphabetical order
			Most_Increase_Name = 'zzzzzzzzzzzzzzzzzzzzzzzz' # For alphabetical order


			for k in range(0, Diseases_findings_num[j]) :
				if Patients_findings[i][j][k] == 'T' : # Problem 1
					product1 *= Without_Disease_findings_P[j][k]
					product2 *= With_Disease_findings_P[j][k]
				elif Patients_findings[i][j][k] == 'F' : # Problem 1
					product1 *= (1 - Without_Disease_findings_P[j][k])
					product2 *= (1 - With_Disease_findings_P[j][k])

				elif Patients_findings[i][j][k] == 'U': # No use in problem 1, but use in problem 2 and problem 3
					if Without_Disease_findings_P[j][k] > With_Disease_findings_P[j][k] :

						if With_Disease_findings_P[j][k] != 0:
							problem2_min_prod *= Without_Disease_findings_P[j][k] / With_Disease_findings_P[j][k]
						else:
							problem2_min_prod_flag = 1

						if (1 - With_Disease_findings_P[j][k]) != 0:
							problem2_max_prod *= (1 - Without_Disease_findings_P[j][k]) / (1 - With_Disease_findings_P[j][k])

					elif Without_Disease_findings_P[j][k] < With_Disease_findings_P[j][k] :

						if (1 - With_Disease_findings_P[j][k]) != 0:
							problem2_min_prod *= (1 - Without_Disease_findings_P[j][k]) / (1 - With_Disease_findings_P[j][k])
						else:
							problem2_min_prod_flag = 1

						if With_Disease_findings_P[j][k] != 0:
							problem2_max_prod *= Without_Disease_findings_P[j][k] / With_Disease_findings_P[j][k]

					elif Without_Disease_findings_P[j][k] == With_Disease_findings_P[j][k] :
						pass




					Uncertain_Finding_flag = 1 # For problem 3
					if Without_Disease_findings_P[j][k] > With_Disease_findings_P[j][k] :

						if With_Disease_findings_P[j][k] != 0:
							More_Decrease = Without_Disease_findings_P[j][k] / With_Disease_findings_P[j][k]
						else:
							problem2_min_prod_flag = 1
							Most_Decrease_Name_if_0 = Diseases_findings[j][k]
							Most_Decrease_Value_if_0 = 'T'

						if (1 - With_Disease_findings_P[j][k]) != 0:
							More_Increase = (1 - Without_Disease_findings_P[j][k]) / (1 - With_Disease_findings_P[j][k])

					elif Without_Disease_findings_P[j][k] < With_Disease_findings_P[j][k] :

						if (1 - With_Disease_findings_P[j][k]) != 0:
							More_Decrease = (1 - Without_Disease_findings_P[j][k]) / (1 - With_Disease_findings_P[j][k])
						else:
							problem2_min_prod_flag = 1
							Most_Decrease_Name_if_0 = Diseases_findings[j][k]
							Most_Decrease_Value_if_0 = 'F'

						if With_Disease_findings_P[j][k] != 0:
							More_Increase = Without_Disease_findings_P[j][k] / With_Disease_findings_P[j][k]

					elif Without_Disease_findings_P[j][k] == With_Disease_findings_P[j][k] :
						More_Decrease = 1.0
						More_Increase = 1.0



					if More_Decrease > Decrease_Most_pro : # No = for using the first one
						Decrease_Most_pro = More_Decrease
						Most_Decrease_Name = Diseases_findings[j][k]
						if Without_Disease_findings_P[j][k] >= With_Disease_findings_P[j][k]:
							Most_Decrease_Value = 'T'
						else:
							Most_Decrease_Value = 'F'
					elif More_Decrease == Decrease_Most_pro and Diseases_findings[j][k] < Most_Decrease_Name :# For alphabatical order
						Most_Decrease_Name = Diseases_findings[j][k]
						if Without_Disease_findings_P[j][k] >= With_Disease_findings_P[j][k]:
							Most_Decrease_Value = 'T'
						else:
							Most_Decrease_Value = 'F'

					if More_Increase < Increase_Most_pro : # No = for using the first one
						Increase_Most_pro = More_Increase
						Most_Increase_Name = Diseases_findings[j][k]
						if Without_Disease_findings_P[j][k] < With_Disease_findings_P[j][k]:
							Most_Increase_Value = 'T'
						else:
							Most_Increase_Value = 'F'
					elif More_Increase == Increase_Most_pro and Diseases_findings[j][k] < Most_Increase_Name :# For alphabatical order
						Most_Increase_Name = Diseases_findings[j][k]
						if Without_Disease_findings_P[j][k] < With_Disease_findings_P[j][k]:
							Most_Increase_Value = 'T'
						else:
							Most_Increase_Value = 'F'
			
			if product2 != 0:				
				answer_1 = 1 / (1 + product1 / product2)
				diction_1[Diseases_name[j]] = str('%0.4f'%round(answer_1, 4))

				if product1 != 0:
					if problem2_min_prod_flag == 0 :
						answer_2_min = 1 / (1 + problem2_min_prod * product1 / product2)
						answer_2_max = 1 / (1 + problem2_max_prod * product1 / product2)			
						diction_2[Diseases_name[j]][0] = str('%0.4f'%round(answer_2_min, 4))
						diction_2[Diseases_name[j]][1] = str('%0.4f'%round(answer_2_max, 4))
					elif problem2_min_prod_flag == 1 :
						answer_2_min = 0
						answer_2_max = 1 / (1 + problem2_max_prod * product1 / product2)			
						diction_2[Diseases_name[j]][0] = str('%0.4f'%round(answer_2_min, 4))
						diction_2[Diseases_name[j]][1] = str('%0.4f'%round(answer_2_max, 4))


					if Uncertain_Finding_flag == 0 :
						diction_3[Diseases_name[j]][0] = 'none'
						diction_3[Diseases_name[j]][1] = 'N'
						diction_3[Diseases_name[j]][2] = 'none'
						diction_3[Diseases_name[j]][3] = 'N'
					elif Uncertain_Finding_flag == 1:

						if problem2_min_prod_flag == 0 :
							diction_3[Diseases_name[j]][0] = Most_Increase_Name
							diction_3[Diseases_name[j]][1] = Most_Increase_Value
							diction_3[Diseases_name[j]][2] = Most_Decrease_Name
							diction_3[Diseases_name[j]][3] = Most_Decrease_Value
						elif problem2_min_prod_flag == 1 :
							diction_3[Diseases_name[j]][0] = Most_Increase_Name
							diction_3[Diseases_name[j]][1] = Most_Increase_Value
							diction_3[Diseases_name[j]][2] = Most_Decrease_Name_if_0
							diction_3[Diseases_name[j]][3] = Most_Decrease_Value_if_0

						if Increase_Most_pro == 1.0 :
							diction_3[Diseases_name[j]][0] = 'none'
							diction_3[Diseases_name[j]][1] = 'N'	
						if Decrease_Most_pro == 1.0 :
							diction_3[Diseases_name[j]][2] = 'none'
							diction_3[Diseases_name[j]][3] = 'N'	
				elif product1 == 0:
					diction_1[Diseases_name[j]] = str('%0.4f'%round(1, 4))
					diction_2[Diseases_name[j]][0] = str('%0.4f'%round(1, 4))
					diction_2[Diseases_name[j]][1] = str('%0.4f'%round(1, 4))
					diction_3[Diseases_name[j]][0] = 'none'
					diction_3[Diseases_name[j]][1] = 'N'
					diction_3[Diseases_name[j]][2] = 'none'
					diction_3[Diseases_name[j]][3] = 'N'	

			else:
				diction_1[Diseases_name[j]] = str('%0.4f'%round(0, 4))
				diction_2[Diseases_name[j]][0] = str('%0.4f'%round(0, 4))
				diction_2[Diseases_name[j]][1] = str('%0.4f'%round(0, 4))
				diction_3[Diseases_name[j]][0] = 'none'
				diction_3[Diseases_name[j]][1] = 'N'
				diction_3[Diseases_name[j]][2] = 'none'
				diction_3[Diseases_name[j]][3] = 'N'						
		
		# print diction_1 #Outputpart
		# print diction_2 #Outputpart
		# print diction_3 #Outputpart

		outputFile.write(str(diction_1) + '\r\n')
		outputFile.write(str(diction_2) + '\r\n')
		outputFile.write(str(diction_3) + '\r\n')
""" Main Part """
outputFile = open(inputFile_name_without_kind + '_inference.txt', 'w')
Problem()
outputFile.close()
