import networkx as nx
import matplotlib.pyplot as plt

# Build bipartite graph from filtered experiences
filtered_df = experience_df[experience_df["company"].isin(top_companies.index)]
B = nx.Graph()
for _, row in filtered_df.iterrows():
    B.add_edge(row["person_id"], row["company"])

# Companies are the cluster "supernodes"
companies = list(top_companies.index)

# Create a supergraph (one node per company) to compute well-spaced centers
supergraph = nx.cycle_graph(len(companies))
superpos = nx.spring_layout(supergraph, scale=3, seed=42)
centers = list(superpos.values())

# For each company, compute a local layout for the company + its people
pos = {}
for center, company in zip(centers, companies):
    members = [company] + list(B.neighbors(company))
    if len(members) == 1:
        # company with no people — place at center
        pos[company] = tuple(center)
        continue
    subpos = nx.spring_layout(B.subgraph(members), center=center, seed=123)
    # Ensure the company stays at the exact center
    subpos[company] = tuple(center)
    pos.update(subpos)

# Draw
plt.figure(figsize=(14, 14))
nx.draw_networkx_edges(B, pos, alpha=0.08, width=0.6)

# People nodes: all nodes that are not company labels
people = [n for n in B.nodes() if n not in companies]
nx.draw_networkx_nodes(B, pos, nodelist=people, node_size=40, node_color="lightblue", alpha=0.7)

# Company nodes: larger and labeled
nx.draw_networkx_nodes(B, pos, nodelist=companies, node_size=900, node_color="coral", alpha=0.95)
nx.draw_networkx_labels(B, pos, labels={c: c for c in companies}, font_size=8)

plt.title("Companies as Cluster Centers with Their People")
plt.axis("off")
plt.tight_layout()
plt.savefig("graph.png", dpi=200)
plt.show()