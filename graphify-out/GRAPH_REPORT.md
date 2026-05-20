# Graph Report - .  (2026-05-06)

## Corpus Check
- Corpus is ~1,271 words - fits in a single context window. You may not need a graph.

## Summary
- 27 nodes · 23 edges · 9 communities detected
- Extraction: 78% EXTRACTED · 22% INFERRED · 0% AMBIGUOUS · INFERRED: 5 edges (avg confidence: 0.79)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_FL Algorithms & Privacy|FL Algorithms & Privacy]]
- [[_COMMUNITY_Healthcare Applications & Neural Architectures|Healthcare Applications & Neural Architectures]]
- [[_COMMUNITY_Data Heterogeneity & Convergence|Data Heterogeneity & Convergence]]
- [[_COMMUNITY_FL Frameworks|FL Frameworks]]
- [[_COMMUNITY_RNN Models|RNN Models]]
- [[_COMMUNITY_Transformers|Transformers]]
- [[_COMMUNITY_Substra Framework|Substra Framework]]
- [[_COMMUNITY_PySyft Framework|PySyft Framework]]
- [[_COMMUNITY_USTHB Institution|USTHB Institution]]

## God Nodes (most connected - your core abstractions)
1. `Federated Learning` - 9 edges
2. `Optimizing Federated Learning for Healthcare Applications` - 4 edges
3. `EEG Signals` - 3 edges
4. `Medical Imaging` - 3 edges
5. `FedAvg` - 2 edges
6. `FedProx` - 2 edges
7. `FedNova` - 2 edges
8. `SCAFFOLD` - 2 edges
9. `Differential Privacy` - 2 edges
10. `Secure Aggregation` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Optimizing Federated Learning for Healthcare Applications` --produced_by_institution--> `USTHB University Logo and Thesis Title`  [EXTRACTED]
  README.md → figures\USTHB.png

## Hyperedges (group relationships)
- **FL Aggregation Strategies** — readme_fedavg, readme_fedprox, readme_fednova, readme_scaffold [EXTRACTED 1.00]
- **Federated Learning Frameworks** — readme_flowerflwr, readme_fedml, readme_substra, readme_pysyft [EXTRACTED 1.00]
- **Privacy Mechanisms in FL** — readme_differentialprivacy, readme_secureaggregation [EXTRACTED 0.90]

## Communities

### Community 0 - "FL Algorithms & Privacy"
Cohesion: 0.31
Nodes (9): Communication Optimization, Differential Privacy, FedAvg, Federated Learning, FedNova, FedProx, Privacy-Preserving Machine Learning, SCAFFOLD (+1 more)

### Community 1 - "Healthcare Applications & Neural Architectures"
Cohesion: 0.25
Nodes (9): Master's Thesis Document, USTHB University Logo and Thesis Title, Cancer Sub-type Classification, CNN, EEGNet, EEG Signals, Epilepsy Detection, Medical Imaging (+1 more)

### Community 2 - "Data Heterogeneity & Convergence"
Cohesion: 1.0
Nodes (2): Convergence Stability, Non-IID Data

### Community 3 - "FL Frameworks"
Cohesion: 1.0
Nodes (2): FedML, Flower (Flwr)

### Community 4 - "RNN Models"
Cohesion: 1.0
Nodes (1): RNN

### Community 5 - "Transformers"
Cohesion: 1.0
Nodes (1): Transformers

### Community 6 - "Substra Framework"
Cohesion: 1.0
Nodes (1): Substra

### Community 7 - "PySyft Framework"
Cohesion: 1.0
Nodes (1): PySyft

### Community 8 - "USTHB Institution"
Cohesion: 1.0
Nodes (1): UniversitÃ© des Sciences et de la Technologie Houari Boumediene

## Knowledge Gaps
- **14 isolated node(s):** `Epilepsy Detection`, `Cancer Sub-type Classification`, `Communication Optimization`, `RNN`, `Transformers` (+9 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Data Heterogeneity & Convergence`** (2 nodes): `Convergence Stability`, `Non-IID Data`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `FL Frameworks`** (2 nodes): `FedML`, `Flower (Flwr)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `RNN Models`** (1 nodes): `RNN`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Transformers`** (1 nodes): `Transformers`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Substra Framework`** (1 nodes): `Substra`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `PySyft Framework`** (1 nodes): `PySyft`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `USTHB Institution`** (1 nodes): `UniversitÃ© des Sciences et de la Technologie Houari Boumediene`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Federated Learning` connect `FL Algorithms & Privacy` to `Healthcare Applications & Neural Architectures`?**
  _High betweenness centrality (0.298) - this node is a cross-community bridge._
- **Why does `Optimizing Federated Learning for Healthcare Applications` connect `Healthcare Applications & Neural Architectures` to `FL Algorithms & Privacy`?**
  _High betweenness centrality (0.271) - this node is a cross-community bridge._
- **What connects `Epilepsy Detection`, `Cancer Sub-type Classification`, `Communication Optimization` to the rest of the system?**
  _14 weakly-connected nodes found - possible documentation gaps or missing edges._