import requests
import json

# from app.celery_worker import celery_app


# @celery_app.task(acks_late=True, queue="flight_search")
# def flights_search():
#     response_a = requests.post("http://app:9000/provider_a/search")
#     response_b = requests.post("http://app:9000/provider_b/search")

#     return json.loads(response_a.text) + json.loads(response_b.text)
