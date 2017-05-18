''' Convert old gdl text file to gml 
	Work through each functional class
'''
# imort time to check how long sections take
from time import time

''' functions '''
''' node function '''
def nodeCreate(nodeTxt, key, gene_list):
    return (nodeTxt) % (key, gene_list[0], gene_list[1])

''' get all the pairings '''
def edgePairs(edgeTxt, pair0, pair1):
        newFile.write(((edgeTxt) % (pair0, pair1)))

''' edge function'''
def edgeCreate(edgeTxt, graph_dict):
	sizeDict = len(graph_dict)

	for i in range(sizeDict):
		for j in range(i+1, sizeDict,1):
			edgePairs (edgeTxt, str(i), str(j))

# open file
def openFile():
	try:
		oF = open("YeastOutputDefault.txt", "r")
		return oF
	except Exception as e:
		print ("file not found")
		exit()

# new file
def newFile():
	try:
		nf = open("op_full01.gml", "w")
		return nf
	except Exception as e:
		print ("file not found")
		exit()


# 'main' code
''' Load the file and create the new file'''
oldFile = openFile()
newFile = newFile()

''' Variables '''

gene_id = 0
func_id = ""
gene_dict = {}
func_dict = {}
gene_meta = ["", ""]
genes_ls = ['gene list']
# templates for nodes and edges
nodeTxt = "\tnode\n\t[\n\t\tid %s\n\t\tlabel \"%s\"\n\t\tGO \"%s\"\n\t\tgraphics\n\t\t[\n\t\tw	20.0\n\t\th	20.0\n\t\ttype	\"ellipse\"\n\t\twidth	1.00000\n\t\tfill	\"#E1E1E1\"\n\t\toutline	\"#000000\"\n\t\t]\n\t]\n"
edgeTxt = "\tedge [\n\t\tsource %s\n\t\ttarget %s\n\t\tlabel \"pp\"\n\t\tgraphics \n\t\t[\n\t\twidth	2\n\t\ttype	\"line\"\n\t\tfill	\"#0000E1\"\n\t\t]\n\t]\n"
topTxt = "Creator \"Y\"\nVersion 1.0\ngraph\n[\n\tlabel	\"\"\n\tdirected	1\n"
botTxt = "\n]"

''' Work through the file '''
# Start time 
start = time()

for line in oldFile:
	# print (line);
	# set up fucntional class dictionary

	# Make list of all the genes 

	if line.startswith("total"): # end of data line
		break
	elif line[0] == "-":
		#print ("gene line")
		# get id, name and GO
		components = line.split("\t")

		gene_meta[0] = components[1].rstrip()
		gene_meta[1] = components[2].rstrip()

		if gene_meta[0] not in genes_ls:
			genes_ls.append(gene_meta[0])
			gene_dict[gene_id] = gene_meta
			gene_id = gene_id + 1
			gene_meta = ["", ""]
		else:
			index = genes_ls.gene_meta[0]
			gene_dict[gene_id] = gene_meta
			gene_meta = ["", ""]

		func_dict[func_id][2] = gene_dict

	else:
		components = line.split("\t")
		gene_dict = {}
		func_list = [components[1].rstrip(), components[2].rstrip(), gene_dict]
		func_dict[components[0].rstrip()] = func_list
		func_id = components[0].rstrip()


end = time()

total_time = end - start
print ("Total time to load and check gene list and create fucntional class list is: " + str(total_time))

# for key in func_dict:
# 	print (key)
# 	for gene in func_dict[key][2]:
# 		print ('\t', func_dict[key][2][gene][0], gene)

# print the information to file

# header of file
newFile.write(topTxt)

# nodes
# for group in func_dict:
for element in func_dict:
	gene_diction = func_dict[element][2]
	for gene_id in gene_diction:
		newFile.write(nodeCreate(nodeTxt, gene_id, gene_diction[gene_id]))
	
# edges
#edgeCreate(edgeTxt, graph_dict)

newFile.write(botTxt)

# Close the files
oldFile.close()
newFile.close()
