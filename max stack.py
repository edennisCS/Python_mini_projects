# max stack

class MaxStack:
  def __init__(self):
    self.items = []

  def push(self, val):
    self.items.append(val)

  def pop(self):
    return self.items.pop()

  def max(self):
      if self.items:
          myMax = float('-inf')
          for i in self.items:
              if i > myMax:
                  myMax = i
          return myMax
      else:
          return None

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print (s.max())
# 3
s.pop()
s.pop()
print (s.max())
# 2
