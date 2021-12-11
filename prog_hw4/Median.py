## Important! You shouldn't use statistics library! ("import statistics" is not allowed)
import math
class MinHeap: #Please store and implement MinHeap data structure with an array
    def __init__(self):
        self.array = []
        self.size = 0
    def getSize(self):
        return self.size
    def parent(self, pos):
        if pos == 0:
            return 0
        return (pos - 1) // 2
    def left_child(self, pos):
        return (2 * pos) + 1
    def right_child(self, pos):
        return (2 * pos) + 2
    def leaf(self, pos):
        if pos >= self.size // 2 and pos <= self.size:
            return True
        return False
    def swap(self, pos1, pos2):
        self.array[pos1], self.array[pos2] = self.array[pos2], self.array[pos1]
    def min_heapify(self, pos):
        if not self.leaf(pos):
            if self.left_child(pos) < self.size - 1:
                # both left_child and right_child exist.
                if self.array[pos] > self.array[self.left_child(pos)] or self.array[pos] > self.array[self.right_child(pos)]:
                    if self.array[self.left_child(pos)] < self.array[self.right_child(pos)]:
                        self.swap(pos, self.left_child(pos))
                        self.min_heapify(self.left_child(pos))
                    else:
                        self.swap(pos, self.right_child(pos))
                        self.min_heapify(self.right_child(pos))
            else:
                # only left_child exists.
                if self.array[pos] > self.array[self.left_child(pos)]:
                    self.swap(pos, self.left_child(pos))
    def insert(self, item): #insert new item        
    ### TODO ### 
    ### input: a value ###
    ### You need not return or print anything with this function. ###
        self.array.append(item)
        cur = self.size
        while self.array[cur] < self.array[self.parent(cur)]:
            self.swap(cur, self.parent(cur))
            cur = self.parent(cur)
        self.size += 1
    def peek(self):  #Find Minimum item
        if self.size == 0:
            return
        else:
            return self.array[0]
    def removeMin(self):
    ### TODO ###
    ### You need not return or print anything with this function. ###
        if len(self.array) > 1:
            self.array[0] = self.array.pop()
            self.size -= 1
            self.min_heapify(0)
        else:
            self.array.pop(0)
    def showMinHeap(self):  #Show MinHeap with array
        return self.array
class MaxHeap: #Please store and implement MinHeap data structure with an array
    def __init__(self):
        self.array = []
        self.size = 0
    def getSize(self):
        return self.size
    def parent(self, pos):
        if pos == 0:
            return 0
        return (pos - 1) // 2
    def left_child(self, pos):
        return (2 * pos) + 1
    def right_child(self, pos):
        return (2 * pos) + 2
    def leaf(self, pos):
        if pos >= self.size // 2 and pos <= self.size:
            return True
        return False
    def swap(self, pos1, pos2):
        self.array[pos1], self.array[pos2] = self.array[pos2], self.array[pos1]
    def max_heapify(self, pos):
        if not self.leaf(pos):
            if self.left_child(pos) < self.size - 1:
                # both right_child and left_child exist.
                if self.array[pos] < self.array[self.left_child(pos)] or self.array[pos] < self.array[self.right_child(pos)]:
                    if self.array[self.left_child(pos)] > self.array[self.right_child(pos)]:
                        self.swap(pos, self.left_child(pos))
                        self.max_heapify(self.left_child(pos))
                    else:
                        self.swap(pos, self.right_child(pos))
                        self.max_heapify(self.right_child(pos))
            else:
                # only left_child exists.
                if self.array[pos] < self.array[self.left_child(pos)]:
                    self.swap(pos, self.left_child(pos))
    def insert(self, item): #insert new item
    ### TODO ###
    ### input: a value ###
    ### You need not return or print anything with this function. ###
        self.array.append(item)
        cur = self.size
        while self.array[cur] > self.array[self.parent(cur)]:
            self.swap(cur, self.parent(cur))
            cur = self.parent(cur)
        self.size += 1
    def peek(self):    #Find Maximum item
        if self.size == 0:
            return
        else:
            return self.array[0]
    def removeMax(self):   #Find Maximum item
    ### TODO ###
    ### You need not return or print anything with this function. ###
        if len(self.array) > 1:
            self.array[0] = self.array.pop()
            self.size -= 1
            self.max_heapify(0)
        else:
            self.array.pop(0)
    def showMaxHeap(self):   #Show MaxHeap with array
        return self.array
class FindMedian: 
    def __init__(self):
    ### TODO ###
    ### Your own data structure. Implementing with heap structure is highly recommended. ###
        self.down = MaxHeap()
        self.up = MinHeap()
        pass
    def AddNewValues(self, NewValues):  # Add NewValues(a list of items) into your data structure
    ### TODO ### 
    ### input: a list of values ###
    ### You need not return or print anything with this function. ###
        for i in NewValues:
            if (self.down.size <= 0 and self.up.size <= 0) or self.down.array[0] > i:
                self.down.insert(i)
            else:
                self.up.insert(i)
            if self.down.size - self.up.size > 1:
                tmp = self.down.array[0]
                self.down.removeMax()
                self.up.insert(tmp)
            elif self.up.size - self.down.size > 1:
                tmp = self.up.array[0]
                self.up.removeMin()
                self.down.insert(tmp)
        pass
    def ShowMedian(self):  # Show Median of your data structure
    ### TODO ### 
    ### You need not print anything but "return Median". ###
        if self.down.size <= 0 and self.up.size <= 0:
            return
        elif self.down.size > self.up.size:
            return float(self.down.array[0])
        elif self.down.size < self.up.size:
            return float(self.up.array[0])
        else:
            return 0.5 * float(self.up.array[0] + self.down.array[0])
        pass
    def RemoveMedianRelatedValue(self): # Remove value(s) related with median: odd (1), even (2)
    ### TODO ###
    ### You need not return or print anything with this function. ###
        if self.down.size <= 0 and self.up.size <= 0:
            return
        elif self.down.size >= self.up.size:
            self.down.removeMax()
        elif self.down.size <= self.up.size:
            self.up.removeMin()
        pass