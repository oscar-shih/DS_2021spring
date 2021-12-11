import Median
if __name__== '__main__':
	with open("0001.txt", "w") as output:
		heap1 = Median.MinHeap()
		heap2 = Median.MaxHeap()
		a = [3, 4, 6, 21, 10, 7, 8, 22, 28, 13, 19, 25, 20]
		for i in a:
			heap1.insert(i)
			for n in heap1.showMinHeap():
				output.write(str(n) + " ")
			output.write("\n")
		heap1.removeMin()
		for n in heap1.showMinHeap():
			output.write(str(n) + " ")
		output.write("\n")
		for i in a:
			heap2.insert(i)
			for n in heap2.showMaxHeap():
				output.write(str(n) + " ")
			output.write("\n")
