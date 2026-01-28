def assess_confidence(finding, ai_score):
    if ai_score >= 9:
        return "CONFIRMED"
    if ai_score >= 7:
        return "LIKELY"
    if ai_score >= 4:
        return "UNCERTAIN"
    return "FALSE_POSITIVE"
