""" READ THE INPUT FILE """
import sys
inputFile = open(sys.argv[2])
DataFile = open(sys.argv[4])

input_string = []
for line in inputFile:
	input_string.append(line)
inputFile.close()

Data_string = []
for line in DataFile:
	Data_string.append(line)
DataFile.close()

""" Build The Data Struct """
# For First Line in input
Query_Num = int(input_string[0])
Query_List = []
for i in range (1, len(input_string)):
	Query_List.append(eval(input_string[i]))

# For First Line in Data
Name_of_the_Fields = Data_string[0].split()

Data_Information_List = []
for i in range (1, len(Data_string)):
	Data_Information_List.append(Data_string[i].split())

# Useful Data Struct
Case_Num = len(Data_Information_List)

income_P = [0] * 4
exercise_P = [0] * 2
smoke_P = [0] * 2
bmi_P = [0] * 4
bp_P = [0] * 2
cholesterol_P = [0] * 2
angina_P = [0] * 2
attack_P = [0] * 2
stroke_P = [0] * 2
diabetes_P = [0] * 2

exercise_income_P = [0] * 4
""" Useful Fuctions """
def Construct_CPT():
	# CountNumber
	for i in range (0, Case_Num):
		# Count Income num
		Data_Information_List[i][0] = int(Data_Information_List[i][0])
		if 0 <= Data_Information_List[i][0] and Data_Information_List[i][0] <= 25000:
			income_P[0] += 1
		elif 25001 <= Data_Information_List[i][0] and Data_Information_List[i][0] <= 50000:
			income_P[1] += 1
		elif 50001 <= Data_Information_List[i][0] and Data_Information_List[i][0] <= 75000:
			income_P[2] += 1
		elif 75000 < Data_Information_List[i][0]:
			income_P[3] += 1
		# Count exercise num
		if Data_Information_List[i][1] == 'yes':
			exercise_P[0] += 1
		elif Data_Information_List[i][1] == 'no':
			exercise_P[1] += 1
		# Count smoke num
		if Data_Information_List[i][2] == 'yes':
			smoke_P[0] += 1
		elif Data_Information_List[i][2] == 'no':
			smoke_P[1] += 1
		# Count bmi num
		if Data_Information_List[i][3] == 'underweight':
			bmi_P[0] += 1
		elif Data_Information_List[i][3] == 'normal':
			bmi_P[1] += 1
		elif Data_Information_List[i][3] == 'overweight':
			bmi_P[2] += 1
		elif Data_Information_List[i][3] == 'obese':
			bmi_P[3] += 1
		# Count bp num
		if Data_Information_List[i][4] == 'yes':
			bp_P[0] += 1
		elif Data_Information_List[i][4] == 'no':
			bp_P[1] += 1
		# Count cholesterol num
		if Data_Information_List[i][5] == 'yes':
			cholesterol_P[0] += 1
		elif Data_Information_List[i][5] == 'no':
			cholesterol_P[1] += 1
		# Count angina num
		if Data_Information_List[i][6] == 'yes':
			angina_P[0] += 1
		elif Data_Information_List[i][6] == 'no':
			angina_P[1] += 1
		# Count attack num
		if Data_Information_List[i][7] == 'yes':
			attack_P[0] += 1
		elif Data_Information_List[i][7] == 'no':
			attack_P[1] += 1
		# Count stroke num
		if Data_Information_List[i][8] == 'yes':
			stroke_P[0] += 1
		elif Data_Information_List[i][8] == 'no':
			stroke_P[1] += 1
		# Count diabetes num
		if Data_Information_List[i][9] == 'yes':
			diabetes_P[0] += 1
		elif Data_Information_List[i][9] == 'no':
			diabetes_P[1] += 1
		
		# Count exercise and income num-----P(exercise|income[i])
		if 0 <= Data_Information_List[i][0] and Data_Information_List[i][0] <= 25000 and Data_Information_List[i][1] == 'yes':
			exercise_income_P[0] += 1
		elif 25001 <= Data_Information_List[i][0] and Data_Information_List[i][0] <= 50000 and Data_Information_List[i][1] == 'yes':
			exercise_income_P[1] += 1
		elif 50001 <= Data_Information_List[i][0] and Data_Information_List[i][0] <= 75000 and Data_Information_List[i][1] == 'yes':
			exercise_income_P[2] += 1
		elif 75000 < Data_Information_List[i][0] and Data_Information_List[i][1] == 'yes':
			exercise_income_P[3] += 1

	# Compute income_P
	for i in range (0, len(income_P)):
		income_P[i] = float(income_P[i])
		income_P[i] = income_P[i] / Case_Num
	# Compute exercise_P
	for i in range (0, len(exercise_P)):
		exercise_P[i] = float(exercise_P[i])
		exercise_P[i] = exercise_P[i] / Case_Num
	# Compute smoke_P
	for i in range (0, len(smoke_P)):
		smoke_P[i] = float(smoke_P[i])
		smoke_P[i] = smoke_P[i] / Case_Num
	# Compute smoke_P
	for i in range (0, len(bmi_P)):
		bmi_P[i] = float(bmi_P[i])
		bmi_P[i] = bmi_P[i] / Case_Num
	# Compute bp_P
	for i in range (0, len(bp_P)):
		bp_P[i] = float(bp_P[i])
		bp_P[i] = bp_P[i] / Case_Num
	# Compute cholesterol_P
	for i in range (0, len(cholesterol_P)):
		cholesterol_P[i] = float(cholesterol_P[i])
		cholesterol_P[i] = cholesterol_P[i] / Case_Num
	# Compute angina_P
	for i in range (0, len(angina_P)):
		angina_P[i] = float(angina_P[i])
		angina_P[i] = angina_P[i] / Case_Num
	# Compute attack_P
	for i in range (0, len(attack_P)):
		attack_P[i] = float(attack_P[i])
		attack_P[i] = attack_P[i] / Case_Num
	# Compute stroke_P
	for i in range (0, len(stroke_P)):
		stroke_P[i] = float(stroke_P[i])
		stroke_P[i] = stroke_P[i] / Case_Num
	# Compute diabetes_P
	for i in range (0, len(diabetes_P)):
		diabetes_P[i] = float(diabetes_P[i])
		diabetes_P[i] = diabetes_P[i] / Case_Num

	# Compute P(exercise|income[i])
	for i in range (0, len(income_P)):
		exercise_income_P[i] = float(exercise_income_P[i])
		exercise_income_P[i] = income_P[i] / Case_Num


	print income_P
	print exercise_P
	print smoke_P
	print bmi_P
	print bp_P
	print cholesterol_P
	print angina_P
	print attack_P
	print stroke_P
	print diabetes_P

""" Main Part """
Construct_CPT()
print '\r'
