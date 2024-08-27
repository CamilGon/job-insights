from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list: List[Dict[str, str]] = []

    def read(self, path: str) -> None:
        try:
            with open(path, mode="r", newline="", encoding="utf-8") as file:
                self.jobs_list = list(csv.DictReader(file))
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {path}")
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")

    def get_unique_job_types(self) -> List[str]:
        job_types = set()
        for job in self.jobs_list:
            job_type = job.get("job_type")
            if job_type:
                job_types.add(job_type)
        return list(job_types)

    def filter_by_multiple_criteria(
        self, jobs: List[Dict[str, str]], filter: Dict[str, str]
    ) -> List[Dict[str, str]]:
        if not isinstance(filter, dict):
            raise TypeError("O filtro deve ser um dicionário")
        industry = filter.get("industry")
        job_type = filter.get("job_type")

        if industry is None or job_type is None:
            return []

        return [
            job
            for job in jobs
            if job.get("industry") == industry and job.get("job_type") == job_type
        ]
