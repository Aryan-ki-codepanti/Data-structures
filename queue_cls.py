
class Queue:

	""" This class implements Queue methods using an array"""

	def __init__(self,que=None):

		""" This constructor creates an instance of queue.
			if an array is passed to it then queue is initialized with it
			otherwise it creates an empty queue"""

		if que is None:
			self.que = []
			self.front = self.back = None
		else:
			self.que = que
			self.front = 0
			self.back = len(que) - 1

	def is_empty(self):
		"""This method takes instance of queue as argument and return boolean True if its empty
			else boolean False """
		return self.que == []

	def enqueue(self,node):

		""" This method takes instance of queue and an item as arguments and item is appended into queue"""

		if self.is_empty():
			self.que.append(node)
			self.front = self.back = 0

		else:
			self.que.append(node)
			self.back += 1

	def dequeue(self):

		"""This method only takes instance of queue as an argument and 
			return front element(after its removal from queue) if queue has element(s) 
			else it returns 'Underflow' str"""

		if self.is_empty():
			return "Underflow"

		else:
			if len(self.que) == 1:

				self.front = self.back = None
				return self.que.pop(0)

			else:
				self.back -= 1
				return self.que.pop(0)

	def peek(self,side='f'):

		"""This method takes instance of queue as an argument and default argument side ,
			if side is provided as 'b' then element from back of queue is returned (without removing it queue)
			else element from front of queue is returned (without removing it from queue)"""

		if self.is_empty():
			return "Empty queue"
		elif side == 'f':
			return self.que[self.front]
		else:
			return self.que[self.back]


	def display(self):
		""" This method displays whole queue from front to back in single line if it has element(s)
			else it prints 'Empty queue' string """
		if self.is_empty():
			print("Empty queue")

		elif self.front == self.back: #single element
			print(f"Front-> {self.que[self.back]} <-Back")

		else:
			print(f"Front-> {self.que[self.front]}",end=" ")
			for i in range(self.front+1,self.back):
				print(self.que[i],end=" ")
			print(f"{self.que[self.back]} <-Back")

	def __str__(self):
		""" This method returns string of general info about queue that are
			 number of elements in it,its front and back"""
		return f"Elements: {len(self.que)},front: {self.front},back: {self.back}"

	def __repr__(self):
		"""This method returns a string describing queue instance in a format similar 
		to that used at time of creating its instance"""
		return f"Queue({self.que})"


#Now a menu driven program which allows user to interact with Queues
print("Choose any one")
print("1.Want to initialise queue ")
print("2.Create new empty queue")
want = input()

if want == "1":
	elements = input("Enter space separated items in queue from front to back: ")
	queue = Queue(elements.split(' '))
else:
	queue = Queue()


while True:
	print("-"*70)
	print("Welcome to queue menu!!!  Make a choice")
	print("1.Insertion (Enqueue)")
	print("2.Deletion (Dequeue)")
	print("3.Peeking (Checking front or back)")
	print("4.Display whole queue")
	print("5.To check if its empty")
	print("6.Exit")

	c = input()

	if c == '6':
		break

	elif c == '1':
		item = input("Enter element you wana insert to queue: ")
		queue.enqueue(item)

	elif c == '2':
		x = queue.dequeue()

		if x == "Underflow":
			print(x)
		else:
			print("Deleted item: {}".format(x))

	elif c == '3':
		s = input("Enter  front(f) or back(b): ")

		res = queue.peek(s)
		if res == "Empty queue":
			print(res)
		else:
			if s == 'b' or s != 'f':
				print("Back element: {}".format(res))
			else:
				print("Front element: {}".format(res))

	elif c == '4':
		queue.display()

	elif c == '5':
		if queue.is_empty():
			print("Its empty")
		else:
			print("Its not empty")
			
	else:	
		print("Make a valid choice")

	print(repr(queue),str(queue))
