# AVL-Tree

Hey everyone, this repository include an implementation of The List ADT using an AVL tree, complete with a complexity analysis and two experiments to validate the analysis resultes.


An AVL tree is a self-balancing binary search tree that maintains balance by ensuring that the height difference of the left and right subtrees of any node is not more than 1. This helps to ensure the tree remains balanced and search operations have an average time complexity of O(log n).

## AVLNode class:
This implementation features an AVLNode class, where each object of type AVLNode holds the following instance fields:

* value: the value stored in the node
* left: a pointer to the node's left child
* right: a pointer to the node's right child
* parent: a pointer to the node's parent
* height: the height of the node in the tree, represented by the longest path from the node to a leaf in the tree
* size: the number of nodes in the node's subtree, representing the size of the subtree
* bf: the balance factor of the node, representing the difference between the height of the left and right subtrees.

## AVL functions:
The AVLTreeList class has the following instance fields:

* root: a pointer to the root node of the tree.
* size: the number of nodes in the tree.

It also has the following functions:

* init: Initializes the tree by setting root to None and size to 0.
* rank(node): returns the rank of the input node in the tree.
* select(node, requested_rank): returns the node at the specified rank in the tree, where the input node is the root.
* predecessor(node): returns the node preceding the input node, as determined by the algorithm taught in the lecture.
* successor(node): returns the node following the input node, as determined by the algorithm taught in the lecture.
* create_virtual_children(node): a helper function that creates virtual left and right children for a given node.
* empty(): returns true if the tree is empty and false otherwise.
* retrieve(i): returns the value of the node at index i in the tree.
* insert(i,val): inserts a node with value "val" at index "i" in the tree.
* fix_tree_insert(node): receives a newly inserted node and returns the number of rotations performed to maintain the tree as a proper AVL tree.
* rotate(node): receives a node and performs rotations as necessary to maintain the tree as a proper AVL tree. The function returns the number of rotations made. The rotations are done using the left_rotate and right_rotate functions.
* left_rotate(node): rotates the tree to the left around the input node and updates the pointers in the tree. The root of the tree is updated if necessary.
* right_rotate(node): rotates the tree to the right around the input node and updates the pointers in the tree. The root of the tree is updated if necessary.
* delete(i): deletes the node at index i in the tree.
* delete_root(): deletes the root node of the tree.
* fix_tree_delete(node): receives a node after a delete operation and returns the number of rotations performed to maintain the tree as a proper AVL tree.
* first(): returns the value of the first node in the tree (the node with the lowest key value).
* last(): returns the value of the last node in the tree (the node with the highest key value).
* listToArray(): returns an array representation of the tree.
* listToArrayRec(lst, currNode): is a recursive function that returns an array representation of the tree by passing through the nodes in in-order.
* sort(): returns a tree with nodes in sorted order according to their values.
* merge_sort(lst): performs a merge sort on the input list, as taught in the lecture.
* permutation(): returns a tree with nodes in random order.
* build_tree_from_list(list): builds a tree from the input list.
* concat(lst): concatenates the input tree "lst" to the end of the original tree and returns the height difference between the two trees.
* search(val): searches for the input value in the tree.
* getRoot(): returns the root of the tree.

## Performance and Complexity Analysis:

### Experiment 1

This experiment examine the average number of balancing steps required in a series of insertions, deletions, and a mixture of insertions and deletions, for different sizes of trees.
The number of nodes that will be inserted into the tree will be: n = 1500 * 2^i. For example, when i = 1, the tree size will be 3000, and when i = 10, the tree size will be about 1.5 million. This will be done for i = 1, ..., 10.

For each tree size, we will conduct three separate experiments:

a. Insert elements in random order.
b. Insert elements in random order (time measurement not included), followed by deletion of the elements in random order.
c. Insert n/2 elements in random order, then perform n/2 insertions and deletions in random order.

Results Summary:

***table:*** showing the number of ***rotations*** in the tree as a function of the value of n for each of the experiments

