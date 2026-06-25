Cleaning and structuroing the data
  1. We remove fields that are irrelevant for this analysis.
  2. We create 5 tables: People, Experiences, Educations, Companies, Schools.
  3. We normalize Company and School names with plain Python.
  4. We perform entity resolution/normalization on company names to unify close institutions.
  5. We add the normalized names to the initial data.
    
Creating the network
  - The network is bipartite and heterogeneous. Then we project it into a one-mode company-company graph.
  Nodes
  1. Person
  2. Company
  3. School (Not used)

  Edges
  1. WORKED_IN (certain company)
  2. ATTENDED (certain school) (not used)
    
Metrics analysed
  1. Degree
  2. Centrality (degree, betweennes and eigenvector)
  3. Density
  4. Connected components
  5. Clustering
  6. Communities

Key connectors
  1. Clemson University holds the highest centrality.
  2. If we look closely at LPL Financial, it has relatively low degree centrality but high Eigenvector centrality, usually meaning that it has good connections.
  3. We don't have enough data to do this with people nodes since the degree of every person is around 2 and 3.

Assumptions
  1. We assume that different representations of the same organization or person have been successfully consolidated. Incorrect merging or splitting can significantly alter degree, centrality, and community structure.
  2. All relationships have equal importance

Limitations
  1. Incomplete data
  2. Community detection is basic and can be further analysed.
  3. Edges are unweighted.
  4. Time-lapses of when people worked at each company not taken into account.