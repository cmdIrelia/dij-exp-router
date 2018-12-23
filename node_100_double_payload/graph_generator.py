import numpy as np

V=100

Squad_V=int(np.sqrt(V))

array=np.zeros([V,V])

for i in range(Squad_V):
    for j in range(1,Squad_V):
        #print('['+str(i*Squad_V+j)+','+str(i*Squad_V+j-1)+']',end='\t')
        array[int(i*Squad_V+j)][int(i*Squad_V+j-1)]=1
        array[int(i*Squad_V+j-1)][int(i*Squad_V+j)]=1
    #print('')

print('==============')

for i in range(Squad_V):
    for j in range(1,Squad_V):
        #print('['+str(i+Squad_V*j)+','+str(i+Squad_V*(j-1))+']',end='\t')
        array[int(i+Squad_V*j)][int(i+Squad_V*(j-1))]=1
        array[int(i+Squad_V*(j-1))][int(i+Squad_V*j)]=1
    #print('')

print('==============')

with open('C:\\Users\\90612\\Desktop\\graph_array.txt','w') as f:
    for i in array:
        #print('{',end='')
        f.write('{')
        for index,j in enumerate(i):
            #print(int(j),end='')
            f.write(str(int(j)))
            if(index!=V-1):
                #print(', ',end='')
                f.write(', ')
        #print('},')
        f.write('},\n')

