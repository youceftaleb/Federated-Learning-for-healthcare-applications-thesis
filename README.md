# Optimizing Federated Learning for Healthcare Applications

> Master's Thesis — University of Science and Technology Houari Boumediene (USTHB)

---

## Overview

This repository contains the full LaTeX source of the thesis **"Optimizing Federated Learning for Healthcare Applications"**. The work investigates federated learning (FL) as a privacy-preserving paradigm for training AI models across multiple collaborating healthcare institutions without sharing raw patient data.

The thesis compares and optimizes several aggregation strategies and communication schemes in FL, evaluated on two clinical case studies:

- **Case Study 1 — EEG Signals**: Epilepsy detection from electroencephalographic recordings
- **Case Study 2 — Medical Imaging**: Cancer sub-type classification from imaging data

---

## Thesis Structure

```
main.tex                  ← Root document
citation.bib              ← Bibliography (BibLaTeX)
Chapters/
├── introduction.tex      ← General introduction
├── chapter1.tex          ← Chapter 1: Medical Context and AI Foundations
├── chapter2.tex          ← Chapter 2: Federated Learning — State of the Art
├── chapter3.tex          ← Chapter 3: Proposed Architecture and Methodology
├── chapter4.tex          ← Chapter 4: Implementation and Results
├── conclusions.tex       ← General conclusion and perspectives
├── abstract.tex          ← Abstract (English)
├── resume.tex            ← Résumé (French)
├── acknowledgements.tex  ← Acknowledgements
├── acronyms.tex          ← List of acronyms
└── appendix.tex          ← Appendix
figures/
└── USTHB.png             ← University logo and thesis figures
```

---

## Table of Contents (Summary)

| Chapter | Title |
|---------|-------|
| 1 | Medical Context and AI Foundations for Healthcare Data Analysis |
| 2 | Federated Learning — State of the Art |
| 3 | Proposed Architecture and Methodology |
| 4 | Implementation and Results |

### Chapter 1 — Medical Context and AI Foundations
- Healthcare institutions, data silos, GDPR/HIPAA constraints
- Medical data modalities: EEG signals, medical imaging, clinical data
- AI foundations: machine learning, deep learning (CNNs, RNNs, EEGNet, Transformers)
- Model evaluation framework

### Chapter 2 — Federated Learning State of the Art
- From centralized to distributed learning
- FL architecture: client-server paradigm, communication rounds
- Aggregation strategies: FedAvg, FedProx, FedNova, SCAFFOLD
- Communication optimization, privacy mechanisms (differential privacy, secure aggregation)
- Existing FL frameworks: Flower, FedML, Substra, PySyft

### Chapter 3 — Proposed Architecture and Methodology
- Overall federated system design
- EEG preprocessing and local model architecture (EEGNet)
- Medical imaging preprocessing and CNN-based local model
- Proposed aggregation strategy optimizations
- Communication scheme optimizations
- Privacy preservation configuration
- Evaluation protocol

### Chapter 4 — Implementation and Results
- Hardware/software environment
- Federated system simulation setup
- Results: epilepsy detection from EEG (per aggregation strategy)
- Results: cancer sub-type classification from imaging (per aggregation strategy)
- Comparative analysis, privacy-utility trade-off, comparison with state of the art
- Application presentation

---

## Key Topics

- Federated Learning (FL)
- Privacy-Preserving Machine Learning
- Aggregation Strategies (FedAvg, FedProx, FedNova, SCAFFOLD)
- Communication Optimization in FL
- Differential Privacy / Secure Aggregation
- EEG Signal Processing & Epilepsy Detection
- Medical Image Classification & Cancer Sub-Types
- Deep Learning: CNN, RNN, EEGNet, Transformers
- Non-IID Data, Convergence Stability
- FL Frameworks: Flower (Flwr), FedML, Substra

---

## Collaboration Guide

### Workflow

1. Always branch off, never commit directly to `main`
2. Open a pull request to `main` when a section is ready for review
3. Merge to `main` only when a chapter is finalized and reviewed by both collaborators

### Commit Message Convention

```
[ch1] Add AI section and evaluation metrics
[ch2] Rewrite FedProx subsection
[bib] Add missing citations for Chapter 3
[fig] Add federation architecture diagram
[fix] Correct compilation error in acronymes.tex
```

---

## Authors

| Name | Role |
|------|------|
| [Youcef Taleb](https://github.com/youceftaleb) | Author |
| [Yazid Bensefia](https://github.com/alphaacode) | Author |

> USTHB — Department of Computer Science
> Academic Year: 2025–2026

---

## License

This repository contains academic work. All rights reserved. Do not reproduce or distribute without the authors' explicit permission.