from ai.llm import call_llm
from ai.prompt import build_prompt
from confidence.engine import assess_confidence

def analyze_findings(findings, ai_profile):
    prompt = build_prompt(findings, ai_profile)
    ai_output = call_llm(prompt)

    results = ai_output.get("findings", [])

    for r in results:
        r["confidence"] = assess_confidence(
            r.get("exploitability_score", 0),
            r.get("exploitability_score", 0)
        )

    return results
