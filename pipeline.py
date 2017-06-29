#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 20:12:57 2017

@author: Chatten
"""

import subprocess
import gigaConvert
import json_create
import key

# # Run perl GIGA program to get gdl file
# giga = ['perl','giga.pl','-IDelRisi_expr.txt','-NYeastNetwork.txt','-GYeastGeneAnnot.txt','-Ftxt','-OoutTxt.txt']
# subprocess.call(giga)
# # Run perl GIGA program again to get the default text file
# gigaTxt = ['perl','giga.pl','-IDelRisi_expr.txt','-NYeastNetwork.txt','-GYeastGeneAnnot.txt','-Fgdl','-Oout.gdl']
# subprocess.call(gigaTxt)


# defaulttext = subprocess.run(giga, stdout=subprocess.PIPE).stdout.decode('utf-8')
# this extracts the standard output of the program run. However as it is not the default text it is of limited use.


# extract giga.pl information into dictionaries
# This would probably be better as a oop class
gigaConvert.mainGiga()
funClasses = gigaConvert.retFC()
geneDiction = gigaConvert.retGD()

# Build the key file in text
key.buildTxt(funClasses, geneDiction)


# Create the JSON file

json_create.main(funClasses, geneDiction)

# Convert output to gml
# subprocess.call(['/Library/Frameworks/Python.framework/Versions/3.6/bin/python3', 'gigaConvert.py'])

# # Open cytoscope with file
# # java -Xmx512M -jar cytoscape.jar [OPTIONS]
# # -N,--network <file>     Load a network file (any format)
# cyto = ['/Applications/Cytoscape_v3.5.1/cytoscape.sh', '-N', 'cyto_01.gml']
# subprocess.call(cyto)
