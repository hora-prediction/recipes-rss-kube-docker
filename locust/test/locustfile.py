from locust import HttpLocust, TaskSet, task
from random import randint

class MyTaskSet(TaskSet):

    def on_start(self):
        self.user_id = randint(1,999999999)
        print("username = ", self.user_id)

    @task(1)
    def view(self):
        self.client.get("/jsp/rss.jsp")

    @task(1)
    def addAbc(self):
        self.client.post("/jsp/rss.jsp", {"url":"http://rssserver/abc.xml", "username":self.user_id})

    @task(1)
    def addBbc(self):
        self.client.post("/jsp/rss.jsp", {"url":"http://rssserver/bbc.xml", "username":self.user_id})

    @task(1)
    def addCnn(self):
        self.client.post("/jsp/rss.jsp", {"url":"http://rssserver/cnn.xml", "username":self.user_id})

    @task(1)
    def addDw(self):
        self.client.post("/jsp/rss.jsp", {"url":"http://rssserver/dw.xml", "username":self.user_id})

    @task(1)
    def addForbes(self):
        self.client.post("/jsp/rss.jsp", {"url":"http://rssserver/forbes.xml", "username":self.user_id})

    @task(1)
    def addReuters(self):
        self.client.post("/jsp/rss.jsp", {"url":"http://rssserver/reuters.xml", "username":self.user_id})

    @task(1)
    def addSpiegel(self):
        self.client.post("/jsp/rss.jsp", {"url":"http://rssserver/spiegel.xml", "username":self.user_id})

    @task(1)
    def addWsj(self):
        self.client.post("/jsp/rss.jsp", {"url":"http://rssserver/wsj.xml", "username":self.user_id})

    @task(1)
    def deleteAbc(self):
        self.client.post("/jsp/rss.jsp", {"delFeedUrl":"http://rssserver/abc.xml", "username":self.user_id})

    @task(1)
    def deleteBbc(self):
        self.client.post("/jsp/rss.jsp", {"delFeedUrl":"http://rssserver/bbc.xml", "username":self.user_id})

    @task(1)
    def deleteCnn(self):
        self.client.post("/jsp/rss.jsp", {"delFeedUrl":"http://rssserver/cnn.xml", "username":self.user_id})

    @task(1)
    def deleteDw(self):
        self.client.post("/jsp/rss.jsp", {"delFeedUrl":"http://rssserver/dw.xml", "username":self.user_id})

    @task(1)
    def deleteForbes(self):
        self.client.post("/jsp/rss.jsp", {"delFeedUrl":"http://rssserver/forbes.xml", "username":self.user_id})

    @task(1)
    def deleteReuters(self):
        self.client.post("/jsp/rss.jsp", {"delFeedUrl":"http://rssserver/reuters.xml", "username":self.user_id})

    @task(1)
    def deleteSpiegel(self):
        self.client.post("/jsp/rss.jsp", {"delFeedUrl":"http://rssserver/spiegel.xml", "username":self.user_id})

    @task(1)
    def deleteWsj(self):
        self.client.post("/jsp/rss.jsp", {"delFeedUrl":"http://rssserver/wsj.xml", "username":self.user_id})

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 10000
