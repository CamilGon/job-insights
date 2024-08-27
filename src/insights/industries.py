from typing import List
from src.insights.jobs import ProcessJobs


class ProcessIndustries(ProcessJobs):
    def __init__(self) -> None:
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        sole_industries = set()
        for job in self.jobs_list:
            industry = job.get("industry")
            if industry:
                sole_industries.add(industry)
        return list(sole_industries)
