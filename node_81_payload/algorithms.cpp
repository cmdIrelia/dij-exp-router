#include "stdafx.h"
#include<iostream>
#include <fstream>
#include <string>
#include <iomanip>

#include <cmath>
#include <vector>
#include <algorithm>

#include<stack>
#include<queue>

#include "graph_array.h"

using namespace std;
// Number of vertices in the graph
//#define V 81

#define Tmax 6

#define DST_NODE V-1

#define FLOAT_MAX (999.99f)

//����һ���ڵ��pֵ
float calcP(float node_value, float new_node_value)
{
	if (new_node_value > Tmax - node_value) 
	{
		return FLOAT_MAX;
	}
	else
	{
		float p = (new_node_value) / (Tmax - node_value);
		return p;
	}
}

////�������·���ڵ��Ȩֵ  gȨֵͼ  g_value�ۼ�ռ��ͼ  new_node_value��ӵ�ֵ
//void updateGraph(float g[V][V], int dst, int prev[V], float g_value[V][V], float new_node_value)
//{
//	int cur_v = dst;
//	do
//	{
//		//printf(" %d", prev[cur_v]);
//		int touch_index = prev[cur_v];
//		for (int i = 0; i < V; i++) 
//		{
//			if (g[touch_index][i] != 0) //�Ǹ�ͨ·���Գ�������ֻ�ж�һ��
//			{
//				//δ�����
//				if (g_value[touch_index][i] >= 0)
//				{
//					g_value[touch_index][i] += new_node_value;
//					g_value[i][touch_index] += new_node_value;
//
//					//���Ϊ�Ѵ���
//					g_value[touch_index][i] = -g_value[touch_index][i];
//					g_value[i][touch_index] = -g_value[i][touch_index];
//				}
//			}
//		}
//		cur_v = prev[cur_v];
//	} while (prev[cur_v] != 0);
//
//	//�Ѹ��ű��ȥ��
//	for (int i = 0; i < V; i++)
//		for (int j = 0; j < V; j++)
//			if (g_value[i][j] < 0)
//				g_value[i][j] = -g_value[i][j];
//}

//�������·���ڵ��Ȩֵ  gȨֵͼ  g_value�ۼ�ռ��ͼ  new_node_value��ӵ�ֵ
void updateGraph(float g[V][V], int dst, int prev[V], float g_value[V][V], float new_node_value)
{
	int cur_v = dst;
	int previous_index = dst;
	do
	{
		//printf(" %d", prev[cur_v]);
		int touch_index = prev[cur_v];

		g_value[touch_index][previous_index] += new_node_value;
		g_value[previous_index][touch_index] += new_node_value;

		previous_index = touch_index;

		cur_v = prev[cur_v];
	} while (prev[cur_v] != 0);

	//���һ���ڵ�ָ��source�������п�������sourceָ��source�����������һ�����䡣
	if (previous_index != 0)
	{
		g_value[prev[cur_v]][previous_index] += new_node_value;
		g_value[previous_index][prev[cur_v]] += new_node_value;
	}
}

//α��������ͼ��Ȩֵ  gȨֵͼ  g_value�ۼ�ռ��ͼ  new_node_value��ӵ�ֵ
void fakeUpdateGraph(float g[V][V], float g_value[V][V], float new_node_value)
{
	for (int i = 0; i < V; i++)
	{
		for (int j = 0; j < V; j++)
		{
			if (g[i][j] != 0)
			{
				float p = calcP(g_value[i][j], new_node_value);
				g[i][j] = exp(p);
			}
		}
	}
}

//��������һ��ͼ
void copyGraph(float g[V][V], float new_g[V][V])
{
	for (int i = 0; i < V; i++)
	{
		for (int j = 0; j < V; j++)
		{
			new_g[i][j] = g[i][j];
		}
	}
}

