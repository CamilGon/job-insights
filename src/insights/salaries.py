from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self) -> None:
        super().__init__()

    def get_max_salary(self) -> int:
        
        max_salary = 0
        for job in self.jobs_list:
            max_salary_str = job.get("max_salary")
            if max_salary_str and max_salary_str.isdigit():
                max_salary = max(max_salary, int(max_salary_str))
        return max_salary

    def get_min_salary(self) -> int:
        
        min_salaries = [
            int(job["min_salary"])
            for job in self.jobs_list
            if job.get("min_salary") and job["min_salary"].isdigit()
        ]
        if not min_salaries:
            raise ValueError("Nenhum salário mínimo válido encontrado.")
        return min(min_salaries)

    def matches_salary_range(self, job: Dict[str, str], salary: Union[int, str]) -> bool:
     
        try:
            salary = int(salary)
            max_salary = int(job["max_salary"])
            min_salary = int(job["min_salary"])
        except (ValueError, KeyError, TypeError) as e:
            raise ValueError("Valor do salário inválido.") from e

        if max_salary < min_salary:
            raise ValueError("Salário máximo é menor que o salário mínimo.")

        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[Dict[str, str]], salary: Union[str, int]
    ) -> List[Dict[str, str]]:

        try:
            salary = int(salary)
        except ValueError:
            raise ValueError("O salário deve ser um número inteiro.")

        filtered_jobs = []
        for job in jobs:
            try:
                if self.matches_salary_range(job, salary):
                    filtered_jobs.append(job)
            except ValueError:
                # Se o job não tem salários válidos, não adiciona ao filtro
                continue

        return filtered_jobs
