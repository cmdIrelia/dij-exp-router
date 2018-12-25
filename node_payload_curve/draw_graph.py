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

V=len(graph_path)

plt.figure(figsize=(3,3))
plt.ion()

G = nx.Graph()

#颜色明显程度
color_scale = 2.9

weight_list = list()

for i in range(V):
    for j in range(i+1,V):
        if(graph_path[i][j]!='0'):
            G.add_edge(i,j)
            G[i][j]['color']=hsv2str(1/color_scale-float(graph_weight[i][j])/(Tmax*color_scale),1,1)
            G[i][j]['weight']=graph_weight[i][j]

            weight_list.append(graph_weight[i][j])

position={}
if int(np.sqrt(V))!=np.sqrt(V):
    raise Exception

Side_Len = np.sqrt(V)
for i in range(V):
    position[i]=(int(i/Side_Len),int(i%Side_Len))


edges,colors = zip(*nx.get_edge_attributes(G,'color').items())
nx.draw(G,pos=position,edgelist=edges,edge_color=colors,font_size=8,
    with_labels=True,width=3,node_size=100,node_color='#bfbfbf') 
#pos = nx.circular_layout(G),

#plt.axis('off')
#plt.savefig("weighted_graph.png") # save as png

plt.figure()

for index,d in enumerate(weight_list):
    weight_list[index]=float(d)

weight_list.sort()
plt.plot(weight_list)
plt.ylabel('payload')
plt.xlabel('node')
plt.show()