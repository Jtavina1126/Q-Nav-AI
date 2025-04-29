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