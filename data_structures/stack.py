class Stack:
    def __init__(self, para=[]):
      self.stack = para
      pass

    def push(self,newElement):
      self.stack.append(newElement)
    #  return self.para.append(self,newElement)

    def pop(self):
      last.element = self.stack[len(self.stack)-1]
      self.stack.remove(len(self.stack)-1)
      return last.element

    def top(self):
      self.stack[len(self.stack)-1]

    def isEmpty(self):
      len(self.stack)==0

    def display_stack(self):
      print(self.Stack)
