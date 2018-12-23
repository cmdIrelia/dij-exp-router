import matplotlib.pyplot as plt
import matplotlib.colors as clrs
import numpy as np
import networkx as nx
import colorsys 

def rgb2str(r,g,b):
    #r, g, b = rgbcolor
    #return str(hex(r))[2:] + str(hex(g))[2:] + str(hex(b)[2:])
    return "#{:0>2x}{:0>2x}{:0>2x}".format(r,g,b)

def hsv2rgb(h,s,v):
    return colorsys.hsv_to_rgb(h,s,v)

def hsv2str(h,s,v):
    r,g,b = hsv2rgb(h,s,v)
    return rgb2str(int(r*255),int(g*255),int(b*255))

s=input().split()
graph_path = list()
graph_path.append(s)
for i in range(len(s)-1):
    graph_path.append(input().split())
print('path input done.')
#print(graph_path)

s=input().split()
graph_weight = list()
graph_weight.append(s)
for i in range(len(s)-1):
    graph_weight.append(input().split())
print('weight input done.')

# graph_path=[
#     ['0', '1', '0', '0', '0', '0', '0', '1', '1'], 
#     ['1', '0', '1', '0', '0', '0', '0', '1', '0'], 
#     ['0', '1', '0', '1', '0', '1', '0', '0', '1'], 
#     ['0', '0','1', '0', '1', '1', '0', '0', '0'], 
#     ['0', '0', '0', '1', '0', '1', '0', '0', '1'], 
#     ['0', '0', '1', '1', '1', '0', '1', '0', '0'], 
#     ['0', '0', '0', '0', '0', '1', '0', '1', '1'], 
#     ['1', '1', '0', '0', '0', '0', '1', '0', '1'], 
#     ['1', '0', '1', '0', '1', '0', '1', '1', '0']
# ]

# graph_weight=[
#     ['0', '3.6', '0', '0', '0', '0', '0', '3.7', '3.9'], 
#     ['3.6', '0', '3.6', '0', '0', '0', '0', '0', '0'],
#     ['0', '3.6', '0', '3.3', '0', '2', '0', '0', '1.7'], 
#     ['0', '0', '3.3', '0', '3.3', '0', '0', '0', '0'], 
#     ['0', '0','0', '3.3', '0', '4', '0', '0', '3.9'],
#     ['0', '0', '2', '0', '4', '0', '2', '0', '0'],
#     ['0', '0', '0', '0', '0', '2', '0', '2', '0'], 
#     ['3.7', '0', '0', '0', '0', '0', '2', '0', '1.7'], 
#     ['3.9', '0', '1.7', '0', '3.9', '0', '0', '1.7', '0']
# ]

V=len(graph_path)

plt.figure(figsize=(5,4))

G = nx.Graph()

#G.add_edge(1, 2, weight=4.7 )
#G.add_edges_from([(3, 4,{'color': rgb2str(255,0,0)}), (4, 5,{'color': rgb2str(255,0,0)})])
#G[3][4]['color']=rgb2str(0,255,0)

for i in range(V):
    for j in range(i+1,V):
        if(graph_path[i][j]!='0'):
            G.add_edge(i,j)
            G[i][j]['color']=hsv2str(0.5-float(graph_weight[i][j])/8,1,1)
            G[i][j]['weight']=graph_weight[i][j]

#position={}
#for i in range(V):
#    position[i]=(i,i)
position={
    0:(0,0),
    1:(1,1),
    2:(2,1),
    3:(3,1),
    4:(4,0),
    5:(3,0.5),
    6:(2,0.5),
    7:(0.8,0.2),
    8:(2,-0.5),
    9:(1.5,0),
    10:(2.5,0)}

edges,colors = zip(*nx.get_edge_attributes(G,'color').items())
nx.draw(G,pos=position,edgelist=edges,edge_color=colors,
    with_labels=True,width=3,node_size=700,node_color='#bfbfbf') 
#pos = nx.circular_layout(G),

#plt.axis('off')
#plt.savefig("weighted_graph.png") # save as png
plt.show()