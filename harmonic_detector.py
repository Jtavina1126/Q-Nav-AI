def calculate_harmonic_index(data):
    score = 0

    # Normalize HRV
    if data.hrv >= 80:
        score += 0.35
    elif data.hrv >= 60:
        score += 0.25
    else:
        score += 0.1

    # Brainwave ratio
    if 1.3 <= data.alpha_theta_ratio <= 2.0:
        score += 0.3
    else:
        score += 0.15

    # Emotional coherence
    if data.emotional_coherence == 'high':
        score += 0.2
    elif data.emotional_coherence == 'moderate':
        score += 0.1

    # Spiritual state
    if data.spiritual_state == 'surrendered':
        score += 0.15
    elif data.spiritual_state == 'aligned':
        score += 0.1

    # Output
    return {
        "harmonic_index": round(score, 3),
        "frequency_signature": round(430 + score * 10, 2),
        "alignment_state": (
            "Resonant" if score > 0.75 else
            "Partial Harmony" if score > 0.5 else
            "Misaligned"
        )
    }