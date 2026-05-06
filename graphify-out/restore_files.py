import json
from pathlib import Path

analysis = {
  "communities": {
    "0": ["readme_communicationoptimization", "readme_differentialprivacy", "readme_fedavg", "readme_federatedlearning", "readme_fednova", "readme_fedprox", "readme_privacypreservingmachinelearning", "readme_scaffold", "readme_secureaggregation"],
    "1": ["figures_masters", "figures_usthb", "readme_cancersubtypeclassification", "readme_cnn", "readme_eegnet", "readme_eegsignals", "readme_epilepsydetection", "readme_medicalimaging", "readme_optimizingfederatedlearning"],
    "2": ["readme_convergencestability", "readme_non-iiddat"],
    "3": ["readme_fedml", "readme_flowerflwr"],
    "4": ["readme_rnn"],
    "5": ["readme_transformers"],
    "6": ["readme_substra"],
    "7": ["readme_pysyft"],
    "8": ["figures_ustbh"]
  },
  "cohesion": {
    "0": 0.31,
    "1": 0.25,
    "2": 1.0,
    "3": 1.0,
    "4": 1.0,
    "5": 1.0,
    "6": 1.0,
    "7": 1.0,
    "8": 1.0
  },
  "gods": [
    {"id": "readme_federatedlearning", "label": "Federated Learning", "degree": 9},
    {"id": "readme_optimizingfederatedlearning", "label": "Optimizing Federated Learning for Healthcare Applications", "degree": 4},
    {"id": "readme_eegsignals", "label": "EEG Signals", "degree": 3},
    {"id": "readme_medicalimaging", "label": "Medical Imaging", "degree": 3}
  ],
  "surprises": [
    {"source": "Optimizing Federated Learning for Healthcare Applications", "target": "USTHB University Logo and Thesis Title", "source_files": ["README.md", "figures\\USTHB.png"], "confidence": "EXTRACTED", "relation": "produced_by_institution", "why": "crosses file types"}
  ],
  "questions": [
    {"type": "bridge_node", "question": "Why does `Federated Learning` connect `Community 0` to `Community 1`?", "why": "High betweenness centrality"},
    {"type": "isolated_nodes", "question": "What connects `Epilepsy Detection` to the rest?", "why": "14 weakly-connected nodes"}
  ]
}

labels = {
  "0": "FL Algorithms & Privacy",
  "1": "Healthcare Applications & Neural Architectures",
  "2": "Data Heterogeneity & Convergence",
  "3": "FL Frameworks",
  "4": "RNN Models",
  "5": "Transformers",
  "6": "Substra Framework",
  "7": "PySyft Framework",
  "8": "USTHB Institution"
}

Path('graphify-out/.graphify_analysis.json').write_text(json.dumps(analysis))
Path('graphify-out/.graphify_labels.json').write_text(json.dumps(labels))
print('Restored analysis and labels')