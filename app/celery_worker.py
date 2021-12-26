import os
import celery
import requests
import json

from celery import Celery


celery = Celery(__name__)
celery.conf.broker_url = os.environ["CELERY_BROKER_URL"]
celery.conf.result_backend = os.environ["CELERY_RESULT_BACKEND"]
celery.conf.update(task_track_started=True)


@celery.task(name="flights_search", acks_late=True, queue="flight_search")
def flights_search():
    response_a = requests.post("http://app:8000/provider_a/search")
    response_b = requests.post("http://app:8000/provider_b/search")

    response = json.loads(response_a.text) + json.loads(response_b.text)

    return response