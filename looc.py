from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    def on_start(self):
        """ This is run when a simulated user starts interacting with the system. """
        self.login()

    @task(1)
    def login(self):
        """ Simulate user login with valid credentials. """
        response = self.client.post("/form_login",data={
            "username": "nachi",  # Replace with a valid username from your database
            "password": "123"     # Replace with a valid password
       })
        if "Invalid" in response.text:
            print("Login failed.")
        else:
            print("Login succeeded.")

   # @task(2)
    #def load_home_page(self):
        """ Simulate user navigating to the home page after logging in. """
       # self.client.get("/")

class WebsiteUser(HttpUser):
    host = "http://127.0.0.1:5000" 
    tasks = [UserBehavior]
    wait_time = between(1, 3)  # Simulate a delay of 1 to 3 seconds between user actions
