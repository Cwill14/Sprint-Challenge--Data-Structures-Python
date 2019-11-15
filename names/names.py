import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# names = names_1 + names_2
duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
# #             duplicates.append(name_1)
# bst = BinarySearchTree()
# bst.insert(names_1)
# bst.insert(names_2)

# def find_duplicates(x):
#     # if x already exists, ??????
#     # if 
#     # append to duplicates
#     pass
# print(type(names_1))
# print(type(names_2))
# print(type(names))
# bst.insert(*names)
# for n in names:
#     bst.insert(n)
# bst.for_each(find_duplicates)
# bst.contains
# bst.in_order_print(bst)
bst1 = BinarySearchTree()
bst2 = BinarySearchTree()
for n in names_1:
    bst1.insert(n)
for n in names_2:
    bst2.insert(n)
for n in names_1:
    if bst1.contains(n) and bst2.contains(n):
        duplicates.append(n)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# run time at beginning is O(n^2) I believe, 
# because it has a nested for loop inside a for loop.

# my first solution is O(n) I believe, because
# I have to for loops inserting into the bst (each is O(n))
# and then I have a for loop that loops over the first list(O(n)),
# but then the contains is O(log n) because of it's binary search
# at least it runs in well under a second

# actually, because the the O(log n) is inside of O(n) loop, that means my first solution is O(n log n)