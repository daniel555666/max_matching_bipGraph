import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk


# When we have bipartite graph we want to find the max edge matching:
# The hungarian method serching for argumenting path on the graph and change the edges it take
# By using the graph as directed graph we can to look if there is a better path
 
 
# cases for making the directed graph if there is undricted edge between them we will make it directed as following:
# (node from A but not from M) --> (node from B)
# (node from A and from M) --> (node from B and from M) - if the nodes pointing to another group this mean that this edge is already need to be part of the matching.
# All the node in the matching point from B to A.

# change our graph to bipartite graph
# that all paths are augmenting paths

# The function get: 1.graph(G) 2. edges of the matching (M), 3. The vertecies of the group A on the grpah(NodesA) 4. The vertecies of the group B on the grpah(NodesB) , 5.vertices of the matching (MNodes)
def change_to_bipG(G, M, NodesA, NodesB, MNodes):
    BP = nx.DiGraph()  # made the graph nodes
    BP.add_nodes_from(NodesA, bipartite=0)
    BP.add_nodes_from(NodesB, bipartite=1)
    for e in G.edges(): ## tuple of the nodes of the edge
        
         # A\M out edges
        if e[0] not in MNodes and e[0] in NodesA: 
            BP.add_edges_from([e])
            continue
        if e[1] not in MNodes and e[1] in NodesA:
            BP.add_edges_from([(e[1], e[0])])
            continue

        # A with M and B\M
        if (e[0] in MNodes and e[0] in NodesA) and (e[1] in NodesB and e[1] not in MNodes):
            BP.add_edges_from([e])
            continue
        if (e[1] in MNodes and e[1] in NodesA) and (e[0] in NodesB and e[0] not in MNodes):
            BP.add_edges_from([(e[1], e[0])])
            continue

        # edges of M
        if e in M:  
            if e[0] in NodesA:
                BP.add_edges_from([(e[1], e[0])])
            else:
                BP.add_edges_from([e])

        else:
            if e[0] in NodesA:
                BP.add_edges_from([e])
            else:
                BP.add_edges_from([(e(1), e(0))])
    pos = nx.bipartite_layout(BP, [1, 2, 3, 4], align='vertical', scale=2)
    nx.draw_networkx_nodes(BP, pos, nodelist=BP.nodes(), node_color='r', node_size=500)
    nx.draw_networkx_edges(BP, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_labels(BP, pos, font_size=16)
    # plt.draw()
    return BP

# find the augmenting path in the bipartite graph.
# return the path with nodes list
def agumnting_path(BP, MNodes, NodesA, NodeB):
    pathNodes = []
    for e in BP.edges():
        # search for node on A\m and send its edge for looking id it is connecting to node in B\m 
        if e[0] in NodesA and e[0] not in MNodes:
            pathNodes.insert(len(pathNodes), e[0])
            pathNodes.insert(len(pathNodes), e[1])
            return rec_agumnting_path(BP, MNodes, NodesA, NodeB, pathNodes)
            break
    return []  # if didnt found


# a recursive function to find the augmenting path for the travel on the bipartite graph
def rec_agumnting_path(BP, MNodes, NodesA, NodeB, pathNodes):
    # if the node we insert at the end of the list ending in B\M we find augmenting path and we done.
    if pathNodes[len(pathNodes) - 1] in NodeB and pathNodes[len(pathNodes) - 1] not in MNodes:
        return pathNodes
    # else we serch if there is edge that exit from the same vertex and not on the current matching M, if it is we will add the vertex and keep serching from this position edge ending in B\M
    for e in BP.edges():
        if e[0] == pathNodes[len(pathNodes) - 1] and e[1]not in MNodes: #for get the path with the 2 sides not in M first
            pathNodes.insert(len(pathNodes), e[1])
            return rec_agumnting_path(BP, MNodes, NodesA, NodeB, pathNodes)
    
    for e in BP.edges():                         #we can return visit to BNodes but not to ANodes
        if e[0] == pathNodes[len(pathNodes) - 1] and((e[1] in NodeB) or (e[1]not in pathNodes and e[1]in NodesA)): #keep the path and take vertex we didint visit
            pathNodes.insert(len(pathNodes), e[1])
            return rec_agumnting_path(BP, MNodes, NodesA, NodeB, pathNodes)
    # for e in BP.edges():
    #     if e[0] == pathNodes[len(pathNodes) - 1]: #keep the path
    #         pathNodes.insert(len(pathNodes), e[1])
    #         return rec_agumnting_path(BP, MNodes, NodesA, NodeB, pathNodes)
    return []  # if didnt found


# start the algorithem for finding maxium matching
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

    layout = nx.bipartite_layout(B, NodesA, align= 'vertical', scale= 2)
    num_of_plots = 0
    while 1 > 0:
        MNodes = []
        for e in M:  # save the nodes in the matching
            if e[0] not in MNodes:
                MNodes.append(e[0])
            if e[1] not in MNodes:
                MNodes.append((e[1]))

        BP = change_to_bipG(B, M, NodesA, NodesB, MNodes)
        # fig = plt.figure()
        #   timer = fig.canvas.new_timer(interval=300)
        #   timer.add_callback(showGui(BP))
        better_path = agumnting_path(BP, MNodes, NodesA, NodesB)
        print(better_path)


        # here we want to print the augmenting path
        if not better_path:  # stop the loo
            break

        better_path_edges = []

        for i in range(len(better_path) - 1):
            better_path_edges.append((better_path[i], better_path[i + 1]))
        plt.clf()
        draw_augmented_path(BP, layout, better_path_edges, M)
        plt.pause(3)

        num_of_plots += 1
        # updates.append(update)

        # change the matching to the new matching
        for e in M:
            if e[0] in better_path or e[1] in better_path:
                M.remove(e)
        for i in range(len(better_path))[0::2]:
            #if (i % 2 == 0):
            M.insert(len(M), (better_path[i], better_path[i + 1]))

    return M


# init the graph from the user , begin the algorithem for finding maximum matching
# and print the matching
def run_algo (a_nodes, b_nodes, edges):
    plt.clf()
    B = nx.Graph()
    B.add_nodes_from(a_nodes, bipartite=0)
    B.add_nodes_from(b_nodes, bipartite=1)
    B.add_edges_from(edges)
    layout = nx.bipartite_layout(B, a_nodes, align='vertical', scale=2)

    # nx.draw_networkx_nodes(B, pos, nodelist=B.nodes(), node_color='r', node_size=500)
    # nx.draw_networkx_edges(B, pos, width=1.0, alpha=0.5)
    # nx.draw_networkx_labels(B, pos, font_size=16)
    M = get_matching(B)
    plt.clf()
    nx.draw_networkx_nodes(B, layout, nodelist=B.nodes(), node_color='r', node_size=500)
    # nx.draw_networkx_edges(B.edges, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_edges(B, layout, edgelist=B.edges, edge_color='gray', arrows=True)
    nx.draw_networkx_edges(B, layout, edgelist=M, edge_color='r', arrows=True)

    nx.draw_networkx_labels(B, layout, font_size=16)
    plt.pause(3)
    print(M)


# drawer of the graph
def draw_augmented_path(G, pos, path, M):
    red_edges = []
    blue_edges = []

    for edge in path:
        if tuple(reversed(edge)) in M:
            red_edges.append(edge)
        else:
            blue_edges.append(edge)
    # pos = nx.bipartite_layout(G, [1, 2, 3, 4], align='vertical', scale=2)
    # pos = nx.bipartite_layout(G, [1,2], align='vertical', scale=2)
    print("MATCHING", red_edges)
    print("NOT MATCHING", blue_edges)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color='gray', arrows=True)
    nx.draw_networkx_nodes(G, pos, nodelist=G.nodes(), node_color='r', node_size=500)
    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=blue_edges, edge_color='b', arrows=True)
    nx.draw_networkx_labels(G, pos, font_size=14)

