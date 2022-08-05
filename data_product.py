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
        self.kafka_server = os.getenv('KFK_SERVER', '')
        self.topic_name = os.getenv('KFK_TOPIC_NAME', '')
        self.template_owner = os.getenv('GH_TEMPLATE_OWNER', '')


    def create_data_product(self, value: dict) -> str:
        """ Create a data product.

            Parameters:
                value (dict): Event message.
        """

        body = self.generate_body.create_repos_template(data=value)
        self.git.create_repos_template(
            template_owner=self.template_owner, template_repo=f"{value['type']}Model", body=body)
        self.pub.producer(key='data_product_created', value=body)
        print('Data product created')
        return 'Data product created'


if __name__ == '__main__':
    dp = DataProduct()

    @celery.task(name="consumer_data_product")
    def consumer():
        consumer = KafkaConsumer(
            'datahub',
            value_deserializer=lambda m: json.loads(m.decode('utf-8')), # to deserialize kafka.producer.object into dict
        )
        for event in consumer:
            print ("%s:%d:%d: key=%s value=%s" % (event.topic, event.partition, event.offset, event.key, event.value))
            # dp.create_data_product(value=event.value)
            dp.create_data_product.delay(event.value)
