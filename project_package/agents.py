import asyncio, uuid, json
from typing import Dict, Any

class LLMInterface:
    async def classify_event(self, event: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError
    async def generate_guidance(self, alert: Dict[str, Any]) -> str:
        raise NotImplementedError

class LocalStubLLM(LLMInterface):
    async def classify_event(self, event: Dict[str, Any]) -> Dict[str, Any]:
        base = event.get('meta', {}).get('severity_hint', 0.1)
        type_map = {'fire': 0.9, 'air_quality': 0.6, 'weather': 0.4, 'news': 0.3, 'transport': 0.2}
        score = min(1.0, base * 0.7 + type_map.get(event.get('type'), 0.2) * 0.5)
        category = 'high' if score > 0.7 else ('medium' if score > 0.4 else 'low')
        rationale = f"Heuristic: base={base:.2f}, type_weight={type_map.get(event.get('type'),0.2):.2f} -> score={score:.2f}"
        return {'score': score, 'category': category, 'rationale': rationale}

class EventBus:
    def __init__(self):
        self._subs = {}
    def subscribe(self, event_name: str, handler):
        self._subs.setdefault(event_name, []).append(handler)
    async def publish(self, event_name: str, payload: Dict[str, Any]):
        handlers = self._subs.get(event_name, [])
        await asyncio.gather(*(h(payload) for h in handlers))

class Agent:
    def __init__(self, name: str, bus: EventBus):
        self.name = name
        self.bus = bus
    def log(self, obj: Dict[str, Any]):
        pass

class RiskAnalysisAgent(Agent):
    def __init__(self, name, bus, llm):
        super().__init__(name,bus)
        self.llm = llm
        bus.subscribe('raw_event', self.on_raw_event)
    async def on_raw_event(self, raw_event):
        result = await self.llm.classify_event(raw_event)
        score = float(result.get('score',0.0))
        category = result.get('category','low')
        alert = {'alert_id': str(uuid.uuid4()), 'source_event_id': raw_event.get('id'), 'category': category, 'score': score, 'rationale': result.get('rationale',''), 'location': raw_event.get('location'), 'summary': raw_event.get('text'), 'raw': raw_event}
        await self.bus.publish('alert', alert)

def compute_env_score(weather: Dict[str, Any]) -> float:
    pm = weather.get('pm2_5',0)
    pm_score = min(1.0, pm / 200.0)
    return pm_score
