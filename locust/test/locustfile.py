from locust import HttpLocust, TaskSet, task
from locust import events
from random import randint
import json
import requests
from influxdb import InfluxDBClient
import os

class MyTaskSet(TaskSet):

    def on_start(self):
        self.user_id = randint(1,999999999)

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

def on_request_success(request_type, name, response_time, response_length, **kw):
    json_body = [
            {
                "measurement": "test_results",
                "tags": {
                    "request_type": request_type,
                    "name": name,
                    "exception": ""
                    },
                "fields": {
                    "request_type": request_type,
                    "name": name,
                    "response_time": response_time,
                    "response_length": response_length,
                    "exception": ""
                    }
                }
            ]
    client.write_points(json_body)

def on_request_failure(request_type, name, response_time, exception, **kw):
    json_body = [
            {
                "measurement": "test_results",
                "tags": {
                    "request_type": request_type,
                    "name": name,
                    "exception": str(exception)
                    },
                "fields": {
                    "request_type": request_type,
                    "name": name,
                    "response_time": response_time,
                    "response_length": 0,
                    "exception": str(exception)
                    }
                }
            ]
    client.write_points(json_body)

influxdb_url = os.environ['INFLUXDB_URL']
influxdb_port = os.environ['INFLUXDB_PORT']
events.request_success += on_request_success
events.request_failure += on_request_failure
client = InfluxDBClient(influxdb_url, influxdb_port, 'root', 'root', 'locust')
client.create_database('locust')
