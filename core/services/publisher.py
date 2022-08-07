import os
import json
from datetime import datetime
from kafka import KafkaProducer


class Publisher:

    def __init__(self):
        self.kafka_server = os.getenv('KFK_SERVER', '')
        self.topic_name = os.getenv('KFK_TOPIC_NAME', '')


    def producer(self, key: str, value: dict) -> str:
        """ Kafka event producer.
        
            Parameters:
                key (str): Event key.
                value (dict): Event value.
        """

        producer = KafkaProducer(bootstrap_servers=self.kafka_server)
        producer.send(
            topic=self.topic_name,
            value=json.dumps(value).encode('utf-8'),
            key=bytes(key, encoding='utf-8'),
            timestamp_ms=int(datetime.timestamp(datetime.now()))
        )
        producer.flush()
        print("--- Sent to consumer ---")
        return 'Message published'
