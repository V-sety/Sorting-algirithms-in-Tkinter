import time
def bubbleSort(array, drawArr):
	if len(array) == 1:
		return array
	l = len(array)-1
	while l !=0:
		for i in range(l):
			if array[i] > array[i+1]:
				array[i],array[i+1] = array[i+1],array[i]
				drawArr(array, ["pink" if x ==i or x ==i+1 else "dark red" for x in range(len(array))])
				time.sleep(0.3)
		l = l-1
	drawArr(array, ["pink" for _ in range(len(array))])
	

def insertionSort(array, drawArr):
	for i in range(1, len(array)):
		x = array[i]
		j=i
		while x < array [j-1] and j > 0:
			array[j]=array[j-1]
			drawArr(array, ["pink" if n ==i or n == j else "dark red" for n in range(len(array))])
			time.sleep(0.3)
			j = j-1
		array[j] = x
	drawArr(array, ["pink" for _ in range(len(array))])

def selectionSort(array, drawArr):
	for j in range(len(array)):
		m = 0
		x = array[j]
		for i in range(j,len(array)):
			drawArr(array, ["pink" if n ==i or n == j else "dark red" for n in range(len(array))])
			time.sleep(0.3)
			if array[i] < x:
				x = array[i]
				m = i
		if m !=0: 
			array[m],array[j] = array[j],array[m]
	drawArr(array, ["pink" for _ in range(len(array))])

def quickSort(array, drawArr):
	helper(array, 0 , len(array) - 1,drawArr)
	
def helper(array,start,end,drawArr):
	if start >= end:
		return 
	pivot = start
	left = start + 1
	right = end
	while left <= right:
		if array[left] > array[pivot] and array[right] < array[pivot]:
			array[left],array[right] = array[right],array[left]
			drawArr(array, ["pink" if n ==left or n == right or n == pivot else "dark red" for n in range(len(array))])
			time.sleep(0.3)
		if array[left] <= array[pivot]:
			drawArr(array, ["pink" if n ==left or n == right or n == pivot else "dark red" for n in range(len(array))])
			time.sleep(0.3)
			left +=1
		if array[right] >= array[pivot]:
			drawArr(array, ["pink" if n ==left or n == right or n == pivot else "dark red" for n in range(len(array))])
			time.sleep(0.3)
			right -=1
	array[pivot],array[right] = array[right],array[pivot]
	leftIsSmaller = (right - 1) - start < end - (right + 1)
	if leftIsSmaller:
		helper(array, start , right - 1,drawArr)
		helper(array, right + 1, end, drawArr)
	else:
		helper(array, right + 1, end, drawArr)
		helper(array, start , right - 1, drawArr)
	drawArr(array, ["pink" for _ in range(len(array))])