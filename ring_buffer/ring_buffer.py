class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    self.current += 1
    if self.current == self.capacity:
      self.current = 0

  def get(self):
    result = []
    for i in self.storage:
      if i != None:
        result.append(i)
    return result
  
test1 = RingBuffer(5)
test1.append('a')
test1.append('b')
test1.append('c')
test1.append('d')
print(f"test1.get: {test1.get()} should equal ['a', 'b', 'c', 'd']")