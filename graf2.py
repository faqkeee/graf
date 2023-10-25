import pickle as pkl
import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()

nodes=["1","2","3","4","5","6","7","8","9","10","11","12"]
G.add_nodes_from(nodes)
G.add_edge("1","2")
G.add_edge("1","3")
G.add_edge("3","4")
G.add_edge("3","5")
G.add_edge("4","5")
G.add_edge("4","6")
G.add_edge("5","6")
G.add_edge("6","7")
G.add_edge("7","8")
G.add_edge("7","9")
G.add_edge("9","10")
G.add_edge("10","11")
G.add_edge("11","12")
print(G.nodes())

f=open("plik.obj", 'wb')
pkl.dump(G, f)
f.close()

fa = open("plik.obj",'rb')
G = pkl.load(fa)
print(G.edges())
nx.draw(G, with_labels = True)
plt.savefig("simple_path.png") 
plt.show() 
