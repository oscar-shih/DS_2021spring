import Median
if __name__== '__main__':
	with open("0002.txt", "w") as output:
		a = [3, 4, 6, 21, 10, 7, 8, 22, 28, 13, 19, 25, 20]
		M = Median.FindMedian()
		M.AddNewValues(a)
		output.write(str(M.ShowMedian()) + "\n")
		M.RemoveMedianRelatedValue()
		output.write(str(M.ShowMedian()))
