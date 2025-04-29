from pydantic import BaseModel
from typing import List, Dict

class ResonanceInput(BaseModel):
    input_coordinates: List[float]
    input_field_strength: float
    observer_mindset: str

class BlipInput(BaseModel):
    blip_seed: float
    intensity: float
    entropy_bias: float

class HarmonicInput(BaseModel):
    hrv: float
    alpha_theta_ratio: float
    emotional_coherence: str
    spiritual_state: str

class IndividualInput(BaseModel):
    hrv: float
    alpha_theta_ratio: float
    emotional_coherence: str
    spiritual_state: str

class MergeInput(BaseModel):
    person_1: Dict[str, float or str]
    person_2: Dict[str, float or str]