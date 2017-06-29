#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Create an html description of the subgraphs
'''
#
import networkx as nx
import matplotlib.pyplot as plt

# Main function receives the two data dictionaries
def main (funClasses, geneDiction):
    # Start
    print ('Main')

    # Make a graph object from the data dictionaries
    fc01 = nx.MultiGraph()

    # Use for the first functional class for this one
    key = 'YER065C'
    geneList = funClasses[key][2]


    # Create nodes
    for geneDetails in geneList:
        nodeGene = geneDiction[geneDetails[0]][0]
        print (nodeGene)
        fc01.add_node(nodeGene)
        # add labels to nodes
        fc01.node[nodeGene]['label'] = geneDetails[0]

    fc01.nodes(data=True)

    print(fc01.nodes())
    # Create edges
    edgesList = funClasses[key][1]

    for edge in edgesList:
        n1 = edge[0]
        n2 = edge[1]
        fc01.add_edge(n1, n2)

    print (fc01.edges())

    nx.draw(fc01)

    # http://networkx.readthedocs.io/en/networkx-1.11/reference/generated/networkx.drawing.nx_pylab.draw_networkx_labels.html#networkx.drawing.nx_pylab.draw_networkx_labels


    plt.show()


    #