//��ӡgͼ
void printGraph(float g[V][V])
{
	for (int i = 0; i < V; i++)
	{
		for (int j = 0; j < V; j++)
		{
			cout << g[i][j]<<'\t';
		}
		cout << endl;
	}
}

// A utility function to find the vertex with minimum distance value, from
// the set of vertices not yet included in shortest path tree
int minDistance(float dist[], bool sptSet[])
{
	// Initialize min value
	float min = FLOAT_MAX;
	int min_index;

	for (int v = 0; v < V; v++)
		if (sptSet[v] == false && dist[v] <= min)
		{
			min = dist[v];
			min_index = v;
		}

	return min_index;
}

//��ӡ��to������·��
void printSolutionTo(int to, int prev[V])
{
	int cur_v = to;
	do
	{
		printf(" %d", prev[cur_v]);
		cur_v = prev[cur_v];
	} while (prev[cur_v] != 0);
	printf("\n");
}

// A utility function to print the constructed distance array
int printSolution(float dist[], int n, int prev[V])
{
	printf("Vertex \t\t Distance from Source\n");
	for (int i = 0; i < V; i++) {
		printf("%d \t\t %f", i, dist[i]);

		//����߳����·�������
		printf("\t path:");
		int cur_v = i;
		//int previous_index = i;	///
		do
		{
			//int touch_index = prev[cur_v];///
			//previous_index = touch_index;///
			//cout << "previous_index=" << previous_index << "  cur_v=" << cur_v;///
			printf(" %d", prev[cur_v]);
			cur_v = prev[cur_v];
		} while (prev[cur_v] != 0);
		printf("\n");
	}
	return 0;
}

// Funtion that implements Dijkstra's single source shortest path algorithm
// for a graph represented using adjacency matrix representation
void dijkstra(float graph[V][V], int src, int prev[V])
{
	float dist[V];     // The output array.  dist[i] will hold the shortest
					 // distance from src to i

	bool sptSet[V]; // sptSet[i] will true if vertex i is included in shortest
					// path tree or shortest distance from src to i is finalized

					// Initialize all distances as INFINITE and stpSet[] as false
	for (int i = 0; i < V; i++)
		dist[i] = FLOAT_MAX, sptSet[i] = false;

	// Distance of source vertex from itself is always 0
	dist[src] = 0;

	// Find shortest path for all vertices
	for (int count = 0; count < V - 1; count++)
	{
		// Pick the minimum distance vertex from the set of vertices not
		// yet processed. u is always equal to src in first iteration.
		int u = minDistance(dist, sptSet);

		// Mark the picked vertex as processed
		sptSet[u] = true;


		// Update dist value of the adjacent vertices of the picked vertex.
		for (int v = 0; v < V; v++) {

			// Update dist[v] only if is not in sptSet, there is an edge from 
			// u to v, and total weight of path from src to  v through u is 
			// smaller than current value of dist[v]
			if (!sptSet[v] && graph[u][v] && dist[u] != FLOAT_MAX
				&& dist[u] + graph[u][v] < dist[v]) {
				dist[v] = dist[u] + graph[u][v];

				prev[v] = u;	//�������·��ǰһ���ڵ��
								//cout << u << "->" << v << " ";
			}
		}
	}

	// print the constructed distance array
	//printSolution(dist, V, prev);
}

