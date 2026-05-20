import json
from graphify.build import build_from_json
from graphify.export import to_obsidian, to_canvas
from pathlib import Path

extraction = json.loads(Path('graphify-out/.graphify_extract.json').read_text())
analysis   = json.loads(Path('graphify-out/.graphify_analysis.json').read_text())
labels_raw = json.loads(Path('graphify-out/.graphify_labels.json').read_text()) if Path('graphify-out/.graphify_labels.json').exists() else {}

G = build_from_json(extraction)
communities = {int(k): v for k, v in analysis['communities'].items()}
cohesion = {int(k): v for k, v in analysis['cohesion'].items()}
labels = {int(k): v for k, v in labels_raw.items()}

obsidian_dir = 'graphify-out/obsidian'

n = to_obsidian(G, communities, obsidian_dir, community_labels=labels or None, cohesion=cohesion)
print(f'Obsidian vault: {n} notes in {obsidian_dir}/')

to_canvas(G, communities, f'{obsidian_dir}/graph.canvas', community_labels=labels or None)
print(f'Canvas: {obsidian_dir}/graph.canvas - open in Obsidian for structured community layout')
print()
print(f'Open {obsidian_dir}/ as a vault in Obsidian.')
print('  Graph view   - nodes colored by community (set automatically)')
print('  graph.canvas - structured layout with communities as groups')
print('  _COMMUNITY_* - overview notes with cohesion scores and dataview queries')