import time
from locust import HttpUser, TaskSet, task, between

class SubClassTest(TaskSet):

    @task
    def main_page(self):
        self.client.post(url ="/cv/")

    @task(2)
    def perihal_page(self):
        self.client.get(url ="/projects/")


class MainClassTest(HttpUser):
    tasks = [SubClassTest]
    wait_time = between(5, 10)