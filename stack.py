class Stack:
    def __init__(self):
        self.items = []
        
    def pop(self):
        return self.items.pop()
        
    def push(self, x):
        self.items.append(x)
        
s = Stack()
nums = [1, 2, 3, 4, 5]
new_nums = []
for i in nums:
    s.push(i)
    
for i in range(len(nums)):
    new_nums.append(s.pop())
    
print(new_nums)