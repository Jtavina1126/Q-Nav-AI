from fastapi import FastAPI
from schemas import ResonanceInput, BlipInput, HarmonicInput, MergeInput
from resonance_model import predict_resonance
from blip_engine import simulate_blip
from harmonic_detector import calculate_harmonic_index
from merge_mental_coherence import calculate_mental_coherence_merge

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Q-Nav AI Backend is live."}

@app.post("/predict_resonance")
def predict(input_data: ResonanceInput):
    result = predict_resonance(input_data)
    return {"resonance": result}

@app.post("/simulate_blip")
def simulate(input_data: BlipInput):
    blip = simulate_blip(input_data)
    return {"blip_result": blip}

@app.post("/detect_harmonic_resonance")
def detect_harmonic(input_data: HarmonicInput):
    return calculate_harmonic_index(input_data)

@app.post("/merge_mental_coherence")
def merge_minds(input_data: MergeInput):
    return calculate_mental_coherence_merge(input_data.person_1, input_data.person_2)