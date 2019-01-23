import random
import csv

def gen_mult(mode):
	if mode == 'easy':
		num1 = random.randint(1,9)
		num2 = random.randint(31,78)
	if mode == 'hard':
		num1 = random.randint(121,343)
		num2 = random.randint(242,352)
	ans = num1 * num2
	array = [str(num1)+" x ",num2,ans]
	return array

def gen_add():
	num1 = random.randint(11,59)
	num2 = random.randint(11,41)
	ans = num1 + num2
	array = [str(num1)+" + ",num2,ans]
	return array

if __name__ == '__main__':
	with open('task.csv', 'w') as csv_file:
		filednames = ['question', 'answer']
		writer = csv.DictWriter(csv_file, fieldnames=filednames)
		writer.writeheader()
		ran = 33
		for i in range(100):
			# if i < ran :
			# 	if i % 6 == 0:
			# 		arr = gen_mult('easy')
			# 	else:
			# 		arr = gen_add()
			if i >= ran and i % 7 == 0:
				arr = gen_mult('hard')
			else:
				if i % 6 == 0:
					arr = gen_mult('easy')
				else:
					arr = gen_add()
			writer.writerow({'question': str(arr[0])+ str(arr[1]) +" = ", 'answer': str(arr[2])})