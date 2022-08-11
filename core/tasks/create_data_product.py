import os
import json
from kafka import KafkaConsumer
from core.app import make_celery
from core.models.body_git import BodyGit
from core.services.publisher import Publisher
from core.services.api_github import ApiGitHub

celery = make_celery()

class CreateDataProduct:

    def __init__(self):
        self.git = ApiGitHub()
        self.pub = Publisher()
        self.generate_body = BodyGit()
        self.template_owner = os.getenv('GH_TEMPLATE_OWNER', '')


    def provision(self, key: str, value: dict) -> str:
        """ Create a data product.

            Parameters:
                key (str): Event key.
                value (dict): Event value.
        """

        body = self.generate_body.create_repos_template(data=value)
        self.git.create_repos_template(
            template_owner=self.template_owner,
            template_repo=key.split('_')[1],
            body=body
        )
        # self.pub.producer(key='data_product_created', value=body)
        print('Data product created')
        return 'Data product created'


@celery.task
def start_task_create():
    print("--- Creating Data Product ---")

    consumer = KafkaConsumer(
        os.getenv('KFK_TOPIC_NAME', ''),
        bootstrap_servers=[os.getenv('KFK_SERVER', '')],
        # auto_offset_reset='earliest',
        # enable_auto_commit=True,
        # group_id='',
        # consumer_timeout_ms=1000,
        # value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    for event in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (event.topic, event.partition, event.offset, event.key, event.value))
        CreateDataProduct().provision(key=event.key.decode('utf-8'), value=json.loads(event.value.decode('utf-8')))
