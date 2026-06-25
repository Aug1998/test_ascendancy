# Network Analysis

This project turns messy professional profile data into a usable relationship map that helps identify influential organizations, talent pathways, and hidden institutional connections.

Instead of treating records as isolated entries, it builds a network view that reveals:
- which companies and schools act as key connectors,
- where talent clusters form,
- and which institutions are structurally important even when they are not the most frequent.

## Why This Matters

This analysis is useful for answering high-value questions such as:
- Which organizations sit at the center of the network?
- Which institutions connect otherwise separate communities?
- Where do influential career transitions tend to happen?

## What This Project Does

### 1) Data Cleaning and Structuring
1. Removes fields that are not needed for the analysis.
2. Builds 5 structured tables:
   - People
   - Experiences
   - Educations
   - Companies
   - Schools
3. Normalizes company and school names with Python-based matching.
4. Applies entity-resolution logic so similar institution names map to one canonical name.
5. Writes normalized organization names back into the workflow outputs.

### 2) Network Construction
- Uses a heterogeneous bipartite graph and projects it into a one-mode company-to-company graph.

Nodes:
1. Person
2. Company
3. School (currently not used in network analysis)

Edges:
1. WORKED_IN (person -> company)
2. ATTENDED (person -> school, currently not used)

### 3) Metrics Analyzed
1. Degree
2. Centrality (degree, betweenness, eigenvector)
3. Density
4. Connected components
5. Clustering
6. Communities

## Key Findings
1. Clemson University has the highest centrality in the analyzed network.
2. LPL Financial shows relatively low degree centrality but high eigenvector centrality, suggesting strong links to influential nodes.
3. Person-level conclusions are limited because most people have low degree (around 2-3).

## Assumptions
1. Different representations of the same person or organization are correctly consolidated.
2. All relationships are treated with equal weight.

## Limitations
1. Data is incomplete.
2. Community detection is basic and can be improved.
3. Edges are unweighted.
4. Time overlap and chronology of employment are not modeled.

## Project Structure

- `data.json`: source data
- `src/clean_data.py`: builds structured tables
- `src/normalization.py`: organization name normalization logic
- `Jupyter.ipynb`: interactive analysis notebook

## Requirements

- Python 3.10+
- pip

Optional:
- virtual environment (`venv`)
- JupyterLab for notebook-based execution

## Setup

From the project root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## How To Run

### Option A: Run the Notebook (Recommended)

```bash
jupyter lab
```

Then open `Jupyter.ipynb` and run cells top-to-bottom.

### Option B: Install JupyterLab extension in your IDE


## Troubleshooting

1. If `jupyter` command is not found, run:
   ```bash
   pip install jupyterlab
   ```
2. If imports from `src` fail, make sure you are running commands from the project root directory.
3. If package installation fails, verify your Python version and update pip.

## Demo
If you want you can check out this walkthrough video recording

https://drive.google.com/drive/u/0/folders/1bFNBqj4f65N8mlDtvmUXX2uAeln5o42K