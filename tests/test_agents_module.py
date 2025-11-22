import asyncio, uuid
from project_package import agents

def run(coro):
    loop = asyncio.new_event_loop()
    try:
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(coro)
    finally:
        loop.close()

def test_localstub_classify_returns_expected_keys():
    sample = {'id': str(uuid.uuid4()), 'type': 'weather', 'meta': {'severity_hint': 0.1}}
    out = run(agents.LocalStubLLM().classify_event(sample))
    assert isinstance(out, dict)
    assert 'score' in out and 'category' in out and 'rationale' in out
