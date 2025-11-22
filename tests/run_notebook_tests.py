# tests/run_notebook_tests.py
import nbformat, asyncio, uuid, json, os, pytest
NOTEBOOK_PATHS = [
    "community-risk-intelligence-agent.ipynb",
    "community-risk-agent_patched.ipynb",
    "community_risk_agent_submission.ipynb",
    "community_risk_agent_offline.ipynb",
    "community_risk_agent_notebook_patched.ipynb",
    "community-risk-agent.ipynb"
]
SKIP_LIVE = not bool(os.environ.get("GOOGLE_API_KEY"))

def find_notebook():
    for p in NOTEBOOK_PATHS:
        if os.path.exists(p):
            return p
    pytest.skip("No target notebook found in repo root for tests. Ensure one of the expected notebooks is present.")

def exec_notebook_top_cells(nb_path, keywords=None, max_cells=80):
    nb = nbformat.read(nb_path, as_version=4)
    env = {}
    executed_any = False
    for i, cell in enumerate(nb.cells):
        if cell.cell_type != 'code':
            continue
        src = cell.source
        run_cell = False
        if keywords is None:
            run_cell = True
        else:
            for kw in keywords:
                if kw.lower() in src.lower():
                    run_cell = True
                    break
        if run_cell:
            exec(compile(src, f"<nbcell-{i}>", 'exec'), env)
            executed_any = True
        if i >= max_cells:
            break
    return env, executed_any

def test_localstub_defined():
    nb_path = find_notebook()
    env, executed = exec_notebook_top_cells(nb_path, keywords=['localstubllm','class localstubllm','class LocalStubLLM'], max_cells=80)
    assert executed, "No relevant cells executed from notebook; check notebook structure."
    assert 'LocalStubLLM' in env, "LocalStubLLM class not found after executing notebook cells."
    llm_cls = env['LocalStubLLM']
    sample = {'id': str(uuid.uuid4()), 'type': 'weather', 'location': 'downtown', 'meta': {'severity_hint': 0.1}}
    loop = asyncio.new_event_loop()
    try:
        asyncio.set_event_loop(loop)
        coro = llm_cls().classify_event(sample)
        out = loop.run_until_complete(coro)
    finally:
        loop.close()
    assert isinstance(out, dict)
    assert 'score' in out and 'category' in out and 'rationale' in out
