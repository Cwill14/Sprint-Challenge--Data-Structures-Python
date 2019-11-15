# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value=''):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if self.left and self.right != None:
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # to search a give key in Binary Search Tree, we first compare it with root
        # if the key is present at root, we return root. if key is greater than root's key,
        # we recur for right subtree of root node. Otherwise we recur for left subtree.
        # print(f"self.value: {self.value}")
        # print(f"target: {target}")
        if target == self.value:
            return True
        elif target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            if self.left:
                return self.left.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        # go right until you can go right no further, then you shall find what you seek
        while self.right:
            self = self.right
        return self.value

        # return self.right.get_max() if self.right else self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # go left until you can't anymore
        # go back and go right somehow
        # in here somewhere, you want to call cb(node)
        # if we have a left and no right
           # recursively call left
        # if we have a right and no left
           # recursively call right
        # if we have both
        #     call for both
        # if neither, we only have one node
        #     call on self
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node is None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # make queue
        # push root into queue
        # while queue not empty
        #     if left
        #         add left to back
        #     if right
        #         add right to back
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # make Stack
        # put the root in the Stack
        # while stack is not empty
        #     pop the top item in the stack
        #     look right
        #     push right to stack
        #     look left
        #     if there is a left, push to stack
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# test = BinarySearchTree(5)

# # contains #
# print(f"{test.insert(2)} inserted 2")
# print(f"{test.insert(3)} inserted 3")
# print(f"{test.insert(7)} inserted 7")
# # print(f"test.value: {test.value}")
# print(f"test.contains(7): {test.contains(7)} == true? ")
# print(f"test.contains(8): {test.contains(8)} == false? ")

