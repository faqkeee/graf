import pickle as pkl
import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()
## G = nx.MultiDiGraph()
nodes=["0", "1", "2", "3","4"]
G.add_nodes_from(nodes)
G.add_edge("0","1")
G.add_edge("2","3")
G.add_edge("4","1")
G.add_edge("4","3")
G.add_edge("1","2")
print(G.nodes())
##serializacja – zapis do pliku
f=open("plik.obj", 'wb')
pkl.dump(G, f)
f.close()
##deserializacja – odczyt z pliku
fa = open("plik.obj",'rb')
G = pkl.load(fa)
print(G.edges())
nx.draw(G, with_labels = True)
plt.savefig("simple_path.png") # save as png >>>
plt.show() # display