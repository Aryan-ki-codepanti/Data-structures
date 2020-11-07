
class Stack:

	""" This class implements stack methods using an array."""


	def __init__(self,stk=None):

		""" To create  an instance of  stack,we need to pass an array of items or if nothing is passed
			empty stack is created . Also an instance variable namely top is
			assigned to None if empty stack else len(stack)-1"""

		if stk is None:
			self.stk = []
			self.top = None
		else:
			self.stk = stk
			self.top = len(stk) - 1

	def is_empty(self):

		"""This method return boolean True if stack is empty else boolean False"""
		return self.stk == []


	def push(self,node):

		""" This method takes instance and a node as arguments and pushes node to end of stack """

		if self.is_empty():
			self.stk.append(node)
			self.top = 0

		else:
			self.stk.append(node)
			self.top += 1


	def pop(self):

		""" This method takes only instance of stack as argument and 
			returns Underflow string if stack is empty 
			else removes last added item from stack and return it"""

		if self.is_empty():
			return "Underflow"

		elif self.top == 0:
			self.top = None
			return self.stk.pop()

		else:
			self.top -= 1
			return self.stk.pop()

	def peek(self):

		"""This method takes only instance of stack as argument and returns topmost element 
			(without removing it) if stack is not empty 
			else returns empty stack string"""

		if self.is_empty():
			return "Empty stack"
		else:
			return self.stk[self.top]

	def display(self):

		"""This method takes only instance of stack as argument 
			displays whole starting from top to lowermost element line by line if stack has element(s)
			else print 'Empty stack' string"""

		if self.is_empty():
			print("Empty stack")
		else:
			print(f"{self.stk[self.top]} <- TOP")

			for i in range(self.top-1,-1,-1):
				print(self.stk[i])


	def __repr__(self):

		"""For representing stack instance, returns string in a 
			format similar to that was used to create instance of stack """
		return f"Stack({self.stk})"

	def __str__(self):
		"""This method returns general info of stack giving total elements in it , and  topmost level"""
		return f"Elements: {len(self.stk)} ,Top : {self.top}"


#Now a menu driven program which allows user to interact with Stack
print("1.Want to initialize stack elements?")
print("2.By Default: Want a new one")
want = input()
if want == "1":
	elements = input("Enter space separated initial elements: ")
	a = Stack(elements.split(' '))
else:
	a = Stack()
while True:
	print()
	print("-"*80)
	print("Welcome to stack menu!")
	print("Make a choice")
	print()
	print("1.PUSH a node")
	print("2.POP a node")
	print("3.DISPLAY stack")	
	print("4.PEEK")
	print("5.EXIT Program")

	c = input()
	if c == "5":
		break

	elif c == "1":
		item = input("Enter item to be pushed in stack: ")
		a.push(item)
	elif c == "2":
		x = a.pop()
		if x == "Underflow":
			print(x)
		else:
			print(f"Poped item -> {x}")
	elif c == "3":
		a.display()

	elif c == "4":
		res = a.peek()
		if res == "Empty stack":
			print(res)
		else:
			print(f"Topmost element: {res}")
	else:
		print("Make a valid choice")
	print(repr(a),str(a))
	