|i	|n = 1500*2^i	|a- insertions	|b- deletion	|c- insertion and deletion|
|:---: |:---: |:---: |:---: |:---: |
|1	|3000	|2066	|1152	|1904|
|2	|6000	|4205	|2201	|3701|
|3	|12000	|8299	|4509	|7380|
|4	|24000	|16554	|8891	|14748|
|5	|48000	|33434	|17992	|29591|
|6	|96000	|67175	|35593	|59150|
|7	|192000	|134064	|71793	|117888|
|8	|384000	|268185	|143536	|235745|
|9	|768000	|536842	|286764	|471019|
|10	|1536000	|1072027	|575258	|942639|
|Complexity	||O(n)	|O(n)	|O(n)|

***Graph:*** showing the correlation between the number of rotations in the tree and the value of n, along with the trendline equation.

<img src="https://user-images.githubusercontent.com/112472485/217863001-baa50887-d7f0-439d-bb7b-e476a6e91770.png" width="700">


The results presented in the graph demonstrate that the trend lines and R^2 values suggest that each insertion/deletion series takes O(n) rotations.

### Experiment 2
This experiment is about comparing the insertions performance of an AVL tree with that of a linked list and an array.
The insertions will be performed at the beginning, randomly, and at the end of the list. <br />
The number of values to be inserted into the list will be n = 1500 * i, for i = 1, 2, ..., 10.

#### a. Beginning insertions:

|i	|n = 1500*i	|AVL tree beginning insertions [Sec]	|Linked list beginning insertions [Sec]	|Array beginning insertions [Sec]|
|:---: |:---: |:---: |:---: |:---: |
|1	|1500	|9.69E-06	|6.75E-08	|2.33E-07|
|2	|3000	|9.26E-06	|5.44E-08	|4.27E-07|
|3	|4500	|9.13E-06	|5.76E-08	|5.82E-07|
|4	|6000	|9.43E-06	|5.46E-08	|8.10E-07|
|5	|7500	|1.08E-05	|5.57E-08	|9.67E-07|
|6	|9000	|9.99E-06	|5.48E-08	|1.16E-06|
|7	|10500	|9.93E-06	|5.51E-08	|1.35E-06|
|8	|12000	|1.18E-05	|5.50E-08	|1.70E-06|
|9	|13500	|1.13E-05	|5.55E-08	|2.12E-06|
|10	|15000	|1.09E-05	|5.52E-08	|2.15E-06|

***Graph:***

<img src=https://user-images.githubusercontent.com/112472485/217874718-d0cd25fa-b5d9-4be8-8694-b09aff664b25.png width="700">


Results analysis:
##### AVL Tree:
The operation of inserting values at the beginning requires a trip from the root of the tree to the minimum of the tree each time.
This results in paths with lengths of log1 + log2 + ... + logn = O(nlogn). The balancing operations for every insertion have a complexity of O(1), making the total work of the insertion operation at the beginning O(nlogn).
For n elements, the amortized time to insert a member into the tree is O(logn).
The time measurement results show that the time increases at a rate that is less than linear, indicating an adjustment to the expectation.
Additionally, the AVL data structure that we implemented has significantly less efficient running times compared to built-in implementations in Python and C language.
Despite having higher asymptotic running complexity, their running times were lower than our AVL tree implementation.
##### Linked List:
The operation of inserting an element at the beginning of a linked list requires a fixed number of operations, resulting in a time complexity of O(n) for inserting n elements.
The amortized (and Worst case) time to insert an element at the beginning of the list is O(1). The results of the experiment showed an approximately constant running time for inserting an element at the beginning, with an average running time that does not change significantly with an increase in n.
This data structure has the lowest running times among the three structures for inserting at the beginning, as expected due to the constant number of operations required.
#### Array:
The initialization of an empty array takes O(1).<br />
Inserting n elements into the array at the beginning results in a time complexity of 1 + 2 + ... + n = O(n^2), leading to an amortized time  of O(n) for insert an element at the beginning of the array.
The results of the experiment showed a linear growth rate of the average insertion time with an increase in n, matching the expectation. Despite the linear growth rate, the running times for the array were much lower than those of the AVL tree that implemented.

#### b. Random insertions:

