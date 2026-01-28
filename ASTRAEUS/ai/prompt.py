def build_prompt(findings, profile):
    return f"""
You are a senior penetration tester.

AI PROFILE:
Aggressiveness: {profile['aggressiveness']}
False Positive Tolerance: {profile['false_positive_tolerance']}
Focus Areas: {profile['focus']}

Rules:
- Output JSON only
- Prioritize exploitability
- Remove noise

Findings:
{findings}
"""
