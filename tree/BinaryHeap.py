class BinHeap:
	def __init__(self):
		self.heaplist = [0]
		self.currentsize = 0
	def percUp(self,i):
		while i//2 >0:
			if self.heaplist[i] < self.heaplist[i//2]:
				tmp = self.heaplist[i//2]
				self.heaplist[i//2] = self.heaplist[i]
				self.heaplist[i] = tmp
			i = i//2
	def incert(self,k):
		self.heaplist.append(k)
		self.currentsize = self.currentsize +1 
		self.percUp(self.currentsize)

	def percDown(self,i):
		while (i*2) <= self.currentsize
		mc = self.minChild(i)
		if self.heaplist[i] >self.heaplist[mc]
			tmp = self.heaplist[i]
			self.heaplist[i] = self.heaplist[mc]
			self.heaplist[mc] = tmp
	def minChild(self,i):
		if i*2 +1 > self.currentsize:
			return i*2
		else:
			if self.heaplist[i*2]<self.heaplist[i*2+1]:
				return i*2
			else:
				return i*2+1
	def delMin(self):
		retval = self.heaplist[1]
		self.heaplist[1] = self.heaplist[self.currentsize]
		self.currentsize = self.currentsize - 1
		self.heaplist.pop()
		self.percDown(1)
		return retval

	def buildHeap(self,alist):
		i = len(alist)//2
		self.currentsize = len(alist)
		self.heaplist = [0] + alist[:]
		print(len(self.heaplist),i)
		while(i>0):
			print(self.heaplist,i)
			self.percDown(i)
			i = i-1
		print(self.heaplist,i)
		