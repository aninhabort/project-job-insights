from typing import Union, List, Dict

from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    salary_file = read(path)
    all_salary = set()

    for item in salary_file:
        salary = item['max_salary']
        if salary.isdigit():
            all_salary.add(int(salary))

    return max(all_salary)


def get_min_salary(path: str) -> int:
    salary_file = read(path)
    all_salary = set()

    for item in salary_file:
        salary = item['min_salary']
        if salary.isdigit():
            all_salary.add(int(salary))

    return min(all_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if int(job['min_salary']) > int(job['max_salary']):
            raise ValueError

        return int(job['min_salary']) <= int(salary) <= int(job['max_salary'])

    except KeyError:
        raise ValueError

    except TypeError:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    all_salary = []

    for job in jobs:
        try:
            match_salary = matches_salary_range(job, salary)
            if match_salary:
                all_salary.append(job)
        except ValueError:
            None

    return all_salary
