from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    industry_file = read(path)
    all_indrustries = set()

    for item in industry_file:
        indrustry = item['industry']
        if indrustry != '':
            all_indrustries.add(indrustry)

    return all_indrustries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    all_industry = []

    for item in jobs:
        if item['industry'] == industry:
            all_industry.append(item)

    return all_industry
