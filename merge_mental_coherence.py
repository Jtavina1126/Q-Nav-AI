def calculate_mental_coherence_merge(p1, p2):
    score = 0

    # Alpha/Theta similarity (ideal range match and closeness)
    if 1.3 <= p1["alpha_theta_ratio"] <= 2.0 and 1.3 <= p2["alpha_theta_ratio"] <= 2.0:
        diff = abs(p1["alpha_theta_ratio"] - p2["alpha_theta_ratio"])
        score += max(0.3 - diff * 0.2, 0)  # subtract for distance

    # HRV match
    hrv_diff = abs(p1["hrv"] - p2["hrv"])
    score += max(0.3 - hrv_diff * 0.005, 0)

    # Emotional coherence sync
    if p1["emotional_coherence"] == p2["emotional_coherence"] == "high":
        score += 0.2
    elif p1["emotional_coherence"] == p2["emotional_coherence"]:
        score += 0.1

    # Spiritual safety
    if "surrendered" in (p1["spiritual_state"], p2["spiritual_state"]):
        score += 0.15
        safety = "clear"
    elif "aligned" in (p1["spiritual_state"], p2["spiritual_state"]):
        score += 0.1
        safety = "moderate"
    else:
        safety = "uncertain"

    # Output
    coherence_index = round(min(score, 1.0), 3)
    return {
        "coherence_sync_index": coherence_index,
        "resonant_channel": "harmonic-theta" if coherence_index >= 0.75 else "unstable",
        "recommended_method": "binaural + breath sync + mutual prayer" if coherence_index >= 0.75 else "recalibration required",
        "spiritual_safety": safety
    }