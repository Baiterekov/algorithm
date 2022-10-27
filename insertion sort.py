import random

arr = []

change1 = 0
change2 = 0
index = 0

for i in range(0, 10):
	arr.append(random.randint(1,10))
print(arr)
for i in range(0, len(arr)):
	change1 = arr[i]
	index = i
	# print()
	# print("///////////   ", i, "   ///////////")
	# print()
	for j in range(0, i+1):
		if change1<arr[i-j]:
			change2 = arr[i-j]
			arr[i-j]=change1
			arr[index] = change2
			change1 = arr[i-j]
			index = i-j
			
		# print(arr)		
print(arr)
	
# for i in range(0, 10):
# 	for j in range(0, i+1):
# 		print(i-j)
# 	print("////////////////  ", i)
