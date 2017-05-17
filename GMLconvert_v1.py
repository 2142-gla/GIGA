''' Convert old gdl text file to gml '''
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

# 'main' code block
''' Load the file '''
try:
	oldFile = open("YeastOutputDefault.txt", "r")
	newFile = open("output.gml", "w")
except:
	print ("File not found")


''' Variables '''
gene_id = 0
graph_dict = {}
gene_list = ["", ""]
nodeTxt = "\tnode\n\t[\n\t\tid %s\n\t\tlabel \"%s\"\n\t\tGO \"%s\"\n\t\tgraphics\n\t\t[\n\t\tw	20.0\n\t\th	20.0\n\t\ttype	\"ellipse\"\n\t\twidth	1.00000\n\t\tfill	\"#E1E1E1\"\n\t\toutline	\"#000000\"\n\t\t]\n\t]\n"
edgeTxt = "\tedge [\n\t\tsource %s\n\t\ttarget %s\n\t\tlabel \"pp\"\n\t\tgraphics \n\t\t[\n\t\twidth	2\n\t\ttype	\"line\"\n\t\tfill	\"#0000E1\"\n\t\t]\n\t]\n"
#edgeTxt = "%s %s"

''' Work through the file '''
for line in oldFile:
	# print (line);
	if line.startswith("YGR088W"):
		break
	if line[0] == "-":
		#print ("gene line")
		# get id, name and GO
		components = line.split("\t")

		gene_list[0] = components[1].rstrip()
		gene_list[1] = components[2].rstrip()

		graph_dict[gene_id] = gene_list
		gene_id = gene_id + 1
		gene_list = ["", ""]

		# for word in components:
		# 	if word == "\n":
		# 		continue
		# 	word = word.rstrip()
		# 	print (word)

# print graph_dict

topTxt = "Creator \"Y\"\nVersion 1.0\ngraph\n[\n\tlabel	\"\"\n\tdirected	1\n"
botTxt = "\n]"

newFile.write(topTxt)

for key in graph_dict:
	newFile.write(nodeCreate(nodeTxt, key, graph_dict[key]))
	
edgeCreate(edgeTxt, graph_dict)

newFile.write(botTxt)
                        
''' Close the files'''
oldFile.close()
newFile.close()



        
