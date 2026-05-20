import json
from pathlib import Path

ast = json.loads(Path('graphify-out/.graphify_ast.json').read_text()) if Path('graphify-out/.graphify_ast.json').exists() else {'nodes':[],'edges':[]}
sem_new = json.loads(Path('graphify-out/.graphify_semantic_new.json').read_text()) if Path('graphify-out/.graphify_semantic_new.json').exists() else {'nodes':[],'edges':[],'hyperedges':[]}
cached = json.loads(Path('graphify-out/.graphify_cached.json').read_text()) if Path('graphify-out/.graphify_cached.json').exists() else {'nodes':[],'edges':[],'hyperedges':[]}

all_nodes = cached['nodes'] + sem_new.get('nodes', [])
all_edges = cached['edges'] + sem_new.get('edges', [])
all_hyperedges = cached.get('hyperedges', []) + sem_new.get('hyperedges', [])

seen = set()
deduped = []
for n in all_nodes:
    if n['id'] not in seen:
        seen.add(n['id'])
        deduped.append(n)

merged = {
    'nodes': deduped,
    'edges': all_edges,
    'hyperedges': all_hyperedges,
    'input_tokens': sem_new.get('input_tokens', 0),
    'output_tokens': sem_new.get('output_tokens', 0),
}
Path('graphify-out/.graphify_semantic.json').write_text(json.dumps(merged, indent=2))
print(f'Semantic: {len(deduped)} nodes, {len(all_edges)} edges')

# Part C - Merge AST + semantic
ast_nodes = ast.get('nodes', [])
ast_edges = ast.get('edges', [])
sem = json.loads(Path('graphify-out/.graphify_semantic.json').read_text())

seen_ids = {n['id'] for n in ast_nodes}
merged_nodes = list(ast_nodes)
for n in sem['nodes']:
    if n['id'] not in seen_ids:
        merged_nodes.append(n)
        seen_ids.add(n['id'])

merged_edges = ast_edges + sem['edges']
merged_hyperedges = sem.get('hyperedges', [])

final = {
    'nodes': merged_nodes,
    'edges': merged_edges,
    'hyperedges': merged_hyperedges,
    'input_tokens': sem.get('input_tokens', 0),
    'output_tokens': sem.get('output_tokens', 0),
}
Path('graphify-out/.graphify_extract.json').write_text(json.dumps(final, indent=2))
print(f'Merged: {len(merged_nodes)} nodes, {len(merged_edges)} edges')