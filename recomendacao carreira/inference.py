# motor de inferencia

from knowledge_base import RULES

def forward_chaining(facts):
    recommendations = []

    for rule in RULES:
        if all(facts.has_fact(cond) for cond in rule["conditions"]):
            recommendations.append(rule["career"])

    return recommendations
