"""
Conversion program for the gdl graph 
"""

import re

''' functions '''
''' node function '''
def nodeCreate(nodeTxt, title, gene_dict):
    # Return the string in format (gene id, gene name/title, Geno Ontology)
    return (nodeTxt) % (gene_dict[title][0], title, gene_dict[title][1])

def edgeCreate(edgeTxt, edgeList):
    ''' Return the string in format 
    first gene id, second gene id, evidence
    '''
    return (edgeTxt) % (edgeList[0], edgeList[1], edgeList[2])


# variables
funClasses = {}
subgraph = "none"
evList = ["", 0, 0]
geneID = 0
geneName = ""
gene_dict = {}
gene = [0, ""]
fcList = []
label = ""
geneList = []
# templates for nodes and edges
nodeTxt = "\tnode\n\t[\n\t\tid %s\n\t\tlabel \"%s\"\n\t\tGO \"%s\"\n\t\tgraphics\n\t\t[\n\t\tw	20.0\n\t\th	20.0\n\t\ttype	\"ellipse\"\n\t\twidth	1.00000\n\t\tfill	\"#E1E1E1\"\n\t\toutline	\"#000000\"\n\t\t]\n\t]\n"
edgeTxt = "\tedge [\n\t\tsource %s\n\t\ttarget %s\n\t\tlabel \"%s\"\n\t\tgraphics \n\t\t[\n\t\twidth	2\n\t\ttype	\"line\"\n\t\tfill	\"#0000E1\"\n\t\t]\n\t]\n"
topTxt = "Creator \"Y\"\nVersion 1.0\ngraph\n[\n\tlabel	\"\"\n\tdirected	1\n"
botTxt = "\n]"



# load file
oldFile = open("YeastOutputDefault.gdl", "r")

# Information need to make nodes
# Build up the gene dictionary. This requires giving each gene an unique id
# and record its name and GO (Gene Ontology) feature.
for line in oldFile:
    if re.match(r'node:.*title: "[^VIRTUAL].*label', line):
        title = re.findall(r'title: "([^"]*)"',line)[0]
        if title not in gene_dict.keys():
            geneName = title
            gene[0] = geneID
            gene[1] = re.findall(r'label: "([^"]*)"',line)[0]
            gene_dict[geneName] = gene
            gene = [0, ""]
            geneID += 1
# reset the cursor to the start of the file
oldFile.seek(0)

# Information to make up the edges
# Build up the functional class dictionary
for line in oldFile:
    # Get a new Functional Class/subgraph
    if re.match(r'graph:.*"SUBGRAPH ', line):

        ''' if not the first functional class then load edge info
        into funClasses and then clear variables '''
        if subgraph is not "none":
            funClasses[subgraph] = [label, fcList, geneList]
            fcList = []
            geneList = []
        # Get title and metadata about the subgraph
        subgraph = re.findall(r'graph:.*"SUBGRAPH (\S*)"', line)[0]
        label = re.findall(r'.*label: "(.*)"', line)[0]
    # Make a list of all the genes in the functinal class
    elif re.match(r'node:.*title: "[^VIRTUAL].*label', line):
        geneTitle = re.findall(r'title: "([^"]*)"',line)[0]
        if geneTitle is not geneList:
            geneList.append(geneTitle)
        # print (geneList)
    # For each gene in Functional Class get id and use this to build edges
    elif re.match(r'edge:.*', line):
        if re.match(r'edge:.*source:"[^VIRTUAL]', line):
            id1 = gene_dict[geneTitle][0]
            id2 = gene_dict[re.findall(r'.*source:"(\S*)"', line)[0]][0]
            # Sort id's by size
            if id1 > id2:
                n = id1
                id1 = id2
                id2 = n
            evidence = re.findall(r'.*target: "(.*)"', line)[0]
            edge = [id1, id2, evidence]
            # Check if edge is already in list
            if edge not in fcList:
                fcList.append(edge)
# Add last FC to dictionary
funClasses[subgraph] = [label, fcList, geneList]
fcList = []
geneList = []

for key in funClasses:
    print (key, "Functional Class", funClasses[key][0])
    print (funClasses[key][1])
    print (funClasses[key][2])
    print ()

oldFile.close()

# Print the graph model language text
# Use only YDR001C
gmlText = ""
key = "YDR001C"


# Make a new file
newFile = open("output_2.gml", 'w')




# Print header
print (topTxt)
newFile.write(topTxt)

#for key in funClasses:
# Print nodes
for geneTitle in funClasses[key][2]:
    print (nodeCreate(nodeTxt, geneTitle, gene_dict))
    newFile.write(nodeCreate(nodeTxt, geneTitle, gene_dict))
# Print Edges
for edge in funClasses[key][1]:
    print(edgeCreate(edgeTxt, edge))
    newFile.write(edgeCreate(edgeTxt, edge))



# Print footer
print(botTxt)
newFile.write(botTxt)

''' Close the files'''
newFile.close()