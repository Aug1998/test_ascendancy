1. Clean and structure the data.
  1. Removed irrelevant fields.
  2. Created 5 tables: People, Experiences, Educations, Companies, Schools.
  3. Normalized Company and School names. There are NLP, machine-learning tools like SentenceTransformers, which we could leverage but for now we can do with plain python.
  4. Perform entity resolution/normalization on company names
  5. Add the normalized names to the initial data
    
2. Creating the network.
    1. Define nodes and edges
    The network will be multipartite and heterogeneous, meaning it will have multiple types of node. We’re gonna create a projected graph aftewards to analyse the relationships between companies.
    1. Person
    2. Company
    3. School

Edges will be either

1. ATTENDED (certain school)
2. WORKED_IN (certain company)
    
3. Generate metrics.
    1. Degree
    2. Centrality
    3. Density
    4. Connected components
    5. Clustering
    6. Community detection
4. Observations.
    
    Observations
    
5. Assumptions, limitations, and suggested next steps.
    
    Assumptions & Limitations
    
6. Deliver the code and a short walkthrough video explaining approach, decisions, and findings.

What I'd show in a final report