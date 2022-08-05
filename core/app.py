import os
import urllib3
from flask import Flask
from celery import Celery
from flask_cors import CORS
from datetime import datetime
from dotenv import load_dotenv
from settings import BaseConfig


load_dotenv()
urllib3.disable_warnings()
started_date = datetime.now()
celery = Celery(__name__, broker=BaseConfig.CELERY_BROKER_URL)

def create_app():
    # create and configure the app
    app = Flask(__name__)
    app_settings = os.getenv('APP_SETTINGS', BaseConfig)
    app.config.from_object(app_settings)
    CORS(app)
    celery.conf.update(app.config)

    # routes
    from core.routes.health import Health
    Health.register(app, route_base='/')

    from core.routes.webhook import Webhook
    Webhook.register(app, route_base='/webhook')

    return app


# from tasks.data_product import DataProduct
# from kafka import KafkaConsumer
# import json
# dp = DataProduct()

# @celery.task(name="consumer_data_product")
# def consumer():
#     consumer = KafkaConsumer(
#         'datahub',
#         value_deserializer=lambda m: json.loads(m.decode('utf-8')), # to deserialize kafka.producer.object into dict
#     )
#     for event in consumer:
#         print ("%s:%d:%d: key=%s value=%s" % (event.topic, event.partition, event.offset, event.key, event.value))
#         # dp.create_data_product(value=event.value)
#         dp.create_data_product.delay(event.value)