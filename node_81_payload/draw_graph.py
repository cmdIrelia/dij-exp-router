import matplotlib.pyplot as plt
import matplotlib.colors as clrs
import numpy as np
import networkx as nx
import colorsys 

Tmax = 6

def rgb2str(r,g,b):
    #r, g, b = rgbcolor
    #return str(hex(r))[2:] + str(hex(g))[2:] + str(hex(b)[2:])
    return "#{:0>2x}{:0>2x}{:0>2x}".format(r,g,b)

def hsv2rgb(h,s,v):
    return colorsys.hsv_to_rgb(h,s,v)

def hsv2str(h,s,v):
    r,g,b = hsv2rgb(h,s,v)
    return rgb2str(int(r*255),int(g*255),int(b*255))

graph_path = list()
with open(r'C:\\Users\\90612\\Desktop\\graph_path.txt','r') as f:
        while(1):
            s=f.readline()
            if(not s):
                break
            s=s.split()
            graph_path.append(s)
print('path input done.')
#print(graph_path)

graph_weight = list()
with open(r'C:\\Users\\90612\\Desktop\\graph_weight.txt','r') as f:
        while(1):
            s=f.readline()
            if(not s):
                break
            s=s.split()
            graph_weight.append(s)
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

#plt.figure(figsize=(5,4))

G = nx.Graph()

#G.add_edge(1, 2, weight=4.7 )
#G.add_edges_from([(3, 4,{'color': rgb2str(255,0,0)}), (4, 5,{'color': rgb2str(255,0,0)})])
#G[3][4]['color']=rgb2str(0,255,0)

#颜色明显程度
color_scale = 4.0

for i in range(V):
    for j in range(i+1,V):
        if(graph_path[i][j]!='0'):
            G.add_edge(i,j)
            G[i][j]['color']=hsv2str(1/color_scale-float(graph_weight[i][j])/(Tmax*color_scale),1,1)
            G[i][j]['weight']=graph_weight[i][j]

position={}
if int(np.sqrt(V))!=np.sqrt(V):
    raise Exception

Side_Len = np.sqrt(V)
for i in range(V):
    position[i]=(int(i/Side_Len),int(i%Side_Len))

# index=0
# class rectangle:
#     left=0
#     right=0
#     top=0
#     def __init__(self, V):
#         self.left=0
#         self.right=int((V-4)/4)
#         self.top=self.right+9
#         self.last=self.top+8

# rect=rectangle(V)
# for _index in range(rect.left,rect.right+1):
#     position[index]=(_index-rect.left,0)
#     index+=1
# for _index in range(rect.right+1,rect.top+1):
#     position[index]=(rect.right,_index-rect.right)
#     index+=1
# for _index in range(rect.top+1,rect.last+1):
#     position[index]=(rect.top+V/4-1-_index,rect.right)
#     index+=1
# for _index in range(rect.last+1,V):
#     position[index]=(0,_index-rect.last)
#     index+=1

# position={
#     0:(0,0),
#     1:(1,1),
#     2:(2,1),
#     3:(3,1),
#     4:(4,0),
#     5:(3,0.5),
#     6:(2,0.5),
#     7:(0.8,0.2),
#     8:(2,-0.5),
#     9:(1.5,0),
#     10:(2.5,0)}

edges,colors = zip(*nx.get_edge_attributes(G,'color').items())
nx.draw(G,pos=position,edgelist=edges,edge_color=colors,
    with_labels=True,width=3,node_size=300,node_color='#bfbfbf') 
#pos = nx.circular_layout(G),

#plt.axis('off')
#plt.savefig("weighted_graph.png") # save as png
plt.show()
