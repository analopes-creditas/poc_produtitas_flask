import os
import json
from core.app import celery
from kafka import KafkaConsumer
from core.models.body_git import BodyGit
from core.services.publisher import Publisher
from core.services.api_github import ApiGitHub


class DataProduct:

    def __init__(self):
        self.git = ApiGitHub()
        self.pub = Publisher()
        self.generate_body = BodyGit()
        self.template_owner = os.getenv('GH_TEMPLATE_OWNER', '')


    def create_data_product(self, value: dict) -> str:
        """ Create a data product.

            Parameters:
                value (dict): Event message.
        """

        body = self.generate_body.create_repos_template(data=value)
        self.git.create_repos_template(
            template_owner=self.template_owner,
            template_repo=value['type_product'],
            body=body
        )
        self.pub.producer(key='data_product_created', value=body)
        print('Data product created')
        return 'Data product created'


@celery.task
def start_worker():
    consumer = KafkaConsumer(
        os.getenv('KFK_TOPIC_NAME', ''),
        # auto_offset_reset='earliest',
        # enable_auto_commit=True,
        # group_id='my-group',
        # consumer_timeout_ms=1000,
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    
    for event in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (event.topic, event.partition, event.offset, event.key, event.value))
        DataProduct().create_data_product(value=event.value)
