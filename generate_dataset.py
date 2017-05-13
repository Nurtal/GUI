"""
generate the javascript dataset
for apriori animation

TODO : add limit generation

"""


nodeToColor = {"node0": "yellow",
			   "node1": "blue",
			   "node2": "brown",
			   "node3": "red",
			   "node4": "pink",
			   "node5": "grey",
			   "node6": "green",
			   "node7": "purple",
			   "node8": "cyan",
			   "node9": "orange"}

list_of_node = ["node0", "node1", "node2", "node3", "node4", "node5", "node6", "node7", "node8", "node9"]

list_of_node_js = []
list_of_edge_js = []


import itertools


# control data generation
number_of_branch = 0
branch_max_lenght = len(list_of_node)
branch_max_number = 100
branchSizeToNumber_authorized = {}
branchSizeToNumber = {}

for L in range(0, len(list_of_node)+1):
  for subset in itertools.combinations(list_of_node, L):
  	number_of_branch += 1

for x in xrange(0, branch_max_lenght+1):
	branchSizeToNumber_authorized[x] = int(branch_max_number/branch_max_lenght)
	branchSizeToNumber[x] = 0

# Generate all combinaison
node_id = 0
for L in range(0, len(list_of_node)+1):
  for subset in itertools.combinations(list_of_node, L):
  	
  	branch = []
  	for elt in subset:
  		branch.append(node_id)

  	branch_size = len(branch)
  	if(branchSizeToNumber[branch_size] <= branchSizeToNumber_authorized[branch_size]):

  		branchSizeToNumber[branch_size] += 1


	  	for elt in subset:
	  		list_of_node_js.append(elt)
	  		branch.append(node_id)
	  		node_id += 1
	  	
	  	if(len(branch)> 1):
	  		index = 0
	  		for x in xrange(0, len(branch)-1):
	  			edge_to_add = [branch[index], branch[index+1]]
	  			list_of_edge_js.append(edge_to_add)
	  			index +=1
  	

dataset_file = open("apriori_dataset.txt", "w")

dataset_file.write("nodes: [\n")
for node in list_of_node_js:
	dataset_file.write("{ name: \""+str(node)+ "\", color: \""+str(nodeToColor[node])+"\" },\n")
dataset_file.write("],\n")

dataset_file.write("edges: [\n") 
for edge in list_of_edge_js:
	dataset_file.write("{source: "+str(edge[0])+", target: "+str(edge[1]) +"},\n")
dataset_file.write("]\n")

dataset_file.close()