// driver program to test above function
int main()
{
	const char redirect_path[] = "C:\\Users\\90612\\Desktop\\path_result.txt";
	cout << "redirect_path: " << redirect_path << endl;
	// ����cout��������ָ��
	streambuf* coutBuf = cout.rdbuf();
	//�ض���
	ofstream of(redirect_path);
	// ��ȡ�ļ�out.txt��������ָ��
	streambuf* fileBuf = of.rdbuf();
	// ����cout��������ָ��Ϊout.txt����������ָ��
	cout.rdbuf(fileBuf);

	//ԭͼ
	/* Let us create the example graph discussed above */
	//float graph[V][V] = {
	//	//0	 1  2  3  4  5  6  7  8  9  10
	//	{ 0, 4, 0, 0, 0, 0, 0, 8, 1, 1, 0},	//0
	//	{ 4, 0, 8, 0, 0, 0, 0,11, 0, 0, 0},	//1
	//	{ 0, 8, 0, 7, 0, 4, 0, 0, 2, 0, 0},	//2
	//	{ 0, 0, 7, 0, 9,14, 0, 0, 0, 0, 0},	//3
	//	{ 0, 0, 0, 9, 0,10, 0, 0, 1, 0, 1},	//4
	//	{ 0, 0, 4,14,10, 0, 2, 0, 0, 0, 0},	//5
	//	{ 0, 0, 0, 0, 0, 2, 0, 1, 6, 0, 0},	//6
	//	{ 8, 11,0, 0, 0, 0, 1, 0, 7, 0, 0},	//7
	//	{ 1, 0, 2, 0, 1, 0, 6, 7, 0, 0, 0},	//8
	//	{ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},	//9
	//	{ 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0}	//10
	//};

	//�ڵ��ۼ�ռ����ͼ
	float graph_node_value[V][V];
	memset(graph_node_value, 0, sizeof(float)*V*V);

	int prev[V] = { 0 };//�������·��ǰһ���ڵ��

	
	//��ͼ������ͨ·�����дΪ1
	for (int i = 0; i < V; i++) 
	{
		for (int j = 0; j < V; j++)
		{
			if (graph[i][j] != 0)
			{
				graph[i][j] = 1;
			}
		}
	}


	cout << "No Variable Weight with dijkstra." << endl;
	dijkstra(graph, 0, prev);
	//��ӡ��to�����·��
	cout << "path to node " << DST_NODE;
	printSolutionTo(DST_NODE, prev);

	cout << "print graph" << endl;
	printGraph(graph);

	float new_node_value[] = { 0.5f,1,2,2,0.1f,0.5f,0.2f,0.7,0.5,0.1,0.2,0.1,1,1.7,0.6 };
	const int NEW_NODE_VALUE_LEN = sizeof(new_node_value) / sizeof(new_node_value[0]);
	int new_node_index = 0;
	float graph_temp[V][V];

	cout << "NEW_NODE_VALUE_LEN = " << NEW_NODE_VALUE_LEN << endl;
	cout << "sum payload = ";
	float sum_payload = 0;
	for (int i = 0; i < NEW_NODE_VALUE_LEN; i++)
	{
		sum_payload += new_node_value[i];
	}
	cout << sum_payload << endl;
	/****************** new_node_index=i ********************************/
	for (int increse_index_loop = 0; increse_index_loop < NEW_NODE_VALUE_LEN; increse_index_loop++)
	{
		printf("******* new_node_index=%d *********\n", new_node_index);
		/*��Ȩ��dij*/
		cout << "Variable Weight with dijkstra: " << new_node_value[new_node_index] << endl;
		copyGraph(graph_node_value, graph_temp);

		//α����ȫͼ
		fakeUpdateGraph(graph, graph_node_value, new_node_value[new_node_index]);
		cout << "α����ȫͼ" << endl;
		printGraph(graph);

		dijkstra(graph, 0, prev);
		//��ӡ��to�����·��
		cout << "path to node DST_NODE: ";
		printSolutionTo(DST_NODE, prev);

		//����ȫͼ
		updateGraph(graph, DST_NODE, prev, graph_node_value, new_node_value[new_node_index]);

		//��ӡ���º�ͼ
		//cout << "��ӡȨֵͼ" << endl;
		//printGraph(graph);
		cout << "��ӡռ��ͼ" << endl;
		printGraph(graph_node_value);

		new_node_index++;
	}


	of.flush();
	of.close();
	// �ָ�coutԭ������������ָ��
	cout.rdbuf(coutBuf);
	cout << "Program done." << endl;

	system("pause");

	return 0;
}
