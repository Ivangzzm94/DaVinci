class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def top(self):
         if len(self.items) > 0:
            return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)