class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next
  def __repr__(self):
    return f"{self.value}"

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # TO BE COMPLETED
    # if the list only has none values
    # if self.head == None:
    #   return None
    # # for n in list ???


    # prev_node = None
    # curr_node = self.head # 1
    # nn = self.head.next_node # 2

    # while curr_node.next_node is not None: 
    #   curr_node.next_node = prev_node # 2 -> none
    #   prev_node = curr_node # none -> 1
    #   curr_node = nn # 1 -> 2
    #   nn = curr_node.next_node # 2 -> none
    # curr_node.next_node = prev_node # none -> 1
    # return curr_node 

    prev_node = None
    curr_node = self.head
    while curr_node is not None: 
      nn = curr_node.next_node
      curr_node.next_node = prev_node
      prev_node = curr_node
      curr_node = nn
    self.head = prev_node






test = LinkedList()
test.add_to_head(1) # 1
test.add_to_head(2) # 1, 2
test.add_to_head(3) # 1, 2, 3
test.add_to_head(4) # 1, 2, 3, 4
test.add_to_head(5) # 1, 2, 3, 4, 5
print(f"test.reverse_list(): {test.reverse_list()}")