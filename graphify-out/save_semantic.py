import json
from pathlib import Path

chunk_file = Path('graphify-out/.graphify_chunk_01.json')
if chunk_file.exists():
    chunk_result = json.loads(chunk_file.read_text())
    Path('graphify-out/.graphify_semantic_new.json').write_text(json.dumps(chunk_result))
    print(f'Extracted: {len(chunk_result["nodes"])} nodes, {len(chunk_result["edges"])} edges')
else:
    print('Error: chunk file not found')