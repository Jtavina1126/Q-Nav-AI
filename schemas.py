from pydantic import BaseModel
from typing import List

class ResonanceInput(BaseModel):
    input_coordinates: List[float]
    input_field_strength: float
    observer_mindset: str

class BlipInput(BaseModel):
    blip_seed: float
    intensity: float
    entropy_bias: float
    
class HarmonicInput(BaseModel):
    hrv: float  # Heart rate variability (0-100)
    alpha_theta_ratio: float  # Brainwave balance
    emotional_coherence: str  # 'high', 'moderate', 'low'
    spiritual_state: str  # 'surrendered', 'dissonant', 'aligned', 'disconnected'