from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, "r", encoding="utf-8") as file:
        jobs = csv.DictReader(file)
        return list(jobs)


def get_unique_job_types(path: str) -> List[str]:
    jobs_type_file = read(path)
    all_job_type = set()

    for item in jobs_type_file:
        jobs = item['job_type']
        all_job_type.add(jobs)

    return all_job_type


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    all_job_type = []

    for item in jobs:
        if item['job_type'] == job_type:
            all_job_type.append(item)

    return all_job_type
