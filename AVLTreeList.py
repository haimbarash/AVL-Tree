"""AVL Tree List implementation,
a self-balancing binary search tree,
uses for efficient storage and retrieval of a list of elements"""

import random

"""A class representing a node in an AVL tree"""
class AVLNode(object):
	"""Constructor, you are allowed to add more fields.
	@type value: str
	@param value: data of your node
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.size = 1  # size of node's subtree
		self.bf = 0  # Balance Factor of node

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""
	def getLeft(self):
		return self.left

	"""returns the right child
	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):
		return self.right

	"""returns the parent 
	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):
		return self.parent

	"""return the value
	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):
		return self.value

	"""returns the height
	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def getHeight(self):
		if not self.isRealNode():  # Virtual node's height is -1
			return -1
		return max(self.left.getHeight(), self.right.getHeight()) + 1

	def getSize(self):
		return self.size

	def getBf(self):
		return self.bf

	"""sets left child
	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
		self.left = node

	"""sets right child
	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		self.right = node

	"""sets parent
	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
		self.parent = node

	"""sets value
	@type value: str
	@param value: data
	"""
	def setValue(self, value):
		self.value = value

	"""sets the balance factor of the node
	@type h: int
	@param h: the height
	"""
	def setHeight(self, h):
		self.height = h

	def setSize(self, size):
		self.size = size

	def setBf(self, bf):
		self.bf = bf

	"""returns whether self is not a virtual node 
	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		return self.value is not None  # Virtual node is defined to be a node with a value of None


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.
	"""
	def __init__(self):
		self.size = 0
		self.root = None

	"""Finds the rank of node using the rank algo taught
	COMPLEXITY: O(logn)"""
	def rank(self, node):
		rank = node.left.size + 1
		if node == self.root:
			return rank
		curr_node = node
		while curr_node.parent is not None:  # Until root reached
			if curr_node == curr_node.parent.right:
				rank += curr_node.parent.left.size + 1  # Current node + left subtree size added to rank
			curr_node = curr_node.parent
		return rank

	"""Returns the node of the requested rank using the select algo taught ( requested_rank >= 1)
	COMPLEXITY: O(logn)"""
	def select(self, node, requested_rank):
		if self.size == 0:  # No nodes in tree, no node will be found
			return None
		rank = node.left.size + 1
		if requested_rank == rank:
			return node
		elif requested_rank < rank:  # Searches for node in left subtree
			return self.select(node.left, requested_rank)
		else:  # Searches for node in right subtree
			return self.select(node.right, requested_rank - rank)

	"""finds the predecessor of node, using the predecessor algo taught
	COMPLEXITY: O(logn)"""
	def predecessor(self, node):
		if node.left.value is not None:  # Predecessor is max of left subtree
			node = node.left
			while node.right.value is not None:  # Finds max of left subtree
				node = node.right
			return node
		#  "the predecessor of x is the lowest ancestor y of x such that x is in its right subtree"
		curr_node = node.parent
		while curr_node.value is not None and node == curr_node.left:
			node = curr_node
			if node.parent is None:  # if no predecessor of node ( node is the first node in the tree)
				return None
			curr_node = node.parent
		return curr_node

	"""finds the successor of node, using the successor algo taught
	COMPLEXITY: O(logn)"""
	def successor(self, node):
		if node.right.value is not None:  # Successor is min of right subtree
			node = node.right
			while node.left.value is not None:  # Finds min of right subtree
				node = node.left
			return node
		#  "the successor of x is the lowest ancestor y of x such that x is in its left subtree"
		curr_node = node.parent
		while curr_node.value is not None and node == curr_node.right:
			node = curr_node
			if node.parent is None:  # if no successor of node ( node is the last node in the tree)
				return None
			curr_node = node.parent
		return curr_node

	"""creates two virtual children for node, since all tree nodes need to have 2 children"""
	def create_virtual_children(self, node):
		node.setLeft(AVLNode(None))  # Definition of virtual node is value = None
		node.left.parent = node
		node.left.size = 0  # Virtual node's size is 0
		node.setRight(AVLNode(None))
		node.right.parent = node
		node.right.size = 0

	"""returns whether the list is empty
	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		return self.size == 0

	"""retrieves the value of the i'th item in the list
	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	COMPLEXITY: O(logn)
	"""
	def retrieve(self, i):
		return self.select(self.root, i + 1).value

	"""inserts val at position i in the list
	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	COMPLEXITY: O(logn)
	"""
	def insert(self, i, val):
		rebalancing_amount = 0  # Amount of rotations
		if i == self.size:  # Insert-Last is being attempted
			max_node = self.select(self.root, self.size)
			if max_node is None:  # No max_node <-> empty tree. Root is created with 2 virtual children
				node = AVLNode(val)
				self.root = node
				self.root.height = 0
				self.create_virtual_children(node)
			else:
				max_node.right.value = val  # Right virtual node becomes real node
				self.create_virtual_children(max_node.right)  # Inserted node gets 2 children
				rebalancing_amount = self.fix_tree_insert(max_node.right)  # Rotations and size/height values are fixed
		else:
			curr_node = self.select(self.root, i + 1)
			if curr_node.left.value is None:  # Can be inserted as left child
				curr_node.left.value = val
				self.create_virtual_children(curr_node.left)
				rebalancing_amount = self.fix_tree_insert(curr_node.left)
			else:  # will be inserted as right child of predecessor
				predecessor = self.predecessor(curr_node)
				predecessor.right.value = val
				self.create_virtual_children(predecessor.right)
				rebalancing_amount = self.fix_tree_insert(predecessor.right)
		self.size += 1  # New node inserted, tree size += 1
		return rebalancing_amount

	"""After insertion, updates the height, the size, and performs rotations
	COMPLEXITY: O(logn)"""
	def fix_tree_insert(self, node):
		rebalancing_amount = 0
		rotate = True  # Is a rotation still a possibility
		while True:
			node.size = node.left.size + node.right.size + 1  # Size update
			prev_height = node.height
			node.height = max(node.left.height, node.right.height) + 1  # Height update
			node.bf = node.left.height - node.right.height  # Balance factor
			# If height didn't change, no need to rotate anymore
			if abs(node.bf) < 2 and prev_height == node.height and rotate:
				rotate = False
			elif abs(node.bf) < 2 and prev_height != node.height and rotate:
				pass
			elif abs(node.bf) == 2 and rotate:  # Rotation needs to be done
				rebalancing_amount += self.rotate(node)
				rotate = False
			if node.parent is None:  # Reached the root
				return rebalancing_amount
			node = node.parent

	"""According to the BFs, decides which rotations need to be performed"""
	def rotate(self, node):
		if node.left.value is not None:
			node.left.bf = node.left.left.height - node.left.right.height
		if node.right.value is not None:
			node.right.bf = node.right.left.height - node.right.right.height
		if node.bf == -2:
			if node.right.bf == -1 or node.right.bf == 0:
				self.left_rotate(node)
				return 1
			elif node.right.bf == 1:
				self.right_rotate(node.right)
				self.left_rotate(node)
				return 2
		elif node.bf == 2:
			if node.left.bf == -1:
				self.left_rotate(node.left)
				self.right_rotate(node)
				return 2
			elif node.left.bf == 1 or node.right.bf == 0:
				self.right_rotate(node)
				return 1

	"""Rotates the tree to the left using node"""
	def left_rotate(self, node):
		update_root = False  # Is the root the one being rotated (root.parent = None)
		if self.root == node:
			update_root = True
		right_node = node.right
		node.right = right_node.left
		node.right.parent = node
		right_node.left = node
		right_node.parent = node.parent
		if right_node.parent is not None:
			if right_node.parent.left == node:
				right_node.parent.left = right_node
			else:
				right_node.parent.right = right_node
		node.parent = right_node
		right_node.size = node.size  # Size updates
		node.size = node.left.size + node.right.size + 1
		node.height = max(node.left.height, node.right.height) + 1  # Height updates
		right_node.height = max(right_node.left.height, right_node.right.height) + 1
		if update_root:  # New root if root was being updated
			self.root = right_node

	"""Rotates the tree to the right using node"""
	def right_rotate(self, node):
		update_root = False  # Is the root the one being rotated (root.parent = None)
		if self.root == node:
			update_root = True
		left_node = node.left
		node.left = left_node.right
		node.left.parent = node
		left_node.right = node
		left_node.parent = node.parent
		if left_node.parent is not None:
			if left_node.parent.left == node:
				left_node.parent.left = left_node
			else:
				left_node.parent.right = left_node
		node.parent = left_node
		left_node.size = node.size  # Size updates
		node.size = node.left.size + node.right.size + 1
		node.height = max(node.left.height, node.right.height) + 1  # Height updates
		left_node.height = max(left_node.left.height, left_node.right.height) + 1
		if update_root:  # New root if root was being updated
			self.root = left_node

	"""deletes the i'th item in the list
	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	COMPLEXITY: O(logn)
	"""
	def delete(self, i):
		delete = self.select(self.root, i + 1)  # Finds the node that should be deleted
		if delete is None:
			return -1
		if delete == self.root and (delete.left.value is None or delete.right.value is None):
			rebalancing_amount = 0
			self.delete_root()
		elif delete.left.value is None and delete.right.value is None:  # No children
			parent = delete.parent  # Parent of deleted node
			# Parent of deleted node will have a new virtual child instead
			if parent.left == delete:
				parent.left = AVLNode(None)
				parent.left.parent = parent
				parent.left.size = 0
			else:
				parent.right = AVLNode(None)
				parent.right.parent = parent
				parent.right.size = 0
			rebalancing_amount = self.fix_tree_delete(parent)  # Rotations and height/size fixes are attempted
		elif delete.left.value is not None and delete.right.value is None:  # Left child only
			parent = delete.parent
			# Parent of the deleted node becomes parent of the child of the deleted node
			if parent.left == delete:
				parent.left = parent.left.left
				delete.left.parent = parent
			else:
				parent.right = parent.right.left
				delete.left.parent = parent
			rebalancing_amount = self.fix_tree_delete(parent)
		elif delete.left.value is None and delete.right.value is not None:  # Right child only
			parent = delete.parent
			# Parent of the deleted node becomes parent of the child of the deleted node
			if parent.left == delete:
				parent.left = parent.left.right
				delete.right.parent = parent
			else:
				parent.right = parent.right.right
				delete.right.parent = parent
			rebalancing_amount = self.fix_tree_delete(parent)
		else:  # Both children
			successor = self.successor(delete)
			# Successor's value is copied into the 'deleted' node, and successor node is deleted
			parent = successor.parent
			delete.value = successor.value
			if parent.left == successor:  # Successor is the left child of his parent
				parent.left = parent.left.right
				successor.right.parent = parent
			else:  # Successor is the right child of his parent
				parent.right = parent.right.right
				successor.right.parent = parent
			rebalancing_amount = self.fix_tree_delete(parent)
		self.size -= 1
		return rebalancing_amount

	"""Deletes the root node"""
	def delete_root(self):
		delete = self.root
		if delete.left.value is None and delete.right.value is None:  # No children
			self.root = None
		elif delete.left.value is not None and delete.right.value is None:  # Left child only
			self.root = delete.left
			delete.left.parent = None
		elif delete.left.value is None and delete.right.value is not None:  # Right child only
			self.root = delete.right
			delete.right.parent = None

	"""After deletion, updates the height, the size, and performs rotations
	COMPLEXITY: O(logn)"""
	def fix_tree_delete(self, node):
		rebalancing_amount = 0
		while True:
			node.size = node.left.size + node.right.size + 1  # Updates size
			node.height = max(node.left.height, node.right.height) + 1  # Updates height
			node.bf = node.left.height - node.right.height
			if abs(node.bf) < 2:  # No rotation needed
				pass
			elif abs(node.bf) == 2:  # Rotation needed
				rebalancing_amount += self.rotate(node)
			if node.parent is None:  # Reached root
				return rebalancing_amount
			node = node.parent

	"""returns the value of the first item in the list
	@rtype: str
	@returns: the value of the first item, None if the list is empty
	COMPLEXITY: O(logn)
	"""
	def first(self):
		if self.size == 0:
			return None
		return self.retrieve(0)

	"""returns the value of the last item in the list
	@rtype: str
	@returns: the value of the last item, None if the list is empty
	COMPLEXITY: O(logn)
	"""
	def last(self):
		if self.size == 0:
			return None
		return self.retrieve(self.size - 1)

	"""returns an array representing list 
	@rtype: list
	@returns: a list of strings representing the data structure
	COMPLEXITY: O(n)
	"""
	def listToArray(self):
		if self.size == 0:
			return []
		curr_node = self.root
		return self.list_to_array_rec([], curr_node)

	"""Executes in-order tree traversal
	COMPLEXITY: O(n)"""
	def list_to_array_rec(self, lst, curr_node):
		if curr_node.value is None:
			return
		self.list_to_array_rec(lst, curr_node.left)  # Adds left subtree to lst
		lst.append(curr_node.value)  # Adds node to lst
		self.list_to_array_rec(lst, curr_node.right)  # Adds right subtree to lst
		return lst

	"""returns the size of the list 
	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		return self.size

	"""sort the info values of the list
	@rtype: list
	@returns: an AVLTreeList where the values are sorted by the info of the original list.
	COMPLEXITY: O(nlogn)
	"""
	def sort(self):
		if self.size == 0:
			return AVLTreeList()
		lst = self.listToArray()
		self.merge_sort(lst)  # sorts lst
		new_tree = AVLTreeList()  # inserts lst to tree in order
		for i in range(len(lst)):
			new_tree.insert(i, lst[i])
		return new_tree

	"""sorts lst using the merge sort algorithm
	COMPLEXITY: O(nlogn)"""
	def merge_sort(self, lst):
		if len(lst) > 1:
			mid = len(lst)//2
			left = lst[:mid]
			right = lst[mid:]
			self.merge_sort(left)  # sorts the left list
			self.merge_sort(right)  # sorts the right list
			left_index = 0
			right_index = 0
			total_index = 0
			while left_index < len(left) and right_index < len(right):
				if left[left_index] <= right[right_index]:  # left element should be entered
					lst[total_index] = left[left_index]
					left_index += 1
				else:  # right element should be entered
					lst[total_index] = right[right_index]
					right_index += 1
				total_index += 1
			while left_index < len(left):  # rest of left elements should be entered
				lst[total_index] = left[left_index]
				left_index += 1
				total_index += 1
			while right_index < len(right):  # rest of right elements should be entered
				lst[total_index] = right[right_index]
				right_index += 1
				total_index += 1

	"""permute the info values of the list 
	@rtype: list
	@returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
	COMPLEXITY: O(n)
	"""
	def permutation(self):
		if self.size == 0:
			return AVLTreeList()
		lst = self.listToArray()
		for i in range(len(lst)):  # shuffles lst
			rand_index = random.randint(0, len(lst) - 1)
			temp = lst[rand_index]
			lst[rand_index] = lst[i]
			lst[i] = temp
		root = self.build_tree_from_list(lst)  # builds tree from lst
		tree = AVLTreeList()
		tree.root = root
		tree.size = len(lst)
		return tree

	"""Builds AVL tree from a list recursively
	COMPLEXITY: O(n)"""
	def build_tree_from_list(self, lst, index=0):
		if index >= len(lst):
			virtual = AVLNode(None)
			virtual.size = 0
			return virtual
		node = AVLNode(lst[index])
		node.left = self.build_tree_from_list(lst, 2 * index + 1)
		node.left.parent = node
		node.right = self.build_tree_from_list(lst, 2 * index + 2)
		node.right.parent = node
		node.size = node.left.size + node.right.size + 1
		node.height = max(node.left.height, node.right.height) + 1
		node.bf = node.left.height - node.right.height
		return node

	"""concatenates lst to self
	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	COMPLEXITY: O(logn)
	"""
	def concat(self, lst):
		if self.root is None and lst.root is None:  # Empty trees
			return 0
		if self.root is None:  # One empty tree
			height_diff = -1 - lst.root.height
		elif lst.root is None:  # One empty tree
			height_diff = self.root.height - (-1)
		else:
			height_diff = self.root.height - lst.root.height
		new_size = self.size + lst.size
		if self.size == 0:  # Concatenating to an empty tree
			self.root = lst.root
			self.size = lst.size
			return abs(height_diff)
		if lst.size == 0:  # Nothing to concatenate
			return abs(height_diff)
		if height_diff <= 0:  # Right tree is higher
			middle_element = self.retrieve(self.size - 1)  # Retrieves max of left tree -> left <= middle_el <= right
			self.delete(self.size - 1)  # deletes middle_element from left tree
			if self.size == 0:  # Tree had one element, it can be added and returned
				lst.insert(0, middle_element)
				self.root = lst.root
				self.size = lst.size
				return abs(height_diff)
			curr_node = lst.root
			while curr_node.height > self.root.height:  # Finds element in right tree of height <= self.root.height
				curr_node = curr_node.left
			if curr_node.parent is None:  # Root has no parent, parent pointers can't be updated
				curr_node_parent = None
			else:
				curr_node_parent = curr_node.parent
			# Attaches the middle_element to self.root on the left and curr_node on the right, with curr_node_parent
			# as middle_element's parent
			middle_element_node = AVLNode(middle_element)
			middle_element_node.right = curr_node
			curr_node.parent = middle_element_node
			middle_element_node.left = self.root
			self.root.parent = middle_element_node
			if curr_node_parent:
				curr_node_parent.left = middle_element_node
			middle_element_node.parent = curr_node_parent
			# Updates root of tree
			if curr_node_parent:
				self.root = lst.root
			else:
				self.root = middle_element_node
			self.fix_tree_delete(middle_element_node)  # Does rotations and size/height fixes after join
		else:  # Left tree is higher, symmetrical code
			middle_element = lst.retrieve(0)
			lst.delete(0)
			if lst.size == 0:  # Tree had one element, it can be added and returned
				self.insert(self.size, middle_element)
				return abs(height_diff)
			curr_node = self.root
			while curr_node.height > lst.root.height:  # Finds element in left tree of height <= lst.root.height
				curr_node = curr_node.right
			if curr_node.parent is None:  # Root has no parent, parent pointers can't be updated
				curr_node_parent = None
			else:
				curr_node_parent = curr_node.parent
			# Attaches the middle_element to lst.root on the right and curr_node on the left, with curr_node_parent
			# as middle_element's parent
			middle_element_node = AVLNode(middle_element)
			middle_element_node.left = curr_node
			curr_node.parent = middle_element_node
			middle_element_node.right = lst.root
			lst.root.parent = middle_element_node
			if curr_node_parent:
				curr_node_parent.right = middle_element_node
			middle_element_node.parent = curr_node_parent
			# Updates root of tree
			if curr_node_parent:
				self.root = self.root
			else:
				self.root = middle_element_node
			self.fix_tree_delete(middle_element_node)
		self.size = new_size
		return abs(height_diff)

	"""searches for a *value* in the list
	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	COMPLEXITY: O(n)
	"""
	def search(self, val):
		lst = self.listToArray()
		for i in range(len(lst)):  # Searches in order for val in lst
			if lst[i] == val:
				return i
		return -1

	"""returns the root of the tree representing the list
	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		if self.size == 0:
			return None
		return self.root