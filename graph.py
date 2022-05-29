import networkx as nx
import matplotlib.pyplot as plt


from pygraph.classes.digraph import digraph
from pygraph.algorithms.minmax import maximum_flow



gr=digraph()
gr.add_nodes(['F',1,2,'B'])
gr.add_edge(('F',1),wt=4)
gr.add_edge((1,2),wt=3)
gr.add_edge((2,'B'),wt=5)
gr.add_edge(('F',2),wt=3)
gr.add_edge((1,'B'),wt=4)

flows,cuts = maximum_flow(gr, 'F', 'B')
print('flow is ',flows)
print('cuts are ',cuts)


G = nx.DiGraph()
G.add_weighted_edges_from([('F','1', 4), ('F','2',3),('1','2',3), ('1','B',4) ,('2','B',5) ])
labels = nx.get_edge_attributes(G, 'weight')

val_map = {
    'F': 1.0,
    'B': 0.00
}

values = [ val_map.get(nodes, 0.50) for nodes in G.nodes()]



pos = nx.planar_layout(G)
nx.draw_networkx_nodes(G,pos , cmap=plt.get_cmap('spring'), node_size=500 , node_color=values)
nx.draw_networkx_edges(G,pos, width=6, edgelist=G.edges(),edge_color='black')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels )
nx.draw_networkx_labels(G,pos, font_size=20, font_family='sans-serif')
plt.show()

