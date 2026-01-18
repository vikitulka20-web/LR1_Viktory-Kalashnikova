import json
from typing import List, Dict


def task() -> float:
    with open('input.json', 'r', encoding='utf-8') as file:
        data: List[Dict[str, float]] = json.load(file)

    total_sum = 0.0

    for item in data:
        score = item.get("score", 0.0)
        weight = item.get("weight", 0.0)
        total_sum += score * weight

    return round(total_sum, 3)

print(task())