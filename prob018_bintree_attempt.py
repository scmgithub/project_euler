# coding=utf-8
# Maximum path sum I
# Problem 18

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

#    3
#   7 4
#  2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

#                             75
#                           95  64
#                         17  47  82
#                       18  35  87  10
#                     20  04  82  47  65
#                   19  01  23  75  03  34
#                 88  02  77  73  07  63  67
#               99  65  04  28  06  16  70  92
#             41  41  26  56  83  40  80  70  33
#           41  48  72  33  47  32  37  16  94  29
#         53  71  44  65  25  43  91  52  97  51  14
#       70  11  33  28  77  73  17  78  39  68  17  57
#     91  71  52  38  17  14  91  43  58  50  27  29  48
#   63  66  04  68  89  53  67  30  73  16  69  87  40  31
# 04  62  98  27  23  09  70  98  73  93  38  53  60  04  23

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)


#  This binary tree implementation really isn’t working out, and isn’t necessary to solve the problem.


class BinaryTree():
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

  def getLeftChild(self):
    return self.left

  def getRightChild(self):
    return self.right

  def setNodeValue(self, value):
    self.value = value

  def getNodeValue(self):
    return self.value

  def insertIntoTree(self, value):
    print "in insertIntoTree:", self.getNodeValue(), "value:", value
    print "this tree's value is ", self.getNodeValue()
    print "left child value is ", self.getLeftChild()

    # simply find the next open spot and add a tree with that value there.
    #  make no assumption about "searchability".
    if self.left is None:
      print "we see self.left is None.  Inserting", value
      subTree = BinaryTree(value)
      self.left = subTree
    else:
      print "no dice.  trying right side."
      if self.right is None:
        print "self.right is None.  Inserting", value
        subTree = BinaryTree(value)
        self.right = subTree
      else:  # current node's children are full; traversing...

        # I have to figure out when to traverse left vs right.  This is weird.

        print "RECURSING LEFT!  LOOK OUT!"
        self.left.insertIntoTree(value)


def printTree(tree):
  if tree != None:
    printTree(tree.getLeftChild())
    print(tree.getNodeValue())
    printTree(tree.getRightChild())

def testTree():
  tTree = BinaryTree("Steve")
  printTree(tTree)
  tTree.insertIntoTree("Christine")
  tTree.insertIntoTree("Molly")
  tTree.insertIntoTree("Kat")
  tTree.insertIntoTree("Ros")
  # tTree.insertIntoTree("Nyle")
  # tTree.insertIntoTree("Nicole")

  # tTree.insertIntoTree("Elaine")
  # tTree.insertIntoTree("Stoya")
  # tTree.insertIntoTree("Bridget")
  # tTree.insertIntoTree("Gretchen")
  # tTree.insertIntoTree("Emily")
  # tTree.insertIntoTree("Daisy")
  # tTree.insertIntoTree("Krysten")
  # tTree.insertIntoTree("Mandy")
  printTree(tTree)

testTree()






