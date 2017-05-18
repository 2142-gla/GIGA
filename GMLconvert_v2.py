''' Convert old gdl text file to gml 
	Work through each functional class
'''
# imort time to check how long sections take
from time import time


''' functions '''



# 'main' code
''' Load the file and create the new file'''
try:
	oldFile = open("YeastOutputDefault.txt", "r")
	newFile = open("output.gml", "w")
except:
	print ("File not found")

''' Variables '''
gene_id = 0
func_id = ""
gene_dict = {}
func_dict = {}
gene_meta = ["", ""]

genes_ls = ['gene list']


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

for key in func_dict:
	print (key)
	for gene in func_dict[key][2]:
		print ('\t', func_dict[key][2][gene][0], gene)



''' Close the files'''
oldFile.close()
newFile.close()
