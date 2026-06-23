filtered_df = experience_df[
    experience_df["company"].isin(top_companies.index)
]

B = nx.Graph()

for _, row in filtered_df.iterrows():
    person = row["person_id"]
    company = row["company"]

    B.add_node(person, bipartite=0)
    B.add_node(company, bipartite=1)

    B.add_edge(person, company)

people = {
    n for n, d in B.nodes(data=True)
    if d["bipartite"] == 0
}

companies = set(B) - people

pos = nx.bipartite_layout(
    B,
    people,
)

plt.figure(figsize=(16, 12))

nx.draw_networkx_nodes(
    B,
    pos,
    nodelist=people,
    node_size=50,
    alpha=0.6
)

nx.draw_networkx_nodes(
    B,
    pos,
    nodelist=companies,
    node_size=300,
    alpha=0.8
)

nx.draw_networkx_edges(
    B,
    pos,
    alpha=0.2
)

nx.draw_networkx_labels(
    B,
    pos,
    labels={c: c for c in companies},
    font_size=8
)

plt.savefig("graph.png")
plt.show()

