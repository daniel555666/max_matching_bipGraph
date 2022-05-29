import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite



def change_to_bipG(G,M,NodesA,NodesB,MNodes):

    BP=nx.DiGraph() #made the graph nodes
    BP.add_nodes_from(NodesA,bipartite=0)
    BP.add_nodes_from(NodesB,bipartite=1)

    for e in G.edges():

        if e[0] not in MNodes and e[0] in NodesA :#A\M out edges
            BP.add_edges_from([e])
            continue
        if e[1] not in MNodes and e[1] in NodesA:
            BP.add_edges_from([(e[1],e[0])])
            continue

        #A with M and B\M
        if (e[0] in MNodes and e[0] in NodesA )and (e[1] in NodesB and e[1] not in MNodes):
            BP.add_edges_from([e])
            continue
        if (e[1] in MNodes and e[1] in NodesA )and (e[0] in NodesB and e[0] not in MNodes):
            BP.add_edges_from([(e[1],e[0])])
            continue

        if e in M: # edges of M
            if e[0] in NodesA:
                BP.add_edges_from([(e[1], e[0])])
            else :
                BP.add_edges_from([e])

        else:
            if e[0] in NodesA:
                BP.add_edges_from([e])
            else :
                BP.add_edges_from([(e(1),e(0))])
    pos = nx.bipartite_layout(BP, [1, 2, 3, 4], align='vertical', scale=2)
    nx.draw_networkx_nodes(BP, pos, nodelist=BP.nodes(), node_color='r', node_size=500)
    nx.draw_networkx_edges(BP, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_labels(BP, pos, font_size=16)
    #plt.show()
    return BP

def agumnting_path(BP,MNodes,NodesA,NodeB):
    pathNodes=[]
    for e in BP.edges():
        if e[0] in NodesA and e[0] not in MNodes:
            pathNodes.insert(len(pathNodes),e[0])
            pathNodes.insert(len(pathNodes),e[1])
            return rec_agumnting_path(BP,MNodes,NodesA,NodeB,pathNodes)
            break
    return []  # if didnt found


def rec_agumnting_path(BP,MNodes,NodesA,NodeB,pathNodes):
    if pathNodes[len(pathNodes)-1] in NodeB and pathNodes[len(pathNodes)-1] not in MNodes:
        return pathNodes
    for e in BP.edges():
        if e[0]==pathNodes[len(pathNodes)-1]:
            pathNodes.insert(len(pathNodes),e[1])
            return rec_agumnting_path(BP,MNodes,NodesA,NodeB,pathNodes)

    return [] # if didnt found

def showGui(BP):

    pos = nx.bipartite_layout(BP, [1, 2, 3], align='vertical', scale=2)
    nx.draw_networkx_nodes(BP, pos, nodelist=BP.nodes(), node_color='r', node_size=500)
    nx.draw_networkx_edges(BP, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_labels(BP, pos, font_size=16)
    plt.show()


def get_matching(B):
    M = []

    NodesA = []
    NodesB = []
    dict = B.nodes.data()
    for v in dict:
        if v[1] == {'bipartite': 0}:
            NodesA.append(v[0])
        else:
            NodesB.append(v[0])
    while 1>0:
        MNodes = []
        for e in M:  # save the nodes in the matching
            if e[0] not in MNodes:
                MNodes.append(e[0])
            if e[1] not in MNodes:
                MNodes.append((e[1]))

        BP=change_to_bipG(B, M, NodesA, NodesB,MNodes)
        #fig = plt.figure()
     #   timer = fig.canvas.new_timer(interval=300)
     #   timer.add_callback(showGui(BP))


        better_path=agumnting_path(BP,MNodes,NodesA,NodesB)
        if len(better_path)==0: #stop the loop
            break
        # change the matching
        for e in M:
            if e[0]in better_path or e[1]in better_path:
                M.remove(e)
        for i in range(len(better_path))[0::2]:
            if(i%2==0):
                M.insert(len(M),(better_path[i],better_path[i+1]))


    return M



if __name__ == '__main__':
    # BP = nx.DiGraph()
    # BP.add_nodes_from([1, 2, 3], bipartite=0)
    # BP.add_nodes_from([11, 12, 13], bipartite=1)
    # BP.add_edges_from([(1, 11), (12, 2)])
    #
    B = nx.Graph()
    B.add_nodes_from([1, 2, 3, 4], bipartite=0)
    B.add_nodes_from(['a', 'b', 'c', 'd', 'e'], bipartite=1)
    B.add_edges_from([(1, 'a'), (1, 'b'), (2, 'c'), (2, 'd'), (3, 'b'), (3, 'd'), (4, 'a'), (4, 'c')])

    pos = nx.bipartite_layout(B, [1, 2, 3, 4], align='vertical', scale=2)
    nx.draw_networkx_nodes(B, pos, nodelist=B.nodes(), node_color='r', node_size=500)
    nx.draw_networkx_edges(B, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_labels(B, pos, font_size=16)
    M= get_matching(B)
    print(M)


    # for e in B.edges():
    #     print(e)
    # pos = nx.bipartite_layout(BP, [1, 2, 3], align='vertical', scale=2)
    # nx.draw_networkx_nodes(BP, pos, nodelist=BP.nodes(), node_color='r', node_size=500)
    # nx.draw_networkx_edges(BP, pos, width=1.0, alpha=0.5)
    # nx.draw_networkx_labels(BP, pos, font_size=16)
    # plt.show()