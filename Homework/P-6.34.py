#-------------P6.34--------------------

# Class to convert the expression
class Evaluate:
   def __init__(self, capacity):
       self.top = -1
       self.capacity = capacity
       self.array = []

# check if the stack is empty

   def isEmpty(self):
       return True if self.top == -1 else False


   def peek(self):
      return self.array[-1]

# Pop the element from the stack
   def pop(self):
      if not self.isEmpty():
          self.top -= 1
          return self.array.pop()
      
# Push the element to the stack
   def push(self, op):
      self.top += 1
      self.array.append(op)

# The main function
   def evaluatePostfix(self, exp):
      for i in exp:
          if i.isdigit():
              self.push(i)
          else:
              val1 = self.pop()
              val2 = self.pop()
              self.push(str(eval(val2 + i + val1)))
      return (self.pop())

# expression
exp = "52+83-*4/"

obj = Evaluate(len(exp))
print(f"Value of {exp} is {obj.evaluatePostfix(exp)}")
#Value of 52+83-*4/ is 8.75