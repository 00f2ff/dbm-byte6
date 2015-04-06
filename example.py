import numpy as np
import matplotlib.pyplot as plt

a = [[1, 4039], [2, 3964], [3, 3856], [4, 3754], [5, 3634], [6, 3500], [7, 3382], [8, 3230], [9, 3113], [10, 2987], [11, 2904], [12, 2799], [13, 2667], [14, 2519], [15, 2378], [16, 2231], [17, 2061], [18, 1999], [19, 1931], [20, 1854]]
def splitter(a):
	nodes = []
	ks = []
	for i in xrange(len(a)):
		nodes.append(a[i][1])
		ks.append(a[i][0])
	return ks, nodes

ks, nodes = splitter(a)
print ks
print nodes


plt.xlabel('k')
plt.ylabel('Nodes')
plt.title('Facebook Nodes for Varying Values of k')
plt.plot(ks, nodes, 'bo')
plt.show()