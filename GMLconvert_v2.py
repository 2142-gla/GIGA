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
gene_dict = {}
funct_dict = {}
gene_list = ["", ""]
genes_ls = ['gene list']


''' Work through the file '''
start = time()
for line in oldFile:
	# print (line);

	# set up fucntional class dictionary



	# Make list of all the genes 
	# Start time 

	if line.startswith("total"): # end of data line
		break
	elif line[0] == "-":
		#print ("gene line")
		# get id, name and GO
		components = line.split("\t")

		gene_list[0] = components[1].rstrip()
		gene_list[1] = components[2].rstrip()

		if gene_list[0] not in genes_ls:
			genes_ls.append(gene_list[0])
			graph_dict[gene_id] = gene_list
			gene_id = gene_id + 1
			gene_list = ["", ""]
		else:

	else:
		components = line.split("\t")
		func_list = [components[1].rstrip(), components[2].rstrip()]
		funct_dict[components[0].rstrip()] = func_list

end = time()

total_time = end - start
print ("Total time to load and check gene list and create fucntional class list is: " + str(total_time))

for key in funct_dict:
	print (key)




''' Close the files'''
oldFile.close()
newFile.close()