|i	|n	|AVL tree random insertions [Sec]	|Linked list random insertions [Sec]	|Array random insertions [Sec]|
|:---: |:---: |:---: |:---: |:---: |
|1	|1500	|9.67E-06	|7.27E-07	|7.28E-07|
|2	|3000	|1.04E-05	|9.89E-07	|7.98E-07|
|3	|4500	|1.05E-05	|1.22E-06	|7.41E-07|
|4	|6000	|1.07E-05	|1.27E-06	|8.57E-07|
|5	|7500	|1.09E-05	|1.43E-06	|9.53E-07|
|6	|9000	|1.27E-05	|1.59E-06	|1.04E-06|
|7	|10500	|1.14E-05	|1.74E-06	|1.15E-06|
|8	|12000	|1.41E-05	|1.89E-06	|1.24E-06|
|9	|13500	|1.16E-05	|2.12E-06	|1.38E-06|
|10	|15000	|1.30E-05	|2.43E-06	|1.44E-06|

***Graph:***

<img src=https://user-images.githubusercontent.com/112472485/217863298-f1979bc7-202f-4699-9ba9-0fcdfc23fdf4.png width="700">

Results analysis:
##### AVL Tree:
When inserting elements to a random possition in an AVL tree, each insertion requires traversing from the root to a leaf, resulting in a total complexity of O(nlogn).
for every insertion the balancing operation is done with a complexity of O(1), thus the overall time for a random insertion is O(nlogn).
For n elements, the average time for inserting one element into the tree is O(logn).
The time measurement shows that the increase in time is less than linear.
##### Linked List:
For a linked list, inserting elements to a random possition requires going through i elements, where i is the index of the desired insertion point.
On average, half of the elements in the list are traversed during each insertion process.
For n elements, the average time for inserting one element into a random position in the list is O(n), and the growth rate of time is approximately linear with respect to n.
##### Array:
Inserting elements to a random possition in an array also requires moving n-i elements, where i is the index of the desired insertion point.
On average, half of the elements in the array are moved during each insertion process.
For n elements, the average time for inserting one element into a random position in the array is O(n), and the growth rate of time is approximately linear with respect to n.
Although the average time complexity for inserting an element into a random position is the same for an array and a linked list, the running times for arrays are lower for the tested n values.
This may be due to the efficient implementation of arrays in python. The running times for arrays are the lowest for the operation of inserting an element into a random possition.


#### c. insertions to the end of the list:

|i	|n	|AVL tree end insertions [Sec]	|Linked list end insertions [Sec]	|Array end insertions [Sec]|
|:---: |:---: |:---: |:---: |:---: |
|1	|1500	|1.06E-05	|4.96E-08	|5.39E-08|
|2	|3000	|1.04E-05	|4.87E-08	|4.12E-08|
|3	|4500	|1.06E-05	|4.72E-08	|3.78E-08|
|4	|6000	|1.08E-05	|4.87E-08	|3.58E-08|
|5	|7500	|1.09E-05	|4.68E-08	|3.48E-08|
|6	|9000	|1.10E-05	|4.82E-08	|3.50E-08|
|7	|10500	|1.43E-05	|4.72E-08	|3.44E-08|
|8	|12000	|1.22E-05	|5.02E-08	|3.44E-08|
|9	|13500	|1.38E-05	|5.18E-08	|3.49E-08|
|10	|15000	|1.03E-05	|4.92E-08	|3.41E-08|

***Graph:***

<img src=https://user-images.githubusercontent.com/112472485/217863368-8d14439e-6cf0-4f32-8826-c122c6f472db.png width="700">

Results analysis:
##### AVL Tree:
The insertion operation requires traveling along the tree from the root to the bottom of the tree each time, with the lengths of the trip being log1 + log2 + ... + logn = O(nlogn).
The balancing operations have a complexity of O(1), making the total work for the insertion operations O(nlogn).
For n elements, the amortized time for inserting an element into the tree is O(logn).
The measurement results show that the time increases at a rate less than linear, so there is an adjustment to the expectation.
##### Linked List:
The insertion operation at the end of a linked list requires a constant number of operations, resulting in a time complexity of O(n).
The results indicate a nearly constant running time, with an average time that remains almost unchanged as a function of n.
##### Array:
Adding to the end of an array has an amortized complexity of O(1). The results also show a nearly constant running time, with an average time that remains almost unchanged as a function of n.
Although the average time complexities for inserting an element at the end are the same for arrays and linked lists, the running times for arrays are lower for the tested n values.
This is likely due to the efficient implementation of the array data structure in python. The running times for arrays are the lowest for inserting an element at the end.

Thanks for reading