# the gui is using matplotlib to draw the graph and tkinter for the GUI controller
from tkinter import *
def runGUI():
    top = tk.Tk()

    def helloCallBack():
        print("Hello")


    B_label = tk.Label(top, text="A (only numeric characters)")
    B_label.pack()
    B_textBox = tk.Entry(top, bd=5)
    B_textBox.pack()

    A_label = tk.Label(top, text="B (only alphabetic characters)")
    A_label.pack()
    A_textBox = tk.Entry(top, bd=5)
    A_textBox.pack()

    edges_label = tk.Label(top, text="EDGES")
    edges_label.pack()
    edges_textBox = tk.Entry(top, bd=5)
    edges_textBox.pack()

    def getData():
        A_nodes = A_textBox.get().split(" ")
        A_nodes = [node for node in A_nodes if len(node) == 1 and node.isalpha()]
        B_nodes = B_textBox.get().split(" ")
        B_nodes = [node for node in B_nodes if len(node) == 1 and node.isnumeric()]
        edges_input_array = edges_textBox.get().split(" ")
        edges_input_array = [edge for edge in edges_input_array if edge != '' and edge != ' ']
        edges = []
        for edge_str in edges_input_array:
            splitted = edge_str.replace('(', '').replace(')', '').split(",")
            edges.append((splitted[0], splitted[1]))
        top.quit()
        run_algo(A_nodes, B_nodes, edges)

    ok_button = tk.Button(top, text = "OK", command = getData )
    ok_button.pack()
    top.mainloop()


if __name__ == '__main__':
    runGUI()


