from locust import HttpLocust, TaskSet, task
from random import randint

class MyTaskSet(TaskSet):
    rand_user = None

    def on_start(self):
        self.rand_user = randint(1, 999999999)
        print("username = ", self.rand_user)

    @task(10)
    def view(self):
        self.client.get("/jsp/rss.jsp")

    @task(1)
    def addAbc(self):
        self.client.post("/jsp/rss.jsp", {"url":"http://rssserver/abc.xml", "username":self.rand_user})

    @task(1)
    def addBbc(self):
        self.client.post("/jsp/rss.jsp", {"url":"http://rssserver/bbc.xml", "username":self.rand_user})

    @task(1)
    def addCnn(self):
        self.client.post("/jsp/rss.jsp", {"url":"http://rssserver/cnn.xml", "username":self.rand_user})

    @task(1)
    def addDw(self):
        self.client.post("/jsp/rss.jsp", {"url":"http://rssserver/dw.xml", "username":self.rand_user})

    @task(1)
    def addForbes(self):
        self.client.post("/jsp/rss.jsp", {"url":"http://rssserver/forbes.xml", "username":self.rand_user})

    @task(1)
    def addReuters(self):
        self.client.post("/jsp/rss.jsp", {"url":"http://rssserver/reuters.xml", "username":self.rand_user})

    @task(1)
    def addSpiegel(self):
        self.client.post("/jsp/rss.jsp", {"url":"http://rssserver/spiegel.xml", "username":self.rand_user})

    @task(1)
    def addWsj(self):
        self.client.post("/jsp/rss.jsp", {"url":"http://rssserver/wsj.xml", "username":self.rand_user})

    @task(1)
    def deleteAbc(self):
        self.client.post("/jsp/rss.jsp", {"delFeedUrl":"http://rssserver/abc.xml", "username":self.rand_user})

    @task(1)
    def deleteBbc(self):
        self.client.post("/jsp/rss.jsp", {"delFeedUrl":"http://rssserver/bbc.xml", "username":self.rand_user})

    @task(1)
    def deleteCnn(self):
        self.client.post("/jsp/rss.jsp", {"delFeedUrl":"http://rssserver/cnn.xml", "username":self.rand_user})

    @task(1)
    def deleteDw(self):
        self.client.post("/jsp/rss.jsp", {"delFeedUrl":"http://rssserver/dw.xml", "username":self.rand_user})

    @task(1)
    def deleteForbes(self):
        self.client.post("/jsp/rss.jsp", {"delFeedUrl":"http://rssserver/forbes.xml", "username":self.rand_user})

    @task(1)
    def deleteReuters(self):
        self.client.post("/jsp/rss.jsp", {"delFeedUrl":"http://rssserver/reuters.xml", "username":self.rand_user})

    @task(1)
    def deleteSpiegel(self):
        self.client.post("/jsp/rss.jsp", {"delFeedUrl":"http://rssserver/spiegel.xml", "username":self.rand_user})

    @task(1)
    def deleteWsj(self):
        self.client.post("/jsp/rss.jsp", {"delFeedUrl":"http://rssserver/wsj.xml", "username":self.rand_user})

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 10000
